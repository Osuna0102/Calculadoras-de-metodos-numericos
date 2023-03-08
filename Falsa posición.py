import sympy as sp

print("Método de falsa posición\n")
x,y = sp.symbols('x y')
str_ecuacion = input("Ingrese la ecuación:\n")
funcion = sp.sympify(str_ecuacion)
sp.plot(funcion, (x, -10, 10), title = 'Ten en cuenta la(s) raíz(es)', aspect_ratio = 'auto')
a = float(input("Dijite el extremo inferior del intervalo: "))
b = float(input("Dijite el extremo superior del intervalo: "))
tolerancia = float(input("Dijite el error de tolerancia: "))
error = 10

def f(x):
	b = funcion.free_symbols
	var = b.pop()
	valor = funcion.evalf(subs = {var:x})
	return valor

if (f(a) * f(b) <0):

	contador = 1

	print("")
	print ("{0}\t{1}\t{2}\t{3}".format('#', 'f(a)', 'f(b)', 'raiz'))

	while error > tolerancia and contador < 200:

		fa = f(a)
		fb = f(b)
		m = ((a * fb) - (b * fa)) / (fb - fa)
		fm = f(m)

		print (contador, "\t{:.4}\t{:.4}\t{:.10}".format(f(a), f(b), m))

		if fm == 0:
			raiz = m
			break

		elif fa * fm < 0:
			b = m
		else:
			a = m
		raiz = m
		error = abs(fm)

		contador = contador + 1

	print("\nLa raíz es: ", raiz)
	print("El error relativo es: ", error)

else:
	print("\nLos intervalos no contienen la raíz")