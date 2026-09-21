#Declarando un arreglo
numeros = [10, 20, 30, 40, 50]

#Imprimimos un elemento especifico del arreglo
print(numeros[2])

#Reasignación 
numeros[3] = 35
print(numeros)

#Agrega un nuevo valor al final del arreglo
numeros.append(60)
print(numeros)

#Eliminamos un valor en el arreglo
numeros.remove(35)
print(numeros)

#Eliminamos un valor del arreglo usando la posicion
numeros.pop(4)
print(numeros)

fruta = ["Manzana", "Fresa", "Sandia", "Mango", "Melon", "Platano"]
fruta.pop(4)
print(fruta)

#Eliminamos un elemento del arreglo usando el nombre
fruta.remove("Manzana")
print(fruta)

#Declaracion de un arreglo vacio
arreglo = []
print(arreglo)

n = int(input("Ingrese el tamaño del arreglo: "))
print(n)

for i in range(n):
    dato = int(input("Ingresa un numero: "))
    arreglo.append(dato)

print("El arreglo es: ", arreglo)

#Sin append
n = int(input("Ingrese el tamaño del arreglo: "))
arreglo = [0] * n

for i in range(n):
    dato = int(input("Ingresa un numero: "))
    arreglo[i] = dato

print(arreglo)
