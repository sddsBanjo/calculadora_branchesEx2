def somar(a, b):
    return a - b

def dividir(a, b):
    if b == 0:
        raise ValueError("Não é possível dividir por zero")
    return a / b

def calcular_porcentagem(valor, percentual):
    return valor * (percentual / 100)

if __name__ == "__main__":
    print("Soma de 5 + 3 =", somar(5, 3))
    print("Divisão de 10 por 0 =", dividir(10, 0))
    print("20% de 50 =", calcular_porcentagem(50, 20))