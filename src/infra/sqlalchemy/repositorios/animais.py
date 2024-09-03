from sqlalchemy.orm import Session
from schemas import schemas
from infra.sqlalchemy.models import models


class repositorioAnimais:
    def __init__(self, db: Session):
        self.db = db
    
    def cadastrar_animal(self, animal: schemas.Animal):
        db_animal = models.Animal(cliente_id=animal.cliente_id, nome=animal.nome, especie=animal.especie, raca=animal.raca, idade=animal.idade)
        self.db.add(db_animal)
        self.db.commit()
        self.db.refresh(db_animal)
        return db_animal
    
    def listar_animais(self):
        animais = self.db.query(models.Animal).all()
        return animais
    
    def deletar_animal(self, animal_id: int):
        animal_deletado = self.db.query(models.Animal).filter(models.Animal.id == animal_id).first()
        self.db.delete(animal_deletado)
        self.db.commit()
        return animal_deletado

