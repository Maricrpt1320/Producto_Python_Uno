contador=0
numeros=int(input("Introduzca el extremo superior: "))  
print("Múltiplos de 2 y de 3 entre 1 y %i:"%numeros)  
for i in range(1,numeros+1):  
 if i%2==0 and i%3==0:  
  contador+=1  
  print(i)  
print("Existen %i múltiplos de 2 y 3 en ese rango, incluidos los extremos"%contador)  