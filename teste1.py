from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

@app.get('/teste1/{id}')
def main(id: int):
    return {'valor': id*2}