from datetime import datetime
from sqlalchemy import String, DateTime, func, false
from sqlalchemy.orm import Mapped, mapped_column
from core.database import Base



class Usuario(Base):
    __tablename__ = "usuario"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(200), unique=True)
    criado_em: Mapped[datetime] = mapped_column(
            DateTime(timezone=True), 
            server_default=func.now()
            )
    senha_hash: Mapped[str] = mapped_column(String(255))
    admin: Mapped[bool] = mapped_column(default=False, server_default=false())
