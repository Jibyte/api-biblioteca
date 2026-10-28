from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from app import crud
from app.database import engine, get_db
from app.models import Base
from app.schemas import LibroCreate, LibroResponse

# Creamos las tablas en la base de datos automáticamente si no existen
Base.metadata.create_all(bind=engine)

# Inicializamos la aplicación FastAPI
app = FastAPI(
    title="API Biblioteca UdeA",
    description="API desarrollada con FastAPI y MySQL para la gestión de libros",
    version="1.0.0"
)


# Endpoint GET: Listar todos los libros
@app.get("/libros/", response_model=List[LibroResponse], summary="Obtener lista de libros")
def listar_libros(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    libros = crud.get_libros(db, skip=skip, limit=limit)
    return libros


# Endpoint POST: Crear un nuevo libro
@app.post("/libros/", response_model=LibroResponse, status_code=201, summary="Registrar un nuevo libro")
def crear_libro(libro: LibroCreate, db: Session = Depends(get_db)):
    return crud.create_libro(db=db, libro=libro)