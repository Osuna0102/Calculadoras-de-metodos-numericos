import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x**2-4*x

n=400
suma = 0
a = 0
b = 4
Dx = (b-a)/n

for i in range(n):
    altura = f(a+Dx/2)
    Area = Dx * altura
    suma = suma + Area
    a = a + Dx

print(suma)
print(abs(suma))
