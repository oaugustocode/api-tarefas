"""Reúne a Base e todos os models num único ponto.

O Alembic só enxerga as tabelas dos models que foram importados, então
cada novo model deve ser importado aqui.
"""
from core.database import Base
from models.usuario import Usuario

__all__ = ["Base", "Usuario"]
