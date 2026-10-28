from sqlalchemy.orm import Session
from app.models import Libro
from app.schemas import LibroCreate


# Obtener todos los libros
def get_libros(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Libro).offset(skip).limit(limit).all()


# Crear un nuevo libro en la base de datos
def create_libro(db: Session, libro: LibroCreate):
    db_libro = Libro(
        titulo=libro.titulo,
        autor=libro.autor,
        anio_publicacion=libro.anio_publicacion,
        editorial=libro.editorial,
    )
    db.add(db_libro)
    db.commit()
    db.refresh(db_libro)
    return db_libro