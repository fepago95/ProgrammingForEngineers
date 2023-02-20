# Ejemplo de cómo se puede construir una aplicación que contiene una etiqueta en la que se tiene un texto
# y cada vez que se da un clic dicho texto va cambiando, por otro texto que es elegido de forma aleatoria 
# de una lista predefinida.

import tkinter as tk
import random

# función cambia texto
def cambia_texto(label_wt, textos):
    texto = random.choice(textos)
    label_wt.config(text=texto)

# Permite saber si un script esta siendo importado o ejecutado desde la función principal
if __name__ == '__main__':
    # Definimos la lista de textos
    textos = ['Message 1', 'Message 2', 'Message 3', 'Message 4', 'Message 5', 'Message 6', 'Message 7', 'Message 8', 'Message 9', 'Message 10']

    # Establecemos el interprete
    raiz = tk.Tk()
    raiz.title('First window')

    # Creamos el frame
    app = tk.Frame(raiz)
    app.pack(padx = 150, pady = 50)

    etiqueta = tk.Label(app, cnf=dict(text = 'Initial message'))
    etiqueta.pack()

    # Se utiliza lambda para añadir la funcionalidad al boton
    btn = tk.Button(app, command=lambda: cambia_texto(etiqueta, textos))
    btn.config(text = 'Click here')
    btn.pack()

    raiz.mainloop()