from sqlalchemy.orm import Session
from sqlalchemy import text
from app.database.session import get_db
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

from sqlalchemy import text

@router.get("/user-count-by-role")
def user_count_by_role(db: Session = Depends(get_db)):
    result = db.execute(text("SELECT role, COUNT(*) as count FROM users GROUP BY role"))
    rows = result.fetchall()
    return [{"role": row.role, "count": row.count} for row in rows]