#script basico de definicion de clases y su uso
import timeit

class Persona(object):
	""" Definicion de una clase persona""" # Docstring
	def __init__(self, altura, peso, edad):
		""" Inicializacion de un objeto persona"""
		self.altura = altura # OJO TODAS LAS VARIABLES SON PUBLICAS 
		self.peso = peso 
		self.edad = edad
		self.profesion = "" # esta la inicializamos nosotros
		self.lista_tareas = []
		self.__privado = 1 # este atributo es privado no podemos acceder a el desde fuera
	
	def suma_tarea (self, tarea): # incluimos una nueva tarea
		self.lista_tareas.append(tarea)
		self._metodo_privado(tarea)

	def elimino_tarea(self, tarea): # eliminamos una nueva tarea
		self.lista_tareas.remove(tarea)

	def _metodo_privado(self, item): # para indicar que el metodo es privado
		print "incluyo item %s" %item	

# generamos un nuevo objeto y lo inicializamos con ciertos valores 

Daniel = Persona(1.78, 74, 31)
print "Altura %f" % Daniel.altura
print "Altura %.2f" % Daniel.altura # variante para imprimir solo dos digitos

#profesion

Daniel.profesion = "Ingeniero"

print "Profesion %s" % Daniel.profesion

#tareas

lista_tareas = ["compra semana", "paper", "preparar practicas"]

for tar in lista_tareas:
	Daniel.suma_tarea(tar)

print "Tareas pendientes %s" % Daniel.lista_tareas

# imprimimos el docstring

print Daniel.__doc__

#print Daniel.privado
#Daniel.metodo_privado("holaa")

