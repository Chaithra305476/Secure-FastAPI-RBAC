from fastapi import APIRouter, Depends
from app.core.security import get_current_user, require_role

router = APIRouter(prefix="/data", tags=["data"])

@router.get("/me")
def read_own_profile(current_user: dict = Depends(get_current_user)):
    return {"message": f"Hello {current_user['username']}", "role": current_user["role"]}

@router.get("/admin-only")
def admin_dashboard(current_user: dict = Depends(require_role(["admin"]))):
    return {"message": "Welcome to the admin dashboard", "user": current_user["username"]}

@router.get("/manager-or-admin")
def manager_area(current_user: dict = Depends(require_role(["admin", "manager"]))):
    return {"message": "Manager-level access granted", "user": current_user["username"]}