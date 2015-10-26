lista = [1, 30, 40, 5, 4]

# obtener el maximo de una lista
maximo = max(lista)
print "El maximo es: %d" % maximo

# obtener el minimo de una lista
minimo = min(lista)
print "El minimo es: %d" % minimo

# ordenar la lista
ordenada = sorted(lista)
print "lista ordenada %s" % ordenada
print "lista original %s" % lista # no se ha modificado la lista original

# crea una lista de tuplas compuesta a partir de otras listas
x = [1, 2, 3]
y = [4, 5, 6]
zipped = zip(x, y)
print zipped

# utilizada de zip, bucles mas sofisticados

for i, j in zipped:
	print i + j

# funcion map, aplicar una funcion a todos los elementos de un iterable

def cuadrado (a): # elevamos al cuadrado un nuevo
	return a ** 2

lista = [1, 2, 3, 4] #lista a la que vamos a aplicar la funcion

lista_2 = map(cuadrado, lista)
print lista_2

# funcion enumerate, devuelve una lista de tuplas, donde el primer elemento es la cuenta y el segundo el elemento de la lista original
for i, k in enumerate(lista):
	lista[i] = 0
print lista

# ejercicio propuesto, crear una lista de tuplas que representen las coordenadas x,y 

