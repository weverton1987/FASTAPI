import requests

#retorno = requests.get('http://127.0.0.1:8000')
retorno = requests.post('http://127.0.0.1:8000/usuario', params={"id": 4, 'nome': 'roberta', 'senha': 'minhasenha4'})

#print(retorno.json()['mensagem'])
print(retorno.json())