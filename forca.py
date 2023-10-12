print("Jogo da Forca")
palavrasecreta = "Internet".upper()
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
    letra = input("Digite uma letra: ").upper()
    if len(letra) !=1 or not letra.isalpha():
        print("Digite apenas 1 letra.")
        continue
    
    if letra in letrasC or letra in letrasE:
        print("Letra já digitada")
        continue
    
    if letra in palavrasecreta:
        letrasC+=letra
