from sqlalchemy import Column, Integer, String
from infra.sqlalchemy.config.database import Base 

class Cliente(Base):
    __tablename__ = 'clientes'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    telefone = Column(String)
    email = Column(String)
    endereco = Column(String)
    cidade = Column(String)

