from fastapi import APIRouter
from fastapi.responses import JSONResponse
from typing import List

from utils.jwt_manager import create_token
from schemas.user import User

user_router = APIRouter()


@user_router.post("/login", tags=["auth"], status_code=200)
def login(user: User):
    # Generar token
    if user.email == "admin@example.com" and user.password == "admin":
        token: str = create_token(user.dict())
        return JSONResponse(status_code=200, content=token)
    # Valida el token
