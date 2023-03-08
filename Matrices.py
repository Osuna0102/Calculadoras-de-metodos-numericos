import numpy as np
from numpy.linalg import det, inv, matrix_power




xd=np.array([[float(z) for z in x.split()] for x in input("Ingrese las filas separados por ; y las columnas por espacios: ").split(";")])

print(xd)


