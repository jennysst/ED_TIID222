

arreglo = []
resultado = []

n = int(input("Ingrese el tamaño del arreglo: "))
arreglo = [0] * n

for i in range(n):
    dato = int(input("Ingresa un numero: "))
    arreglo[i] = dato

print(arreglo)

for i in arreglo:
    while i%5 != 0:
        i = i+1
    resultado.append(i)
        
print("El arreglo cincuerizado es: ", resultado)
