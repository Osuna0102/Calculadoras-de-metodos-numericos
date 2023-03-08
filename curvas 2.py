import matplotlib.pyplot as plt
import numpy as np


x = np.array([300, 1500, 2100])
y = np.array([6.81495, 8.25375, 8.60055])

A = np.vstack([x, np.ones(len(x))]).T

m, c = np.linalg.lstsq(A, y, rcond=None)[0]

_ = plt.plot(x, y, 'o', label='Original data', markersize=10)
_ = plt.plot(x, m*x + c, 'r', label='Fitted line')
_ = plt.legend()
plt.show()

print(m,'* x',c)
