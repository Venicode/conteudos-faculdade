#importa a biblioteca random com a função choice
from random import choice

print("Jogo da Forca")
arquivo = "palavras.txt"
palavras = []

#abre o arquivo palavras.txt e lê cada linha.
with open (arquivo) as arquivo:
    for linha in arquivo:
        palavras.append(linha.strip())

#com a função choice, escolhe aleatoriamente uma palavra dentro do arquivo para ser a palavrasecreta
palavrasecreta = choice(palavras).upper()
letrasC = ""
letrasE = ""

while True:
    pista = ""
    #percorre cada letra da palavra secreta e verifica se a letra que o usuário digitou contém nela
    for letra in palavrasecreta:
        if letra in letrasC:
            pista += letra
        #caso não contenha, aparece o _ no lugar da letra
        else:
            pista += "_ "
    print(pista)
    #quando não tiver mais nenhum _ , quer dizer que o usuário acertou a palavra
    if "_" not in pista:
        print("Voce ganhou")
        break
    #caso o usuário erre 6 vezes as letras da palavra secreta, ele perde o jogo
    if len(letrasE)==6:
        print("Game over")
        print("Tentativas erradas:",len(letrasE))
        break
    letra = input("Digite uma letra: ").upper()
    #verifica se a letra digitada é apenas 1 e que não é um número
    if len(letra) !=1 or not letra.isalpha():
        print("Digite apenas 1 letra.")
        continue
    #se a letra já tiver sido armazenada na variavel letrasC ou letrasE, quer dizer que já foi digitada.
    if letra in letrasC or letra in letrasE:
        print("Letra já digitada")
        continue
    #se a letra tiver na palavra secreta, acrescenta na variavel letrasC
    if letra in palavrasecreta:
        letrasC+=letra
    #se não, acrescenta na variável letrasE
    else:
        letrasE+=letra
