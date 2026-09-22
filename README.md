# Calculadora com Bugs

Projeto de exemplo para praticar branches, bugfixes e pull requests no Git/GitHub.

## Bugs conhecidos

1. **Soma incorreta**: `somar(a, b)` está subtraindo em vez de somar.
2. **Divisão por zero**: `dividir(a, b)` não trata o caso `b == 0`.
3. **Cálculo de porcentagem errado**: `calcular_porcentagem(valor, percentual)` não divide o percentual por 100.

## Como rodar

```bash
python3 calculadora.py
```