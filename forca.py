from random import choice

print("Jogo da Forca")
arquivo = "palavras.txt"
palavras = []

with open (arquivo) as arquivo:
    for linha in arquivo:
        palavras.append(linha.strip())
        
palavrasecreta = choice(palavras).upper()
letrasC = ""
letrasE = ""

while True:
    pista = ""
    for letra in palavrasecreta:
        if letra in letrasC:
            pista += letra
        else:
            pista += "_ "
    print(pista)
    if "_" not in pista:
        print("Voce ganhou")
        break
    if len(letrasE)==6:
        print("Game over")
        print("Tentativas erradas:",len(letrasE))
        break
    letra = input("Digite uma letra: ").upper()
    if len(letra) !=1 or not letra.isalpha():
        print("Digite apenas 1 letra.")
        continue
    
    if letra in letrasC or letra in letrasE:
        print("Letra já digitada")
        continue
    
    if letra in palavrasecreta:
        letrasC+=letra
    else:
        letrasE+=letra
