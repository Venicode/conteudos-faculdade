# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B 
# seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que 
# a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

popPaisA = 80000
taxaCrescimentoA = 0.03
popPaisB = 200000
taxaCrescimentoB = 0.015
ano = 1
while(popPaisA<popPaisB):
    
    crescimentoAnualA = (popPaisA * taxaCrescimentoA)
    popPaisA = popPaisA + crescimentoAnualA
    
    crescimentoAnualB = (popPaisB * taxaCrescimentoB)
    popPaisB = popPaisB+ crescimentoAnualB
    ano +=1
    
    if(popPaisA>=popPaisB):
        print("A população de A atingiu a população de B. Os anos necessários foram:",ano,)
        break