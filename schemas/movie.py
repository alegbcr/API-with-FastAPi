from pydantic import BaseModel, Field
from typing import Optional


class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=5, max_length=50)
    overview: str = Field(min_length=15, max_length=250)
    year: int = Field(default=2022, le=2022)
    rating: float = Field(gt=0, le=10)
    category: str = Field(min_length=5, max_length=25)

    # Configuración para uso default
    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "title": "Nombre de la pelicula",
                "overview": "Descripcion de la pelicula",
                "year": "2009",
                "rating": 7.8,
                "category": "Accion",
            }
        }
