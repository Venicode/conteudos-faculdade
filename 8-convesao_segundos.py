h = int(input("\nDigite a hora: "))
min = int(input("\nDigite os minutos: "))
seg = int(input("\nDigite os segundos: "))

conv_h = h * 3600
conv_min = min * 60
conv_total = conv_h + conv_min + seg

print("O horário em segundos é: ",conv_total)
