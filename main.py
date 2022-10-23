from fastapi import FastAPI
from db import Database

app = FastAPI()

@app.get('/')
def root():
    return {'mensaje': 'Simple Api con sqlite3'}


# Devolver todas las personas de la base de datos
@app.get('/personas')
def read_personas():
    return Database.read_personas()


# Devolver personas que empiezen con el nombre enviado
@app.get('/personas/nombre/{nombre}')
def read_persons_by_nombre(nombre:str):
    return Database.read_persons_by_nombre(nombre)


# Devolver persona de la base de datos por id mediante parametros url
@app.get('/persona')
def read_person_by_id_param(id:int):
    persona = Database.read_person_by_id(id)
    return persona if persona else []


# Devolver persona de la base de datos por id mediante url
@app.get('/persona/id/{id}')
def read_person_by_id(id:int):
    persona = Database.read_person_by_id(id)
    return persona if persona else []
