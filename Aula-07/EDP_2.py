import numpy as np
import matplotlib.pyplot as plt
# Libreria para obtener mas estilos
import seaborn as sns
sns.set()

from matplotlib import animation

T = np.zeros((100, 100))
T[30,20] = 1

fig, ax = plt.subplots(figsize=(5, 5))
plot = ax.contourf(T)
def ans(f):
    global T, plot
    
    #Time is not defined as the animation will do the loop for T times.
    for j in range(1, 99):
        for i in range(1, 99):
            T[i,j] += (T[i+1,j] + T[i,j+1] + T[i-1,j] + T[i,j-1] - 4*T[i,j])/4
    for c in plot.collections:
        c.remove()
    plot = ax.contourf(T)
    return plot

anim = animation.FuncAnimation(fig, ans, frames=100)
plt.show()