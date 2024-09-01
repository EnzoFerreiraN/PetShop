from typing import List
from pydantic import BaseModel


class Cliente (BaseModel):
    id: None | str = None
    nome: str
    telefone: str
    email: str
    endereco: str
    cidade: str

    class Config:
        orm_mode = True

class Animal (BaseModel):
    id: str
    cliente: Cliente
    nome: str 
    especie: str
    raca: str
    idade: int

    class Config:
        orm_mode = True
    
class Veterinario (BaseModel):
    id: str
    nome: str
    telefone: str
    email: str
    endereco: str
    cidade: str

    class Config:
        orm_mode = True

class Consulta (BaseModel):
    id : str
    animal: Animal
    veterinario: Veterinario
    data: str
    motivo: str
    diagnostico: str
    tratamento: str

    class Config:
        orm_mode = True

class Produto (BaseModel):
    id: str
    nome: str
    descricao: str
    preco: float
    quantidade: int

    class Config:
        orm_mode = True

class Venda (BaseModel):
    id: str
    data: str
    cliente: Cliente
    produtos: List[Produto]
    valor: float

    class Config:
        orm_mode = True

