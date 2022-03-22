producto =[]
precio =[]
codigo =[]
opcion= int(input("Supermecardo la joya: \n 1. Digita 1 para agregar {producto, precio, codigo} \n 2. Digita 2 para validar tus productos registrados \n 3. Digita 3 para buscar tu producto con el código y editar el precio \n 4. Digita 4 para buscar tu producto con el código y eliminarlo \n 0. Digita 0 para salir \n"))

while opcion !=0:
    if opcion == 1:
        (print("Agregar el producto"))
        producto.append(input("Digite el nombre del producto: "))
        precio.append(int(input("Digite precio: ")))
        codigo.append(input("Digite código: "))
    elif opcion == 2:
        print("Mostar productos registrados")
        for x in range(len(producto)):
            print(producto[x], precio[x], codigo[x])
    elif opcion == 3:
        print("Buscar producto con código y edita el precio")
        manipular = input ("Ingrese el código del producto que deseas modificar: ")  
        for x in range(len(codigo)):
            if codigo[x] == manipular:
                producto[x] = input("¿Cuál es el nuevo nombre? ")
                precio[x] = int(input("¿Cuál es el nuevo precio? "))
        print("Producto modificado")        

    elif opcion == 4:
        print("buscar producto y eliminarlo") 
        manipular = input ("Ingrese el código del producto que deseas eliminar: ")   
        for i in range(len(codigo)-1,-1,-1):
            if codigo[i] == manipular:
               codigo.pop(i)
               producto.pop(i)
               precio.pop(i)
        print("Producto eliminado")    
    else:
        print("Por favor digita una opción correcta")           
    opcion= int(input("Supermecardo la joya: \n 1. Digita 1 para agregar {producto, precio, codigo} \n 2. Digita 2 para validar tus productos registrados \n 3. Digita 3 para buscar tu producto con el código y editar el precio \n 4. Digita 4 para buscar tu producto con el código y eliminarlo \n 0. Digita 0 para salir \n"))   