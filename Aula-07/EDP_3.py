import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
sns.set_style('white')

from matplotlib import animation

x = np.linspace(0,1,101)
y = np.linspace(0,1,101)
X,Y = np.meshgrid(x,y)
u = np.zeros((101,101))
u[40,50] = 100
fig = plt.figure()
ax = plt.axes(projection='3d')
ax._axis3don = False
c = ax.contourf3D(X,Y,u,1000)

def ans(f):
    global u, c

    #Time is not defined as the animation will do the loop for T times.
    for j in range(1, 100):
        for i in range(1, 100):
            u[i,j] += (u[i+1,j] + u[i,j+1] + u[i-1,j] + u[i,j-1] - 4*u[i,j])/4
    for xx in c.collections:
        xx.remove()
    c = ax.contourf3D(X,Y,u,1000)
    return c

anim = animation.FuncAnimation(fig, ans, frames=100)
plt.show()