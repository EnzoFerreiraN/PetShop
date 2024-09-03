from typing import List
from pydantic import BaseModel, ConfigDict


class Cliente (BaseModel):
    id: None | int = None
    nome: str
    telefone: str
    email: str
    endereco: str
    cidade: str

    model_config = ConfigDict(from_attributes=True)

class Animal (BaseModel):
    id: None | int = None
    cliente_id: int
    nome: str 
    especie: str
    raca: str
    idade: int
    cliente: None | Cliente = None

    model_config = ConfigDict(from_attributes=True)
    
class Veterinario (BaseModel):
    id: str
    nome: str
    telefone: str
    email: str
    endereco: str
    cidade: str

    

class Consulta (BaseModel):
    id : str
    animal: Animal
    veterinario: Veterinario
    data: str
    motivo: str
    diagnostico: str
    tratamento: str

    

class Produto (BaseModel):
    id: str
    nome: str
    descricao: str
    preco: float
    quantidade: int

    

class Venda (BaseModel):
    id: str
    data: str
    cliente: Cliente
    produtos: List[Produto]
    valor: float

   

