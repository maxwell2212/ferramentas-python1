def trianguloEquilatero(ladoA,ladoB,ladoC):
   if (ladoA) == (ladoB) and (ladoB) == (ladoC):
         return 1
   return 0

def triaguloIsoceles(ladoA,ladoB,ladoC):
   if (ladoA) == (ladoB) and (ladoA) != (ladoC) or (ladoB) == (ladoC) and (ladoB) != (ladoA) or (ladoA) == (ladoC) and (ladoC) != (ladoB): 
         return 1
   return 0

def triaguloEscaleno(ladoA,ladoB,ladoC):
      if (ladoA) != (ladoB) != (ladoC):
            return 1  
      return 0


ladoA = float(input("Digite o valor de lado A:"))
#return ladoA
ladoB = float(input("Digite o valor de lado B:"))
#return ladoB
ladoC = float(input("Digite o valor de lado C:"))
#return ladoC

if trianguloEquilatero(ladoA,ladoB,ladoC) == 1:
      print("É um triagulo equilatero!")

if triaguloEscaleno(ladoA,ladoB,ladoC) == 1:
      print("É um triangulo escaleno!")
      
if triaguloIsoceles(ladoA,ladoB,ladoC) == 1:
      print("É um triangulo Isoceles!")


          

   
   
   
   
   
    


  


       


      










