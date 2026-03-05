import requests
import os

def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def obter_concurso():
    while True:
        entrada = input('Digite o nº do concurso (0 para sair): ').strip()
        if entrada == '0':
            return None
        if entrada.isdigit():
            return entrada
        return 'Erro, digite apenas números'
    
def obter_jogo(quantidade):
    jogo = set()
    while len(jogo) < quantidade:
        print(f'Digite os {quantidade} números do seu jogo (1 a 25): ')
        try:
            num = int(input(f'{len(jogo) + 1}º número: '))
            if 1 <= num <= 25:
                if num not in jogo:
                    jogo.add(num)
                    limpa_tela()
                else:
                    limpa_tela()
                    print('Atenção! Você já digitou esse número')
            else:
                limpa_tela()
                print('Erro: Digite um nº entre 1 e 25')
        except:
            limpa_tela()
            print('Erro', NameError)
    return sorted(list(jogo))


while True:
    concurso = obter_concurso()
    if not concurso:
        break

    try:
        url = f"https://api.guidi.dev.br/loteria/lotofacil/{concurso}"
        resposta = requests.get(url, timeout=5)
        resposta.raise_for_status()
        dados = resposta.json()
        sorteados = [int(n) for n in dados["listaDezenas"]]
    except Exception as e:
        limpa_tela()
        print(f'Não foi possível obter os dados: {e}')
        continue

    while True:
        try:
            quantidade = int(input('Digite a quantidade de números jogados (15-20): '))
            if 15 <= quantidade <= 20:
                break
            print("A Lotofácil permite de 15 a 20 números")
        except ValueError:
            print('Digite um número inteiro')
    
    meu_jogo = obter_jogo(quantidade)

    acertos = sorted(list(set(sorteados) & set(meu_jogo)))

    limpa_tela()
    print(f"{' RESULTADO ':=^40}")
    print(f"Concurso: {concurso} | Data: {dados.get('dataApuracao')}")
    print(f"Acertos:  {len(acertos)}")
    print(f"Dezenas:  {acertos}")
    print("-" * 40)
    print(f"Seu Jogo:  {meu_jogo}")
    print(f"Sorteio:   {sorteados}")
    print("=" * 40 + "\n")