def dividir(numerador, denominador):
    # Se o dominador for zero, levanta uma exceção do tipo ValueError.
    if denominador == 0:
        raise ValueError("Divisão por zero não é permitida!")
    return numerador / denominador

try:
    resultado = dividir(10, 0)
    print("Resultado:", resultado)
except ValueError as erro:
    # Capturamos a exeção e exibimos a mensagem de erro.
    print("Ocorreu um erro:", erro)
