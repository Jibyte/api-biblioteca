from sqlalchemy.orm import Session
from app.models import Libro
from app.schemas import LibroCreate


# Obtener todos los libros (con soporte para paginación opcional que vimos en clase)
def get_libros(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Libro).offset(skip).limit(limit).all()


# Crear un nuevo libro en la base de datos
def create_libro(db: Session, libro: LibroCreate):
    # Instanciamos el modelo de SQLAlchemy con los datos validados por Pydantic
    db_libro = Libro(
        titulo=libro.titulo,
        autor=libro.autor,
        anio_publicacion=libro.anio_publicacion,
        editorial=libro.editorial,
    )

    # Guardamos en la base de datos (Operación transaccional)
    db.add(db_libro)
    db.commit()
    db.refresh(db_libro)  # Actualizamos el objeto para traer el ID autogenerado

    return db_libro