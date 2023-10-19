#criacao de listas
lista = ['chocolate','arroz','feijao','tomate']
numeros = [10,9,8]
print(lista)

#funcao para adicionar elemento em uma lista
lista.append('macarrao')
print(lista)

#funcao para remover elemento de uma lista
lista.remove('feijao')
print(lista)

#funcao para organizar a lista de forma crescente
lista.sort()
numeros.sort()
print(lista)
print(numeros)

#pegando um elemento da lista pela posicao
print(numeros[0])

#juntando duas listas
listaDupla = lista + numeros

print(listaDupla)

#limpando a lista
lista.clear()
print(lista)

#organizando a lista de forma contrária
numeros.reverse()
print(numeros)
