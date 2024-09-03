from typing import List
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session 
from infra.sqlalchemy.config.database import get_db,criar_banco 
from infra.sqlalchemy.models import models
from schemas import schemas
from infra.sqlalchemy.repositorios.clientes import repositorioClientes
from infra.sqlalchemy.repositorios.animais import repositorioAnimais


criar_banco()
app = FastAPI()

#clientes

@app.get("/clientes", response_model=List[schemas.Cliente])
def listar_clientes(db: Session = Depends(get_db)):
    clientes = repositorioClientes(db).listar()
    return clientes


@app.post("/clientes", response_model=schemas.Cliente)
def criar_cliente(cliente: schemas.Cliente, db: Session = Depends(get_db)):
    cliente_criado = repositorioClientes(db).criar(cliente)
    return cliente_criado

@app.delete("/clientes/{cliente_id}", response_model=schemas.Cliente)
def deletar_cliente(cliente_id: int, db: Session = Depends(get_db)):
    cliente_deletado = repositorioClientes(db).deletar_cliente(cliente_id)
    return cliente_deletado



#animais

@app.get("/animais", response_model=List[schemas.Animal])
def listar_animais(db: Session = Depends(get_db)):
    animais = repositorioAnimais(db).listar_animais()
    return animais

@app.post("/animais", response_model=schemas.Animal)
def criar_animal(animal: schemas.Animal, db: Session = Depends(get_db)):
    animal_criado = repositorioAnimais(db).cadastrar_animal(animal)
    return animal_criado

@app.delete("/animais/{animal_id}", response_model=schemas.Animal)
def deletar_animal(animal_id: int, db: Session = Depends(get_db)):
    animal_deletado = repositorioAnimais(db).deletar_animal(animal_id)
    return animal_deletado