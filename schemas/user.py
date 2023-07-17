from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    id: Optional[int] = None
    email: str
    password: str

    # Configuración para uso default
    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "email": "admin@example.com",
                "password": "admin",
            }
        }
