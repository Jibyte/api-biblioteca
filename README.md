# API Biblioteca - FastAPI y MySQL

## Descripción General

Este repositorio contiene el desarrollo de una API RESTful orientada a la gestión de una biblioteca, construida de manera autodidacta con el apoyo de herramientas de inteligencia artificial y asistencia técnica iterativa. El proyecto implementa operaciones de creación y consulta de registros (CRUD) utilizando tecnologías modernas de desarrollo backend en Python.

El propósito principal de este proyecto es consolidar los fundamentos de arquitectura de software, mapeo objeto-relacional (ORM), gestión de bases de datos relacionales y diseño de endpoints bajo buenas prácticas de ingeniería de software.

## Arquitectura y Tecnologias Utilizadas

* **Lenguaje:** Python
* **Framework Web:** FastAPI (para la construcción rápida y documentada de la API REST).
* **ORM:** SQLAlchemy (para la interacción orientada a objetos con la base de datos).
* **Conector de Base de Datos:** PyMySQL (como controlador de conexión para MySQL).
* **Servidor ASGI:** Uvicorn (para la ejecución del servidor de desarrollo local).
* **Gestión de Entorno:** Python-Dotenv (para la carga segura de credenciales mediante variables de entorno).
* **Base de Datos:** MySQL (almacenamiento relacional estructurado).
* **Pruebas de API:** Postman / Interfaz Swagger UI integrada en FastAPI.

## Estructura del Proyecto

La estructura del proyecto sigue una separación clara de responsabilidades:

* `app/main.py`: Punto de entrada de la aplicación FastAPI y configuración del servidor.
* `app/database.py`: Configuración del motor de conexión a la base de datos y la sesión de SQLAlchemy.
* `app/models.py`: Definición de los modelos de datos y esquemas de tablas relacionales (ORM).
* `app/schemas.py`: Validación y serialización de datos mediante Pydantic.
* `.env`: Archivo de configuración local para las credenciales de acceso a la base de datos.

## Configuración y Ejecucion Local

1. Clonar el repositorio y posicionarse en la carpeta raíz del proyecto.
2. Crear y activar un entorno virtual de Python:
```bash
python3 -m venv venv
source venv/bin/activate

```


3. Instalar las dependencias necesarias:
```bash
pip install fastapi uvicorn sqlalchemy pymysql python-dotenv pydantic

```


4. Configurar el archivo `.env` en la raíz con las credenciales de acceso a MySQL:
```env
DB_USER=tu_usuario
DB_PASSWORD=tu_contrasena
DB_HOST=localhost
DB_PORT=3306
DB_NAME=biblioteca_db

```


5. Ejecutar el servidor de desarrollo mediante Uvicorn:
```bash
uvicorn app.main:app --reload

```