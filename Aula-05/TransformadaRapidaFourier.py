# Numpy trae la transformada de fourier ya definida
import numpy as np
# Importamos la librería para visualizar los datos
import matplotlib.pyplot as plt
# Definimos el estilo de la grafica
plt.style.use('classic')

class Wave:
    # Creamos un constructor
    def __init__(self):
        # Generamos una lista llamada params en donde guardamos: Amplitud, Desfase, Freq. Angular
        self.params = [np.random.rand(), np.random.rand(), np.random.rand()]

    # Creamos el metodo evaluate
    def evaluate(self, x):
        return self.params[0] * np.sin(self.params[1] + 2 * np.pi * x * self.params[2])

def main():
    # Array de ondas
    n_waves = 20

    # Lista de objetos
    waves = [Wave() for i in range(n_waves)]

    # Declaramos el domino
    x = np.linspace(-10, 10, 500)
    # Guardamos los datos de la suma de las ondas
    y = np.zeros_like(x)

    # Sumamos las ondas
    for wave in waves:
        y += wave.evaluate(x)

    # Transformada rapida de Fourier
    # Pasamos de graficar la amplitud vs tiempo contra amplitud vs frecuencia
    f = np.fft.fft(y)
    freq = np.fft.fftfreq(len(y), d = x[1] - x[0])
    
    fig, ax = plt.subplots(2)

    # Ciclo para obtener todas la ondas individuales
    for wave in waves:
        ax[0].plot(wave.evaluate(x), color = 'black', alpha = 0.3)

    ax[0].plot(y, color = 'blue')
    ax[1].plot(freq, abs(f)**2)
    plt.show()

if __name__ == '__main__':
    main()