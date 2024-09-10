from typing import List
from fastapi import APIRouter, Depends
from infra.sqlalchemy.config.database import get_db
from infra.sqlalchemy.repositorios.clientes import repositorioClientes
from schemas import schemas
from sqlalchemy.orm import Session




router = APIRouter()

@router.get("/clientes", response_model=List[schemas.Cliente])
def listar_clientes(db: Session = Depends(get_db)):
    clientes = repositorioClientes(db).listar()
    return clientes


@router.post("/clientes", response_model=schemas.Cliente)
def criar_cliente(cliente: schemas.Cliente, db: Session = Depends(get_db)):
    cliente_criado = repositorioClientes(db).criar(cliente)
    return cliente_criado

@router.delete("/clientes/{cliente_id}", response_model=schemas.Cliente)
def deletar_cliente(cliente_id: int, db: Session = Depends(get_db)):
    cliente_deletado = repositorioClientes(db).deletar_cliente(cliente_id)
    return cliente_deletado