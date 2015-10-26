#funciones lambda

y= lambda x: x+2 # asignamos la funcion a una variable

z = y(5)

print z

h = y(9)

print h

# ejercicio propuesto, crear una funcion lambda que calcule el cuadrado de un numero

f = lambda x: x*x

result = f(2.5)
print result

# podemos hacer funciones lambda con dos variables
y = lambda x, y: x + y

t = y(5,4)

print t
