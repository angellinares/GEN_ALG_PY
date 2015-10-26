# definimos la funcion suma
def suma (a, b):
	resultado = a + b
	return resultado

def product(a,b):


	if (type(a) != int) or (type(b) != int):
		 result =  "Input values should be an integer"
	else:
		result = a*b

	return result

# sumamos dos numeros
num1 = 10
num2 = 15

res = suma(num1, num2)
res2 = product(num1,num2)
print res
print res2

# sumamos dos cadenas

cadena1 = "hola"
cadena2 = " mundo!"

res = suma(cadena1, cadena2)
res2 = product(cadena1,cadena2)
print res2
print res

# sumamos dos listas

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

res = suma(lista1, lista2)
print res
res2 = product(lista1,lista2)
print res2



# Sumamos dos tuples

tuple1 = (1,2,3)
tuple2 = (4,5,6)

res = suma(tuple1,tuple2)
print res
# ejercicio propuesto1: realizar una funcion que multiple dos numeros
# ejercicio propuesto 2: realizar una funcion que reciba una cadena y devulva la longitud de la cadena

