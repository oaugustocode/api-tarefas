from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session
from dependencies import abrir_sessao
from models.usuario import Usuario
from schemas.usuario import UsuarioCriar, UsuarioResposta
from core.security import gerar_hash_senha, verificar_senha

router = APIRouter(prefix="/auth")

@router.post("/cadastro", response_model=UsuarioResposta, status_code=201)
def cadastrar_usuario(dados: UsuarioCriar, db: Session = Depends(abrir_sessao)):
    verificar_email = db.scalar(select(Usuario).where(Usuario.email == dados.email))
    if verificar_email:
        raise HTTPException(status_code=409, detail="Esse email ja foi usado")
    senha_criptografada = gerar_hash_senha(dados.senha)
    novo_usuario = Usuario(nome=dados.nome,senha_hash=senha_criptografada,email=dados.email)
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    return novo_usuario