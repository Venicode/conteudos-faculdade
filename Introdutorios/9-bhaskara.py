import math
print("\nPrograma de Bháskara")
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = b * 2 - (4 * a * c)

if delta<0:
   print("Delta negativo")
   
else:
    x1 = (-b + math.sqrt(delta)) /( 2 * a)
    x2 = (-b - math.sqrt(delta)) /( 2 * a)

    print("O delta é: {} e o resultado do X1 é: {} e o x2 é: {}".format(delta,x1,x2))