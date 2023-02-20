# EDP - ecuación de calor usando el método implícito

import numpy as np
import matplotlib.pyplot as plt

h = 0.025
k = 0.025
x = np.arange(0, 1+h, h)
t = np.arange(0, 0.1+k, k)
boundaryCondition = [0, 0]
initialCondition = np.sin(np.pi*x)

n = len(x)
m = len(t)
T = np.zeros((n, m))
T[0, :] = boundaryCondition[0]
T[-1, :] = boundaryCondition[1]
T[:, 0] = initialCondition
factor = k/h**2
T = T.round(3)
#print(T)

A = np.diag([1+2*factor]*(n-2), 0) + np.diag([-factor]*(n-3), -1) + np.diag([-factor]*(n-3), 1)
for j in range(1, m):
    b = T[1:-1, j-1].copy()
    b[0] = b[0] + factor*T[0, j]
    b[-1] = b[-1] + factor*T[-1, j]
    solution = np.linalg.solve(A,b)
    T[1:-1, j] = solution
    print(solution)

T = T.round(3)
print(T.round(3))
t = t.round(3)

B = np.linspace(1, 0, m)
R = np.linspace(0, 1, m)
G = 0
for i in range(m):
    plt.plot(x, T[:,i], color = [R[i],G,B[i]])
    
plt.legend([f't = {value} s' for value in t], loc = 'upper right')
plt.xlabel('Distance [m]')
plt.ylabel('Temperature [$\degree$ C]')
plt.title('EDP')
plt.show()

# fuenteÇ https://www.youtube.com/watch?v=2b4Q_uE4zhk&ab_channel=ShameelAbdulla