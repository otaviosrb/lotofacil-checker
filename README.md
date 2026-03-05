# 🎰 Lotofácil Checker

Aplicação em **Python** que consulta automaticamente o resultado da **Lotofácil** através de uma API pública e compara com os números digitados pelo usuário, mostrando quantos acertos ele teve.

Este projeto foi desenvolvido para praticar **consumo de APIs, manipulação de dados e lógica em Python**.

---

# 🚀 Funcionalidades

* 🔎 Buscar resultados de concursos da Lotofácil via API
* 🎯 Inserir manualmente os números do seu jogo
* 📊 Comparar automaticamente seu jogo com o sorteio
* ✅ Mostrar:

  * quantidade de acertos
  * números acertados
  * seu jogo
  * números sorteados

---

# 🧠 Tecnologias utilizadas

* Python 3
* Biblioteca `requests`
* API pública de resultados da Lotofácil

---

# 📦 Instalação

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/lotofacil-checker.git
```

Entre na pasta do projeto:

```bash
cd lotofacil-checker
```

Instale a dependência necessária:

```bash
pip install requests
```

---

# ▶️ Como executar

Execute o script:

```bash
python main.py
```

O programa irá solicitar:

1. Número do concurso
2. Quantidade de números jogados (15 a 20)
3. Os números do seu jogo

Depois disso ele mostrará o resultado da comparação.

---

# 💻 Exemplo de uso

```
Digite o nº do concurso (0 para sair): 3100
Digite a quantidade de números jogados (15-20): 15

=============== RESULTADO ===============
Concurso: 3100 | Data: 2024-03-01
Acertos:  11
Dezenas:  [2, 5, 7, 8, 11, 13, 15, 19, 20, 23, 24]
----------------------------------------
Seu Jogo:  [2, 5, 7, 8, 9, 11, 13, 15, 18, 19, 20, 21, 23, 24, 25]
Sorteio:   [1, 2, 5, 7, 8, 11, 13, 15, 19, 20, 23, 24, 3, 10, 14]
========================================
```

---

# 🔗 API utilizada

Os dados do sorteio são obtidos através da API:

```
https://api.guidi.dev.br/loteria/lotofacil/{concurso}
```

Ela retorna um JSON contendo informações como:

* dezenas sorteadas
* data do sorteio
* número do concurso

---

# 📚 Aprendizados

Com esse projeto foi possível praticar:

* consumo de API com `requests`
* manipulação de listas e conjuntos
* tratamento de erros com `try/except`
* validação de entrada do usuário
* organização de código em funções

---

# 📌 Melhorias futuras

* Permitir múltiplos jogos
* Gerar jogos aleatórios
* Criar interface gráfica
* Salvar histórico de jogos
* Adicionar suporte para outras loterias

---

# 👨‍💻 Autor

Desenvolvido por **Otávio Ribeiro**

