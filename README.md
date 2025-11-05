# Atividade Prática 04
>
> [Universidade Federal do Ceará (UFC)](https://www.ufc.br/)\
> [Departamento de Computação (DC)](https://dc.ufc.br/pt/)\
> Disciplina: Engenharia de Sistemas Inteligentes (CK0444 – 2025.2)\
> Professor: [Lincoln S. Rocha](http://lattes.cnpq.br/0656977742590515)\
> E-mail: <lincoln@dc.ufc.br>
>

Prática de Build Automatizado e CI com GitHub Actions

Objetivos

- Fixar comandos do Poetry.
- Criar uma aplicação simples de calculadora usando Flask e Poetry.
- Fixar configurações básicas do GitHub actions.  
- Usar commit na `main` como gatilho para execução de CI via GitHub Actions.

## 1. Pré-requisitos

- Conta ativa no GitHub.
- Poetry instalado localmente (`pip install poetry`).
- Git instalado localmente (ou GitHub Desktop).
- Editor de código de sua preferência.

## 2. Roteiro da Prática

### 2.1. Ajustando o Projeto ``webcalc``

>
> OBS. Esse passo pode ser feito usando uma IDE como VS Code.
>

- Navegue até a pasta ``webcalc`` (ela esta junto com as instruções para a realização desta tarefa no SIGAA). Ela deve apresentar a seguinte estrutura:

```bash
webcalc
├── src
│   ├── webcalc
│   │   ├── __init__.py
│   │   ├── app.py
│   │   └── calculadora.py
├── tests
│   ├── __init__.py
│   ├── test_app.py
│   └── test_calculadora.py
├── pyproject.toml
└── README.md
```

- Abra o arquivo ``pyproject.toml`` e altere o trecho a baixo com seu nome e email e salve o arquivo:

```bash
authors = [
    {name = "Seu Nome",email = "eu.email@exemplo.com"}
]
```

- No terminal, navegue até o diretório raiz ``webcalc`` e instale o pacote usando o Poetry:

```bash
cd webcalc
poetry install
```

- Deve ser exibido no terminal algo parecido com o descrito abaixo:

```bash
Creating virtualenv webcalc-iW8W5cNC-py3.9 in /Users/lincolnrocha/Library/Caches/pypoetry/virtualenvs
Updating dependencies
Resolving dependencies... (1.3s)

Package operations: 9 installs, 0 updates, 0 removals

  - Installing markupsafe (3.0.2)
  - Installing zipp (3.21.0)
  - Installing blinker (1.9.0)
  - Installing click (8.1.8)
  - Installing importlib-metadata (8.7.0)
  - Installing itsdangerous (2.2.0)
  - Installing jinja2 (3.1.6)
  - Installing werkzeug (3.1.3)
  - Installing flask (3.1.1)

Writing lock file

Installing the current project: webcalc (0.0.1)
```

- Agora, no diretório raiz ``webcalc``, execute a aplicação usando Poetry:

```bash
poetry run python -u -m webcalc.app
```

- Deve ser exibido no terminal algo parecido com o descrito abaixo:

```bash
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 145-585-503
 ```

- Abra outro terminal e navegue até o diretório raiz ``webcalc``. Em seguida, execute os testes unitários usando Poetry:

```bash
poetry run python -u -m unittest discover tests
```

- Deve ser exibido no terminal algo parecido com o descrito abaixo:

```bash
.....
----------------------------------------------------------------------
Ran 10 tests in 0.009s

OK
---
```

### 2.2. Criação do repositório remoto no GitHub

1. Acesse o [GitHub](https://github.com/) e faça login.  
2. Clique em **New repository**.  
3. Preencha:
   - **Repository name:** `webcalc`
   - **Description (opcional):** “Repositório para prática de GitHub Actions”
   - **Visibility:** Public  
4. Em **Add .gitignore**, indique **gitignore template: Python**
5. Clique em **Create repository**.

### 2.3. Clone do Repositório e primeiro commit local

>
> OBS. Esse passo pode ser feito usando uma IDE como VS Code.
>

- Clone o repositório remoto ``webcalc``

```bash
git clone https://github.com/SEU_USUARIO/webcalc.git
```

- Vá para o diretório `webcalc` para realizar a configuração do Git

```bash
git config user.name "Seu Nome igual ao GitHub"
```

```bash
git config user.email seu.email@igual.do.github
```

- Copie o conteúdo da pasta ``webcalc`` fornecida junto com as instruções desta tarefa para dentro da pasta ``webcalc`` do repositório Git que você clonou no início deste passo.

- No seu computador, abra o arquivo ``gitignore_content.txt``, fornecido junto com as instruções desta tarefa. Copie o conteúdo deste arquivo para dentro do arquivo ``.gitignore`` que está no seu repositório local.

- Agora, faça com que o Git rastreie todos arquivos copiados/alterados:

```bash
git add .
```

- Realize um `commit` e, em seguida, um `push`para enviar as alterações para o GitHub:

```bash
git commit -m "Primeira versão de webcalc!"
```

```bash
git push -u origin
```

### 2.4. Criando o pipeline no GitHub Actions

1. Use o navegador web para ir até o seu repositório no GitHub.
2. Clique em **Actions**.
3. Clique em **New workflow**.
4. Vá em **Python application** e cliquem em **Configure**
5. Na tela de edição, renomeie o arquivo de ``python-app.yml`` para ``webcalc-ci.yml``.
6. No seu computador, abra o arquivo ``webcalc-ci.yml``, fornecido junto com as instruções desta tarefa, e copie o conteúdo deste arquivo para dentro do arquivo que está em edição no GitHub.
7. Clique em **Commit changes** e realize o commit com as alterações.
8. Clique em **Actions** e veja os detalhes da exeução da pipeline.

### 2.5. Entrega da Tarefa

Agora você deve enviar via SIGAA o link do repositório remoto (``https://github.com/SEU_USUARIO_GITHUB/webcalc``) como reposta desta tarefa. OBS. A análise do log do repositório será utilizado para verificar a realização correta da tarefa.
