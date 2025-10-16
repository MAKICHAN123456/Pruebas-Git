def sumarValores(*valores):
    return sum(valores)
numeros = []
for i in range(3):
    ask = int(input("Coloca un numero para sumar: "))
    numeros.append(ask)
resultado = sumarValores(*numeros)
print(f"Resultado: {resultado}")