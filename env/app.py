import requests
import json

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

response = requests.get(url) #get para pegar informações
print(response) #200 é sucesso e 404 é erro

if response.status_code == 200:
    restaurantes = response.json()
    dados_restaurante = {}
    for restaurante in restaurantes:
        nome_restaurante = restaurante['Company']
        if nome_restaurante not in dados_restaurante:
            dados_restaurante[nome_restaurante] = []
        
        dados_restaurante[nome_restaurante].append({"item": restaurante['Item'], "preco": restaurante['price'], "descrição": restaurante['description']})
else:
    print(f'Erro ao acessar a API: {response.status_code}')


# print(dados_restaurante['Pizza Hut']) #Acessando o dicionário de restaurantes

for nome_restaurante, dados in dados_restaurante.items():
    nome_do_aquivo = f'{nome_restaurante}.json'
    with open(nome_do_aquivo, 'w') as arquivo_restaurante:
        json.dump(dados, arquivo_restaurante, indent=4)
        