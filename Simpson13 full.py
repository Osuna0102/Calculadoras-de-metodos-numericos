import numpy as np
import matplotlib.pyplot as plt
import math


def simpson13(x0,xn,n):

    h = (xn - x0) / n
      
    integration = fx(x0) + fx(xn)
    
    for i in range(1,n):
        k = x0 + i*h
        
        if i%2 == 0:
            integration = integration + 2 * fx(k)
        else:
            integration = integration + 4 * fx(k)
    

    integration = integration * h/3
    
    return integration
    
print('===== Calculadora de Simpson 1/3 ====== ')
print(' ')

f = input("Enter the function :")
fx  = lambda x: eval(f)

lower_limit = float(input("Limite inferior:  "))
upper_limit = float(input("Limite Superior: "))
sub_interval = int(input("Numero de particiones: "))


result = simpson13(lower_limit, upper_limit, sub_interval)
print(' ')
print("EL RESULTADO ES: " , (result) )
