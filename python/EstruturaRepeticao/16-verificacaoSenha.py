#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
# mostrando uma mensagem de erro e voltando a pedir as informações.
usuario = 0
senha = 0
usuario = input("Digite o nome do seu usuário:")
senha = str(input("Digite a sua senha:"))

while(usuario == senha):
    
    print("A sua senha não pode ser igual ao nome de usuário!")
    senha = str(input("Digite uma senha válida: "))
    
print("Usuário e senha cadastrados com sucesso!")
