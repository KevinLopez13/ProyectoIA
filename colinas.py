
class Nodo():
	def __init__(self, nombre, valor) -> None:
		self.nombre = nombre
		self.valor = valor
		self.hijos = []

	def addHijo(self, h):
		h.padre = self.nombre
		self.hijo.append(h)

	def addHijos(self,**kwards):
		for hijo in kwards.items():
			self.hijos.append(hijo)

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

class Grafo:
	def __init__(self) -> None:
		self.nodos = {}

	def addNodo(self, n):
		self.nodos[n.nombre] = n

	def solucion(self, nodo, nodolst):
		padre = nodo.getPadre()
		nodoNext = nodo
		tmplst = []
		while padre != None:
			tmplst.append(padre)

			padre = padre.getPadre()

	def colinas(self,raiz, meta):
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
			#if actualN not in respuesta:
			respuesta.append(actualN)
			actualN = actualN.getMin()
				
			# Ya es nuestra solucion?
			if actualN.nombre == meta.nombre:
				respuesta.append(actualN)
				for n in respuesta:
					print(n)
				return True

			# si llegamos a una hoja
			elif not actualN.hijos:
				respuesta.pop()
			else:
				pass

			if not colaNodos:
				print('!Meta')
				return False

	def colinas2(self, raiz, meta):
		colaNodos = []
		respuesta = []
		actualN = raiz

		while True:
			mejorHijo = actualN.getMin()
			print("Actual:", actualN,'-> Mejor hijo:', mejorHijo,'\n')

			if actualN.hijos and actualN not in colaNodos:
				colaNodos.append(actualN)
			elif not actualN.hijos and actualN in colaNodos:
				colaNodos.pop(0)

			if mejorHijo != None:
				if actualN not in respuesta:
					respuesta.append(actualN)
				#respuesta.append(mejorHijo)
				actualN = mejorHijo

				# Vemos si es hoja
				if not actualN.hijos:
					if actualN.nombre == meta.nombre:
						respuesta.append(actualN)
						for n in respuesta:
							print(n)
						return True
					else:
						actualN = colaNodos[0]
						respuesta = [raiz]
			else:
				print("None:")
				actualN = colaNodos[0]
				respuesta = [raiz]





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

I.hijos.append(A)
I.hijos.append(B)
I.hijos.append(C)
I.hijos.append(D)

#A.hijos.append(B)

#B.addHijos(A,C,E,F)
#B.hijos.append(A)
#B.hijos.append(C)
B.hijos.append(E)
B.hijos.append(F)

#C.hijos.append(B)

D.hijos.append(F)
D.hijos.append(J)

E.hijos.append(G)

F.hijos.append(H)

H.hijos.append(Z)

g = Grafo()

g.addNodo(A)
g.addNodo(B)
g.addNodo(C)
g.addNodo(D)
g.addNodo(E)
g.addNodo(F)
g.addNodo(G)
g.addNodo(H)
g.addNodo(I)
g.addNodo(J)
g.addNodo(Z)

print(g.colinas2(I,C))



			




	

