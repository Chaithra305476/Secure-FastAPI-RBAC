from fastapi import FastAPI
from app.database.session import engine, Base
from app.database import models
from app.routers import auth
from app.routers import auth, data_routes

app.include_router(auth.router)
app.include_router(data_routes.router)

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Secure API with RBAC")

app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "API is running"}