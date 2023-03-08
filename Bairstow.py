import sympy as sp
import cmath
import random

def bairstow(a, r, s, g, roots):
	if (g < 1):
		return None

	if ((g == 1) and (a[1] != 0)):
		roots.append(float (-a[0])/float(a[1]))
		return None

	if (g == 2):
		D = (a[1]**2.0) - (4.0)*(a[2])*(a[0])
		X1 = (-a[1] - cmath.sqrt(D)) / (2.0 * a[2])
		X2 = (-a[1] + cmath.sqrt(D)) / (2.0 * a[2])
		roots.append(X1)
		roots.append(X2)
		return None

	n = len(a)
	b = [0] * len(a)
	c = [0] * len(a)
	b[n-1] = a[n-1]
	b[n-2] = a[n-2] + r * b[n-1]
	i = n - 3

	while (i >= 0):
		b[i] = a[i] + r*b[i+1] + s*b[i+2]
		i = i - 1

	c[n-1] = b[n-1]
	c[n-2] = b[n-2] + r*c[n-1]
	i = n -3

	while (i >= 0):
		c[i] = b[i] + r*c[i+1] + s*c[i+2]
		i = i-1

	Din = ((c[2]*c[2])-(c[3]*c[1])) ** (-1.0)
	r = r + (Din)*((c[2])*(-b[1])+(-c[3])*(-b[0]))
	s = s + (Din)*((-c[1])*(-b[1])+(c[2])*(-b[0]))

	if (abs(b[0]) > 1e-14 or abs(b[1]) > 1e-14):
		return bairstow(a, r, s, g, roots)

	if (g >= 3):
		Dis = ((-r)**(2.0)) - ((4.0)*(1.0)*(-s))
		X1 = (r - (cmath.sqrt(Dis))) / (2.0)
		X2 = (r + (cmath.sqrt(Dis))) / (2.0)
		roots.append(X1)
		roots.append(X2)
		return bairstow(b[2:], r, s, g-2, roots)

print("Método de Bairstow\n")

x,y = sp.symbols('x y')
g = int(input("¿Cuál es el grado del polinomio?: "))
print("Dijita los coeficientes en orden ascendente:\n")

a = []

for i in  range(g+1):
	coeficiente=float(input("=> "))
	a.append(coeficiente)

k = 1

print("Ecuación descrita:\n")

ecuacion = str(a[0])

for i in range(g):

	ecuacion += str(" + ")+str(a[k])+"*x**"+str(k)
	k += 1

print(ecuacion)

funcion = sp.sympify(ecuacion)

j = 1
roots = []
r = random.random()
s = random.random()

bairstow(a, r, s, g, roots)

print("\nRaices encontradas:\n")

for r in roots:
	print ("Raíz " , j, " = ", r)
	j += 1

sp.plot(funcion,(x, -3, 3), title="Gráfica de "+str(ecuacion), aspect_ratio='auto')