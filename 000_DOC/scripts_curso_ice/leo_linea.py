import timeit

fichero = open("texto.txt", 'r')

lineas = fichero.readlines() # leo el fichero de golpe

print lineas

for i, k in enumerate(lineas):
	if i == 2:
		lin = k.split(',')
		print "primer valor %d" % int(lin[0]) # si no lo convierto en entero me da error porque lo considera una cadena
		print "segundo valor %d" % int(lin[1])
		print "tercer valor %d" % int(lin[2])

# ejercicio, obtener el penultimo valor de la 4 fila
		
for i, k in enumerate(lineas):

	if i==3:
		lin = k.split(",")
		print "Penultimo valor de la fila 4: %d" %int(lin[3])


timeit.timeit()