from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer, String
from infra.sqlalchemy.config.database import Base 
#from src.infra.sqlalchemy.config.database import Base

class Cliente(Base):
    __tablename__ = 'clientes'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    telefone = Column(String)
    email = Column(String)
    endereco = Column(String)
    cidade = Column(String)

    animais = relationship("Animal", back_populates="cliente")

class Animal(Base):
    __tablename__ = 'animais'

    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey('clientes.id', name='fk_cliente_id'))
    nome = Column(String)
    especie = Column(String)
    raca = Column(String)
    idade = Column(Integer)

    cliente = relationship("Cliente", back_populates="animais")

