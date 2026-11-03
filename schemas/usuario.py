from pydantic import BaseModel, EmailStr, Field, ConfigDict, field_validator, StringConstraints
from typing import Annotated

class UsuarioCriar(BaseModel):
    nome: Annotated[str, StringConstraints(strip_whitespace=True, min_length=2, max_length=100)]
    email: Annotated[EmailStr, StringConstraints(strip_whitespace=True,max_length=200)]
    senha: str = Field(min_length=12, max_length=32)

    @field_validator("senha")
    @classmethod
    def validar_senha(cls, valor: str) -> str:
        if len(valor.encode()) > 72:
            raise ValueError("A Senha ultrapassa os bytes aceitos, prefira por uma senha menor")
        return valor

    
class UsuarioResposta(BaseModel):
    id: int
    nome: str
    email: str

    model_config = ConfigDict(from_attributes=True)

    

