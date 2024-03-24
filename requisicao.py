import requests

#retorno = requests.get('http://127.0.0.1:8000')
retorno = requests.post('http://127.0.0.1:8000/usuario', params={"nome": 'caio'})

#print(retorno.json()['mensagem'])
print(retorno.json())