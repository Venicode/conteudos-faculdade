nome_completo = input("Digite o seu nome completo: ")
curso = input("Informe o seu curso: ")
semestre = input("Informe o seu semestre atual: ")
cpf = int(input("Digite o seu CPF: "))
bolsa = False
valor_mensal = float(input("Qual o valor da mensalidade?: "))

if valor_mensal != 0:
   bolsa = 'Não'
else:
   bolsa = True
   bolsa = 'Sim'

print("Nome completo: {} Curso: {} Semestre: {} CPF: {} Bolsa:  {} Mensalidade: {}".format(nome_completo,curso,semestre,
                                                                                         cpf,bolsa,valor_mensal))