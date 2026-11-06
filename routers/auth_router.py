from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from sqlalchemy import select
from sqlalchemy.orm import Session
from dependencies import abrir_sessao
from models.usuario import Usuario
from schemas.usuario import UsuarioCriar, UsuarioResposta
from core.security import gerar_hash_senha, verificar_senha, criar_token

router = APIRouter(prefix="/auth")

@router.post("/cadastro", response_model=UsuarioResposta, status_code=201)
def criar_conta(dados: UsuarioCriar, db: Session = Depends(abrir_sessao)):
    verificar_email = db.scalar(select(Usuario).where(Usuario.email == dados.email))
    if verificar_email:
        raise HTTPException(status_code=409, detail="E-mail ja esta cadastrado")
    senha_criptografada = gerar_hash_senha(dados.senha)
    novo_usuario = Usuario(nome=dados.nome, email=dados.email, senha_hash=senha_criptografada)
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    return novo_usuario

@router.post("/login", status_code=200)
def logar_conta(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(abrir_sessao)):
    usuario_encontrado = db.scalar(select(Usuario).where(Usuario.email == form_data.username ))
    if not usuario_encontrado:
        raise HTTPException(status_code=400, detail="Email ou senha incorreta.")
    if not verificar_senha(senha_texto=form_data.password,senha_hash=usuario_encontrado.senha_hash):
        raise HTTPException(status_code=400, detail="Email ou senha incorreta.")
    return {"access_token": criar_token(usuario_encontrado.id), "token_type": "bearer"}
    