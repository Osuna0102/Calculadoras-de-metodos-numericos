import sympy as sp

print("Método de la secante\n")
x,y = sp.symbols('x y')
str_ecuacion = input("Ingrese la ecuación:\n")
funcion = sp.sympify(str_ecuacion)
sp.plot(funcion, (x, -10, 10), title = 'Ten en cuenta la(s) raíz(es)', aspect_ratio = 'auto')
a = float(input("Dijite el extremo inferior del intervalo: "))
b = float(input("Dijite el extremo superior del intervalo: "))
tolerancia = float(input("Dijite el error de tolerancia: "))

def f(x):
	b = funcion.free_symbols
	var = b.pop()
	valor = funcion.evalf(subs = {var:x})
	return valor

c = 0
iteraciones = 0

print("")
print ("{0}\t{1}".format('#', 'raíz'))

while(abs(f(c)) > tolerancia and iteraciones < 200):
	c = b - ((b-a) / (f(b)-f(a))) * f(b)
	a = b
	b = c
	print (iteraciones, "\t{:.20}".format(c))
	iteraciones = iteraciones + 1

if(iteraciones == 200):
	print("\nSe ha alcanzado el numero máximo de iteraciones")
	print("Es posible que no hayan raices en el intervalo")
	print("Intenta con otro intervalo")
else:
	print("\nLa raíz es: ",c)
	print("El error relativo es: ", abs(f(c)))