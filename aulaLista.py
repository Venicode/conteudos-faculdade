numeros = [3,2,1]
palavras = ['teste','testando',1]
print(numeros)

numeros.append(4)
print(numeros)

listaDupla = numeros + palavras
print(listaDupla)

for elemento in numeros:
    soma = int(elemento)+1
    print(soma)

numeros.sort()
print(numeros)
