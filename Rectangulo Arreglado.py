import numpy as np
import matplotlib.pyplot as plt



fx = input("Ingrese la funcion:\n")
f  = lambda x: eval(fx)

a  = float(input("Ingrese el limite menor:\n"))

b  = float(input("Ingrese el limite mayor:\n"))

N  = int(input("Ingrese las iteraciones:\n"))



n = 0

x = np.linspace(a,b,N+1)
y = f(x)

X = np.linspace(a,b,n*N+1)
Y = f(X)

plt.figure(figsize=(15,5))

plt.subplot(1,3,1)
plt.plot(X,Y,'b')
x_left = x[:-1] 
y_left = y[:-1]
plt.plot(x_left,y_left,'b.',markersize=10)
plt.bar(x_left,y_left,width=(b-a)/N,alpha=0.2,align='edge',edgecolor='b')
plt.title('Por la izquierda, N = {}'.format(N))

plt.subplot(1,3,2)
plt.plot(X,Y,'b')
x_mid = (x[:-1] + x[1:])/2 
y_mid = f(x_mid)
plt.plot(x_mid,y_mid,'b.',markersize=10)
plt.bar(x_mid,y_mid,width=(b-a)/N,alpha=0.2,edgecolor='b')
plt.title('Por el medio, N = {}'.format(N))

plt.subplot(1,3,3)
plt.plot(X,Y,'b')
x_right = x[1:] 
y_right = y[1:]
plt.plot(x_right,y_right,'b.',markersize=10)
plt.bar(x_right,y_right,width=-(b-a)/N,alpha=0.2,align='edge',edgecolor='b')
plt.title('Por la derecha, N = {}'.format(N))

plt.show()

dx = (b-a)/N
x_left = np.linspace(a,b-dx,N)
x_midpoint = np.linspace(dx/2,b - dx/2,N)
x_right = np.linspace(dx,b,N)

print("Calculadora de integracion por rectangulos")
print(" ")

print(" ")


print("Particion con ",N,"subintervalos.")
left_riemann_sum = np.sum(f(x_left) * dx)
print("Por la izquierda",left_riemann_sum)

midpoint_riemann_sum = np.sum(f(x_midpoint) * dx)
print("Por el medio:",midpoint_riemann_sum)

right_riemann_sum = np.sum(f(x_right) * dx)
print("Por la derecha",right_riemann_sum)
