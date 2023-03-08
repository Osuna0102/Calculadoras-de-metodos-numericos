import tkinter as tki
import sympy as sp

print("Método de Newton Rhapson\n")
x,y = sp.symbols('x y')

#Variable que recibe la funcion
str_ecuacion = input("Ingrese la ecuación:\n")
funcion = sp.sympify(str_ecuacion)
sp.plot(funcion, (x, -10, 10), title = 'Ten en cuenta la(s) raíz(es)', aspect_ratio = 'auto')

#Variable que recibe el punto inicial
x0 = float(input("Dijite el punto de inicio:\n"))

#Variable que recibe el error de tolerancia
tolerancia = float(input("Dijite el error de tolerancia:\n"))


def f(x):
	b = funcion.free_symbols
	var = b.pop()
	valor = funcion.evalf(subs = {var:x})
	return valor

#Funcion calcular derivada numerica
def Df(x):
	b = funcion.free_symbols
	var = b.pop()
	df = sp.diff(funcion,var)
	valor = df.evalf(subs = {var:x})
	return valor

contador = 1

print("")
print ("{0}\t{1}".format('#', 'raíz'))

while (abs(f(x0)) > tolerancia and contador < 200):

	x1 = x0 - f(x0) / Df(x0)
	x0 = x1

	print (contador,"	", x0)
	contador = contador + 1

if(contador == 200):
	print("\nSe ha alcanzado el numero máximo de iteraciones")
	print("Es posible que no hayan raices")
	print("Intenta con otro punto inicial")
else:
	print("\nLa raíz es: ", x0)
	print("El error relativo es: ",abs(f(x0)))
    

