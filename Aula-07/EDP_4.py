# EDP - ecuación de calor usando el método explícito

import numpy as np
import matplotlib.pyplot as plt

#h = 0.25
h = 0.025
#k = 0.25
k = 0.025
x = np.arange(0, 1+h, h)
#t = np.arange(0, 1+k, k)
t = np.arange(0, 0.1+k, k)
boundaryCondition = [0, 0]
initialCondition = np.sin(np.pi*x)

n = len(x)
m = len(t)
T = np.zeros((n, m))
T[0, :] = boundaryCondition[0]
T[-1, :] = boundaryCondition[1]
T[:, 0] = initialCondition
#print(np.transpose(T.round(3)))

factor = k/h**2
for j in range(1, m):
    for i in range(1, n-1):
        T[i,j] = factor*T[i-1, j-1] + (1-2*factor)*T[i, j-1] + factor*T[i+1, j-1]

T = T.round(3)
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


# fuente: https://www.youtube.com/watch?v=NLuCx2SrxHw&ab_channel=ShameelAbdulla
