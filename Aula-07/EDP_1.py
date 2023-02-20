import numpy as np

from matplotlib import pyplot as plt

# Longitud
L = 100

# Creamos un array numpy linspace para los calores de X
x = np.linspace(0, 1, L)
# Creamos un array de zeros del tamaño de L
T = np.zeros(L)

# Declaramos la condición inicial
T[L//2] = 1  

#  Declaramos las condición limitantes
T[0] = 0
T[L-1] = 0

# Ciclo for para recorrer el tiempo
for t in range(100):
    # Ciclo for para recorrer el espacio
    for i in range(1, L-1):
        T[i] += (T[i+1] - 2*T[i] + T[i-1])/4

fig, ax = plt.subplots()
ax.scatter(x, T, linewidth=15, c=T, cmap='jet')
plt.xlabel('Space')
plt.ylabel('Temperature')
plt.title('EDP - Diffusion Equation')
plt.show()