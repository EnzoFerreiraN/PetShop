from sqlalchemy.orm import Session  
from schemas import schemas
from infra.sqlalchemy.models import models


class repositorioClientes:
    def __init__(self, db: Session):
        self.db = db
    
    def criar (self, cliente: schemas.Cliente):
        db_cliente = models.Cliente(nome=cliente.nome, telefone=cliente.telefone, email=cliente.email, endereco=cliente.endereco, cidade=cliente.cidade)
        self.db.add(db_cliente)
        self.db.commit()
        self.db.refresh(db_cliente)
        return db_cliente
    
    def listar (self):
        clientes = self.db.query(models.Cliente).all()
        return clientes
    