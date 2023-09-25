#Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

while True:
    nome  = str(input("Informe o nome:"))
    if len(nome)<3:
        print("Nome inválido.")
        continue
    
    while True:
        idade = int(input("Informe a idade:"))
        if idade<0 or idade>150:
            print("Digite uma idade válida!")
            continue
        else:
            break
        
    while True:
        salario = float(input("Informe o salário:"))
        if salario<=0:
            print("Digite um salário maior que 0")
            continue
        else:
            break
        
    while True:
        sexo = input("Informe o sexo (F ou M):").strip().upper()
        if sexo in 'FM':
            break
        else:
            print("Digite F ou M para denominar o sexo.")
            continue
        
    while True:
        estadoCivil = input("Informe o estado civil (S,C,V,D):").strip().upper()
        if estadoCivil in 'SCVD':
            break
        else:
            print("Digite um estado civil válido conforme as orientações.")
            continue
        
    print(f"\n Dados cadastrados.\n Segue as informações: \n Nome: {nome} \n Idade: {idade} \n Salário: {salario} \n Sexo: {sexo} \n Estado Civil: {estadoCivil}")
    break
