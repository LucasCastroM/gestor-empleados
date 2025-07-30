# Importaciones necesarias de SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuración de la base de datos
# SQLite es una base de datos ligera que se guarda en un archivo
# Perfecta para desarrollo y proyectos pequeños
DATABASE_URL = "sqlite:///./gestor_empleados.db"

# Crear el motor de la base de datos
# El motor es la conexión principal con la base de datos
engine = create_engine(DATABASE_URL)

# Crear la sesión de la base de datos
# Las sesiones permiten hacer operaciones (crear, leer, actualizar, eliminar)
# autocommit=False: No guarda automáticamente los cambios
# autoflush=False: No sincroniza automáticamente con la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crear la clase base para los modelos
# Todos nuestros modelos (tablas) heredarán de esta clase
Base = declarative_base()

# Función para obtener la sesión de la base de datos
# Esta función se usa en cada endpoint para obtener una conexión
def get_db():
    db = SessionLocal()  # Crear una nueva sesión
    try:
        yield db  # Devolver la sesión al endpoint
    finally:
        db.close()  # Cerrar la sesión al terminar (importante para liberar recursos)

        