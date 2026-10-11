# Sistema WebCalc com Flask

## Como Rodar WebCalc

```bash
poetry run python -u -m webcalc.app
```

## Como Usar WebCalc

- Exemplo de operação de de adição:

```bash
http://127.0.0.1:5000/add?a=10&b=10
```

- Exemplo de operação de de subtração:

```bash
http://127.0.0.1:5000/sub?a=20&b=10
```

- Exemplo de operação de de multiplicação:

```bash
http://127.0.0.1:5000/mut?a=5&b=10
```

- Exemplo de operação de de divisão:

```bash
http://127.0.0.1:5000/divb?a=10&b=5
```

## Como Testar WebCalc

```bash
poetry run python -u -m unittest discover tests
```
