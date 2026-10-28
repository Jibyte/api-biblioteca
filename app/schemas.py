from typing import Optional
from pydantic import BaseModel


# Esquema base con los campos comunes de un libro
class LibroBase(BaseModel):
    titulo: str
    autor: str
    anio_publicacion: int
    editorial: Optional[str] = None


# Esquema para cuando un usuario CREA un libro (Hereda de LibroBase)
class LibroCreate(LibroBase):
    pass


# Esquema para cuando la API DEVUELVE un libro al cliente (incluye el ID de la BD)
class LibroResponse(LibroBase):
    id: int

    class Config:
        from_attributes = True  # Permite leer datos directamente desde modelos de SQLAlchemy