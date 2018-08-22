quantidadeA = 0
quantidadeB = 0
quantidadeC = 0
quantidadeD = 0
numero = 0

while numero >= 0: 
      numero = float(input("Digite um número positivo: "))            

      if numero >= 0:
        if numero < 26:
            quantidadeA += 1
        else:
            if numero < 51:
               quantidadeB += 1
            else:    
                if numero < 76:
                   quantidadeC += 1
                else:
                    if numero <= 100:
                       quantidadeD += 1

print ("Quantidade de numero entre [0,25] é: ", quantidadeA)
print ("Quantidade de numero entre [26,50] é: ", quantidadeB)
print ("Quantidade de numero entre [51,75] é: ", quantidadeC)
print ("Quantidade de numero entre [76,100] é: ", quantidadeD)