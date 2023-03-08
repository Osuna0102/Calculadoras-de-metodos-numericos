import numpy as np
import numpy.linalg 


A = np.array([[1,  1,  1,  0,  0,  0],
              [0, -1,  0,  1, -1,  0],
              [0,  0, -1,  0,  0,  1],
              [0,  0,  0,  0,  1, -1],
              [0, 10,-10,  0,-15, -5],
              [5,-10,  0,-20,  0,  0]])
#1 1 1 0 0 0 ; 0 -1 0 1 -1 0 ; 0 0 -1 0 0 1 ; 0 0 0 0 1 -1 ; 0 10 -10 0 -15 -5 ; 5 -10 0 -20 0 0


B = np.array([[0],
              [0],
              [0],
              [0],
              [0],
              [200]])
#0 0 0 0 0 200

a=np.array([[float(z) for z in x.split()] for x in input("Ingrese las filas separados por ; y las columnas por espacios: ").split(";")])

b = input("Ingrese los valores del array x: ").split(' ')
b = [float(y) for y in b]
print('solución de X: ')


print(np.linalg.solve(A,B))
print(np.linalg.solve(a,b))
