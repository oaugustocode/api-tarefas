from passlib.context import CryptContext
import jwt
from datetime import datetime, timedelta, timezone
from core.config import ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY

context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def gerar_hash_senha(senha_texto: str) -> str:
    return context.hash(senha_texto)


def verificar_senha(senha_texto: str, senha_hash: str) -> bool:
    return context.verify(senha_texto, senha_hash)

def criar_token(usuario_id: int) -> str:
    expiracao = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    payload = {
        "sub": str(usuario_id),
        "exp": expiracao
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
