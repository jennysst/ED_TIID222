
from collections import deque

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

raizValor = input("Introduce el valor de la raiz: ")

raiz = Nodo(raizValor)

cola = deque()

nodoActual = raiz
estado = True

while estado == True:
    print("Nodo actual:", nodoActual.valor)
    print("1. Hijo a la izquierda")
    print("2. Hijo a la derecha")
    print("3. Siguiente nodo")
    print("4. Salir")

    opcion = input("Elije una opción: ")

    if opcion == "1":
        if nodoActual.izquierdo == None:
            valorNodo = input("Valor: ")
            nodoActual.izquierdo = Nodo(valorNodo)
            cola.append(nodoActual.izquierdo)
        else:
            print("Ya hay un nodo")

    elif opcion == "2":
        if nodoActual.derecho == None:
            valorNodo = input("Valor: ")
            nodoActual.derecho = Nodo(valorNodo)
            cola.append(nodoActual.derecho)
        else:
            print("Ya hay un nodo")

    elif opcion == "3":
        if len(cola) > 0:
            nodoActual = cola.popleft()
        else:
            print("No hay nodos")

    elif opcion =="4":
        estado = False


def imprimir_arbol(nodo, nivel = 0, prefijo = "Raiz: "):
    if nodo is not None:
        print("   "* nivel + prefijo + str(nodo.valor))
        imprimir_arbol(nodo.izquierdo, nivel + 1, "Izquierdo: ")
        imprimir_arbol(nodo.derecho, nivel + 1, "Derecho: ")

imprimir_arbol(raiz)