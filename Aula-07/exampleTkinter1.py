# Cuando se realizan aplicaciones más grandes, hay que seguir una metodología 
# que permite escalar con facilidad, encapsular código y reutilizar lo más posible,
# por lo que es muy recomendable hacer este tipo de aplicaciones orientadas a 
# clases como se puede ver acontinuación.

import tkinter as tk
import random

class programmingForEngineers(tk.Frame):
    textos = ['Message 1', 'Message 2', 'Message 3', 'Message 4', 'Message 5', 'Message 6', 'Message 7', 'Message 8', 'Message 9', 'Message 10']

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(padx = 150, pady = 50)
        self.crear_componentes()

    def crear_componentes(self):
        self.etiqueta = tk.Label(self, text = 'Initial message')
        self.etiqueta.pack()
        self.btn = tk.Button(self, command=self.cambiar_texto)
        self.btn.config(text = 'Click here')
        self.btn.pack()

    def cambiar_texto(self):
        texto = random.choice(self.textos)
        self.etiqueta.config(text = texto)
    
if __name__ == '__main__':
    raiz = tk.Tk()
    raiz.title('Programming for engineers')
    app = programmingForEngineers(master =  raiz)
    raiz.mainloop()

# documentación relevante: https://realpython.com/python-gui-tkinter/