from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from infra.sqlalchemy.config.database import get_db
from infra.sqlalchemy.repositorios.animais import repositorioAnimais
from schemas import schemas


router = APIRouter()

@router.get("/animais", response_model=List[schemas.Animal])
def listar_animais(db: Session = Depends(get_db)):
    animais = repositorioAnimais(db).listar_animais()
    return animais

@router.post("/animais", response_model=schemas.Animal)
def criar_animal(animal: schemas.Animal, db: Session = Depends(get_db)):
    animal_criado = repositorioAnimais(db).cadastrar_animal(animal)
    return animal_criado

@router.delete("/animais/{animal_id}", response_model=schemas.Animal)
def deletar_animal(animal_id: int, db: Session = Depends(get_db)):
    animal_deletado = repositorioAnimais(db).deletar_animal(animal_id)
    return animal_deletado