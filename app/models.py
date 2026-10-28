from sqlalchemy import Column, Integer, String
from app.database import Base


class Libro(Base):
    __tablename__ = "libros"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    titulo = Column(String(150), nullable=False)
    autor = Column(String(100), nullable=False)
    anio_publicacion = Column(Integer, nullable=False)
    editorial = Column(String(100), nullable=True)