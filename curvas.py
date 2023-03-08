import matplotlib.pyplot as plt
import numpy as np

    
x_d = input("Ingrese los valores del array x: ").split(',')
y_d = input("Ingrese los valores del array y: ").split(',')

x_d = np.array([float(x) for x in x_d]) #0,1,2,3,4,5,6,7,8
y_d = np.array([float(y) for y in y_d]) #0,0.8,0.9,0.1,-0.6,-0.8,-1,-0.9,-0.4
    
plt.figure(figsize = (12, 8))
    
for i in range(1, 7):
    
    y_est = np.polyfit(x_d, y_d, i)
    plt.subplot(2,3,i)
    plt.plot(x_d, y_d, 'o')

    plt.plot(x_d, np.polyval(y_est, x_d))
    plt.title(f'Polynomial order {i}')
    print(y_est)

plt.tight_layout()
plt.show()





