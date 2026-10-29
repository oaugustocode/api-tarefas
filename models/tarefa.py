from datetime import datetime
from sqlalchemy import String, DateTime, func, false, ForeignKey
from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column
from core.database import Base

class Tarefa(Base):
    __tablename__ = "tarefa"

    id: Mapped[int] = mapped_column(primary_key=True,)
    titulo: Mapped[str] = mapped_column(String(50))
    descricao: Mapped[Optional[str]] = mapped_column(String(255))
    concluida: Mapped[bool] = mapped_column(default=False, server_default=false())
    criada_em: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    # 1 usuario podem ter muitas tarefas | muitas tarefas pertecem a 1 usuario
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuario.id"))
    