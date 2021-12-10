
class Nodo():
	def __init__(self, nombre, valor) -> None:
		self.nombre = nombre
		self.valor = valor
		self.hijos = []

	def addHijos(self, *args):
		for hijo in args:
			self.hijos.append(hijo)

	def getBest(self):
		if self.hijos:
			self.hijos.sort( key=lambda v: v.valor )
			return self.hijos.pop(0)
		else:
			return None

	def __str__(self) -> str:
		return self.nombre

class Grafo:
	def __init__(self) -> None:
		self.nodos = {}

	def addNodos(self, *args):
		for n in args:
			self.nodos[n.nombre] = n

	def colinas(self, r, m):
		raiz = self.nodos.get(r)
		meta = self.nodos.get(m)
		if meta == None:
			return "No existe el nodo meta."
		elif raiz.nombre == meta.nombre:
			return meta.nombre

		colaNodos = []
		respuesta = []
		actualN = raiz

		while True:
			mejorHijo = actualN.getBest()
			print("Actual:", actualN,'-> Mejor hijo:', mejorHijo,'\n')

			if actualN.hijos and actualN not in colaNodos:
				colaNodos.append(actualN)
			elif not actualN.hijos and actualN in colaNodos:
				colaNodos.pop(0)

			if actualN not in respuesta:
				respuesta.append(actualN)

			actualN = mejorHijo

			if actualN.nombre == meta.nombre:
				respuesta.append(actualN)
				res = 'El mejor camino es: '
				for r in range(len(respuesta)-1):
					res = res + str(respuesta[r]) + ' -> '
				return res + str(respuesta[-1])
			
			# Vemos si es hoja
			elif not actualN.hijos:
				if colaNodos:
					actualN = colaNodos[0]
					respuesta = [raiz]
				else:
					return "No existe solución"



I = Nodo('I',100)
A = Nodo('A',27)
B = Nodo('B',10)
C = Nodo('C',30)
D = Nodo('D',22)
E = Nodo('E',10)
F = Nodo('F',12)
G = Nodo('G',15)
H = Nodo('H',11)
J = Nodo('J',20)
Z = Nodo('Z',0)

I.addHijos(A,B,C,D)
B.addHijos(E,F)
D.addHijos(F,J)
E.addHijos(G)
F.addHijos(H)
H.addHijos(Z)

X = Nodo('X',40)

g = Grafo()
g.addNodos(A,B,C,D,E,F,G,H,I,J,Z)

m = str(input('Nodo meta: '))
resp = g.colinas('I',m)
print(resp)

