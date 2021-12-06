
class Nodo():
    def __init__(self, nombre, valor) -> None:
        self.nombre = nombre
        self.valor = valor
        self.hijos = []

    def getMin(self):
        if self.hijos:
            self.hijos.sort( key=lambda v: v.valor )
            return self.hijos.pop(0)
        else:
            return None

    def __str__(self) -> str:
        return self.nombre

    def printH(self):
        print("Padre:",self.nombre)
        for i in self.hijos:
            print(i)



def colinas(raiz, meta):
    colaNodos = []
    respuesta = []
    actualN = raiz
    
    
    while True:
        # Guardamos las otras opciones posibles
        if actualN.hijos:
            if actualN not in colaNodos:
                colaNodos.append(actualN)
        else:
            if colaNodos[0].hijos:
                actualN = colaNodos[0]
                respuesta.pop()
            else:
                colaNodos.pop(0)
                actualN = colaNodos[0]

        # Obtenemos el hijo con mejor valor y actualizamos
        respuesta.append(actualN)
        actualN = actualN.getMin()
            
        # Ya es nuestra solucion?
        if actualN.nombre == meta.nombre:
            respuesta.append(actualN)
            for n in respuesta:
                print(n)
            return True
        elif not actualN.hijos:
            respuesta.pop()
        else:
            pass

        if not colaNodos:
            print('!Meta')
            return False
    



nodoS = Nodo('S',1000)
nodoA = Nodo('A',1)
nodoB = Nodo('B',2)
nodoD = Nodo('D',1)
nodoF = Nodo('F',3)

nodoA.hijos.append(Nodo('C',2))
nodoA.hijos.append(nodoD)

nodoB.hijos.append(Nodo('E',2))
nodoB.hijos.append(nodoF)

nodoF.hijos.append(Nodo('G',2))
nodoF.hijos.append(Nodo('H',3))
nodoF.hijos.append(Nodo('I',1))

nodoS.hijos.append(nodoA)
nodoS.hijos.append(nodoB)

colinas(nodoS,Nodo('I',1))



            




    

