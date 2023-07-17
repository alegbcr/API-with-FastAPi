import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

sqlite_file_name = "../database.sqlite"

# Este fragmento de código asigna la ruta absoluta del directorio del archivo actual a la variable base_dir.
base_dir = os.path.dirname(os.path.realpath(__file__))

# La variable database_url contiene una cadena de conexión a una base de datos SQLite utilizando la ruta absoluta del directorio del archivo actual y el nombre del archivo de la base de datos.
database_url = f"sqlite:///{os.path.join(base_dir, sqlite_file_name)}"

# La variable engine crea un objeto de motor de base de datos utilizando la cadena de conexión database_url y se configura para mostrar mensajes de depuración con el valor echo=True.
engine = create_engine(database_url, echo=True)

# La clase Session se configura para crear instancias de sesión utilizando el motor de base de datos engine como enlace.
Session = sessionmaker(bind=engine)

# La clase Base se configura para ser la clase base de todas las clases de mapeo ORM (Object-Relational Mapping) utilizando el patrón declarativo.
Base = declarative_base()
