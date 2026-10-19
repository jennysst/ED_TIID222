
from collections import deque

cola = deque()

estado = True

while estado == True:
    print("-------------------------------------")
    print("1. Insertar Cola")
    print("2. Borrar en cola")
    print("3. Listar cola")
    print("4. Salir")
    print(" ")

    opcion = input("Elije una opcion: ")

    if opcion == "1":
        encolar = input("Ingresa un numero: ")
        cola.append(encolar)
        print("Cola actual: ", cola)

    elif opcion == "2":
        primero = cola.popleft()
        print("Atendido: ", primero)
        print("Cola actual: ", cola)

    elif opcion == "3":
        print("Cola actual: ", cola)

    elif opcion =="4":
        estado = False