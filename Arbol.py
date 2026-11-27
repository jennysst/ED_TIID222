
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None


raiz = Nodo(1)

raiz.izquierdo = Nodo(2)
raiz.derecho = Nodo(3)

raiz.izquierdo.izquierdo = Nodo(4)
raiz.izquierdo.derecho = Nodo(5)

raiz.derecho.derecho = Nodo(6)
raiz.izquierdo.izquierdo.izquierdo = Nodo(7)
raiz.izquierdo.izquierdo.derecho = Nodo(8)
raiz.izquierdo.derecho.derecho = Nodo(9)
raiz.derecho.derecho.derecho = Nodo(10)
raiz.derecho.derecho.derecho.izquierdo = Nodo(11)
raiz.derecho.derecho.derecho.derecho = Nodo(12)



def imprimir_arbol(nodo, nivel = 0, prefijo = "Raiz: "):
    if nodo is not None:
        print("   "* nivel + prefijo + str(nodo.valor))
        imprimir_arbol(nodo.izquierdo, nivel + 1, "Izquierdo: ")
        imprimir_arbol(nodo.derecho, nivel + 1, "Derecho: ")

imprimir_arbol(raiz)