

arreglo = []
resultado = []

for i in range(5):
    dato = int(input("Ingresa un numero: "))
    arreglo.append(dato)

print("El arreglo es: ", arreglo)

for i in range(5):
    if arreglo[i]%5 == 0:
        resultado.append(arreglo[i])
    else:
        resultado.append(0)
        
print("El arreglo cincuerizado es: ", arreglo)
