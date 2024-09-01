from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session 
from infra.sqlalchemy.config.database import get_db,criar_banco 
from schemas import schemas
from infra.sqlalchemy.repositorios.clientes import repositorioClientes 


criar_banco()
app = FastAPI()

@app.get("/clientes")
def listar_clientes(db: Session = Depends(get_db)):
    clientes = repositorioClientes(db).listar()
    return clientes


@app.post("/clientes")
def criar_cliente(cliente: schemas.Cliente, db: Session = Depends(get_db)):
    cliente_criado = repositorioClientes(db).criar(cliente)
    return cliente_criado

