import numpy as np
import matplotlib.pyplot as plt
# Función que s eutiliza solo para crear la onda cuadrada
from scipy import signal
# Funcion para crear animaciones de la serie de Fourier
from celluloid import Camera

# Definimos el estilo de la grafica
plt.style.use('ggplot')

def fourierOndaCuadrada(x, n):
    # Creamos números impares en la variable m
    m = 2 * n - 1
    # Creamos la función de Fourier
    f = (4/np.pi)*(1/m) * np.sin((m * np.pi * x)/L)
    return f

fig = plt.figure()
camera = Camera(fig)

# Creamos el largo del ciclo de la onda
L = np.pi
# Creamos la cantidad de ciclos
ciclos = 1
# Creamos la variable espacial
x = np.linspace(-0.001, 2*ciclos*L, 10000)

# Ploteamos la onda cuadrada
#plt.plot(x, signal.square(x), color = 'black')

# Inicializamos variables
f = 0
n = 1
n_total = 10

# Realizamos la sumatoía de la función de Fourier
while n < n_total:
    f += fourierOndaCuadrada(x, n)
    #plt.plot(x, f, label = "n = {}".format(2*n-1))
    plt.plot(x , f, c = 'tab:orange')
    camera.snap()
    n += 1

plt.plot(x, signal.square(x), color = 'black')
#plt.legend()
#plt.show()
animation = camera.animate()
animation.save('fourier.gif')

# Fuente: https://www.youtube.com/watch?v=7vZyCdliYJM&ab_channel=SciCat