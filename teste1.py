from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

usuarios = [(1, 'caio', 'minhasenha1'), (2, 'joao', 'minhasenha2')]

# @app.get('/usuario/{id}')
# def main(id: int):
#     for i in usuarios:
#         if i[0] == id:
#             return i
#     return 'nao existe'

@app.post('/usuario')
def main(nome):
    for i in usuarios:
        if i[1] == nome:
            return i
    return 'nao existe'