#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e 
#continue pedindo até que o usuário informe um valor válido.
numero = 0
numero = float(input("Digite um número entre 0 e 10:"))

while(numero<0 or numero>10):
    numero = float(input("Digite um número entre 0 e 10:"))
print("Número válido.")