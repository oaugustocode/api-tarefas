from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL is None:
    raise RuntimeError("A variável DATABASE_URL não foi definida. Crie o arquivo .env.")

SECRET_KEY = os.getenv("SECRET_KEY")

if SECRET_KEY is None:
    raise RuntimeError("A variável SECRET_KEY não foi definida. Crie o arquivo .env.")

ALGORITHM = os.getenv("ALGORITHM")

if ALGORITHM is None:
    raise RuntimeError("A variável ALGORITHM não foi definida. Crie o arquivo .env.")

ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")

if ACCESS_TOKEN_EXPIRE_MINUTES is None:
    raise RuntimeError("A variável ACCESS_TOKEN_EXPIRE_MINUTES não foi definida. Crie o arquivo .env.")

ACCESS_TOKEN_EXPIRE_MINUTES = int(ACCESS_TOKEN_EXPIRE_MINUTES)