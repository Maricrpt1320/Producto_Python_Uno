cantidad = int(input('Digite cantidad de frutas que desea agregar al salpicon: '))
frutas = []

i = 0

while i <= cantidad:
    fruta= input('Digite las frutas que deseas: ')
    frutas.append(fruta)
    i+=1

for f in reversed(frutas): 
    print(f)    



