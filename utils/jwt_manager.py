import os
from dotenv import load_dotenv
from jwt import encode, decode

load_dotenv()  # --> take environment variables from .env.
secret_key = os.getenv("SECRET_KEY")


def create_token(data: dict) -> str:
    # payload --> contenido que se convertira en el token
    # key --> es un string que se usa para generar el token (llave secreta)
    # algorithm --> es el algoritmo usado para generar el token, por lo general es HS256
    token: str = encode(payload=data, key=secret_key, algorithm="HS256")
    return token


def validate_token(token: str) -> dict:
    # token --> es el token que se quiere validar
    # key --> es un string que se usa para generar el token (llave secreta)
    # algorithm --> es el algoritmo usado para decodificar el token y viene como una lista
    data: dict = decode(token, key=secret_key, algorithms=["HS256"])
    return data
