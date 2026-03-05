import requests
import os

def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

concurso = int(input('Digite o nº do concurso: '))
limpa_tela()

url = f"https://api.guidi.dev.br/loteria/lotofacil/{concurso}"

resposta = requests.get(url)
dados = resposta.json()

numeros_corretos = dados["listaDezenas"]

qtd_numeros = int(input('Digite a quantidade de números que você jogou: '))
limpa_tela()

# numeros_escolhidos = ['02', '03', '04', '05', '06', '07', '09', '11', '13', '17', '18', '19', '20', '21', '22', '24']
numeros_escolhidos = []
for n in range(qtd_numeros):
    n = input(f'Digite o {n+1}º: ')
    numeros_escolhidos.append(n)
    limpa_tela()

acertos = sorted(set(numeros_corretos) & set(numeros_escolhidos))

print(f'CONCURSO: {concurso}')
print('='*100)
print(f'Você acertou {len(acertos)} números')
print(acertos)
print('='*100)
print('Números Escolhidos:', numeros_escolhidos)
print('Números Corretos:', numeros_corretos)
