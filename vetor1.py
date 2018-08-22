meuVetor = list(range(10))

for n in meuVetor:
    meuVetor[n] = int(input("Digite dez numero: "))

for n in range(0,10):
    if n % 2 == 0:
        print(meuVetor[n])

