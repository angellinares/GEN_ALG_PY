# floatVar1 = 5.5
# intVar2 = 4
# lstVar3 = [1,2,3]

# print "variable1: %f" % floatVar1
# print "variable2: %d" %	intVar2 
# print "variable3: %s" % lstVar3

# print "///////////////////////////////////////////////////////////////////////"

# strCadena = "Hola mundo"

# print "Longitud de cadena: %d" %len(strCadena)
# print "Longitud de lista: %d"	%len(lstVar3)

# print "Trozo de lista: %s"	%lstVar3[1:]

# print "Trozos de cadena: %s" %strCadena.split(" ")
# print "'Oes' en la cadena: %s" %strCadena.find("o")

lstLetras = ["a","b","c","d","e"]
intCounter = 0

for i in range(0,len(lstLetras),2):

	#if i%2 == 0:

	lstLetras[i] = "impar"

	intCounter+=1

	print "Miembro de lstLetras -> " + str(intCounter) + " = " + lstLetras[i]

print lstLetras


