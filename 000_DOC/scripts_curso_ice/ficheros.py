# Leemos el fichero linea a linea

fichero = open("song.txt", 'r')

for line in fichero:
	print line

# Vamos a complicar un poco mas el asunto
# comentar primero el for de arriba

for line in fichero:
	palabras = line.split(" ") # separamos las lineas en palabras
	for palabra in palabras:
		print palabra # imprimimos palabra a palabra


