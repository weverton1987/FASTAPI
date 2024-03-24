from fastapi import FastAPI
'''O fastapi utiliza o servidor do uvicorn, depois do uvicorn a gnt coloca o nome da nossa pasta no caso "teste"
ai coloca : depois o nome da instância da fastapi que no caso é "app" e e um parametro adicional que é o
--reload que serve pra ele ficar carregando automatico, então ficaria assim "uvicorn teste:app --reload"'''

app = FastAPI()

@app.get('/')
def root():
    return {'mensagem': 'home'}

@app.get('/cadastro')
def cadstro():
    return {'mensagem': 'cadastrado'}

@app.get('/login')
def login():
    return {'mensagem': 'logado'}