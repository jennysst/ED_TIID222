
pila = []

estado = True

while estado == True:
    print("-------------------------------------")
    print("1. Insertar")
    print("2. Borrar en pila")
    print("3. Listar pila")
    print("4. Salir")
    print(" ")

    opcion = input("Elije una opcion: ")

    if opcion == "1":
        añadir = input("Ingresa el elemento: ")
        pila.append(añadir)
        print("Pila actual: ", pila)

    elif opcion == "2":
        ultimo = pila.pop()
        print("Atendido: ", ultimo)
        print("Pila actual: ", pila)

    elif opcion == "3":
        print("Pila actual: ", pila)

    elif opcion =="4":
        estado = False