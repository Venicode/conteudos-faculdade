def linhas():
    print('*'*30)

def Soma(n1,n2):
    soma = n1 + n2
    print(soma)

def Sub(n1,n2):
    sub = n1 - n2
    print(sub)

def Div(n1,n2):
    div = n1 / n2
    print(div)

def Multi(n1,n2):
    Multi = n1*n2
    print(Multi)

print("Calculadora")
linhas()

while True:

    n1= float(input("Digite o primeiro número que deseja realizar a operação:\n"))
    n2= float(input("Digite o segundo número que deseja realizar a operação:\n"))
    while True:
        print("Escolha uma das operações a seguir:")
        operacao = int(input("\n 1- Soma \n 2- Substração \n 3- Divisão \n 4- Multiplicação\n"))

        if operacao == 1:
            Soma(n1,n2)
            break
        elif operacao == 2:
            Sub(n1,n2)
            break
        elif operacao == 3:
            Div(n1,n2)
            break
        elif operacao == 4:
            Multi(n1,n2)
            break
        else:
            print("Digite uma opção válida.\n")
            continue

    while True:
        resposta = input("Deseja realizar mais operações?S/N\n").strip().upper()
        if resposta in 'SN':
            break
        else:
            input('Digite apenas S ou N\n')
    if resposta == 'N':
        break
    else:
        continue
        
