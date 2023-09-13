meta = float(input("Qual a meta da vaquinha?"))
arrecadacao = 0

while (arrecadacao < meta):
    doacao = float(input("Qual o valor da doação"))
    if (doacao<=0):
        print("Doação inválida, informe um valor superior a 0")
        continue
    arrecadacao += doacao
print("Meta atingida. O valor arrecadado foi: %.2f" % arrecadacao)

