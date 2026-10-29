from passlib.context import CryptContext
context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def gerar_hash_senha(senha_texto: str) -> str:
     return context.hash(senha_texto)

def verificar_senha(senha_texto: str, senha_hash: str) -> bool:
    return context.verify(senha_texto, senha_hash)