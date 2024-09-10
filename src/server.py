from fastapi import FastAPI
from infra.sqlalchemy.config.database import criar_banco 
from fastapi.middleware.cors import CORSMiddleware
from routers import routers_animais, routers_clientes



criar_banco()
app = FastAPI()

origins = ['http://localhost:5500']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


#clientes

app.include_router(routers_clientes.router)


#animais

app.include_router(routers_animais.router)