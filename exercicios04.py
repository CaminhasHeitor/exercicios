def somar_pares(lista):
    total = 0 
    for i in lista:
        total += i

    media = total / len(lista)
    return media

numeros = [3, 5, 79, 684, 500]

print(somar_pares(numeros))