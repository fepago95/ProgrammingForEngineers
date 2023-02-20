import tkinter as tk

from tkinter import messagebox

# Creamos la clase App
class App():
    # Creamos el método que es un constructor
    # Declaramos el self para poder usar cada uno de los atributos despues
    # Debido a que estamos trabajando con programación orientada a objetos
    def __init__(self):
        # Creamos el objetvio de tipo Tkinter
        ventana = tk.Tk()
        ventana.title('Ventana principal')
        ventana.geometry("400x200")
        ventana.configure(background='Black', cursor='spider')

        # Widgets
        self.label1 = tk.Label(ventana, text='Nombre')
        self.label1.place(x=50, y=30)

        self.text1 = tk.Entry(ventana, background='white', justify='center')
        self.text1.place(x=150, y=30)

        # Boton
        self.bt1 = tk.Button(ventana, text='Aceptar', background='orange', command=self.mensaje)
        self.bt1.place(x=200, y=100)

        # Este metodo ejecuta el evento y lo deja contante
        ventana.mainloop()
    
    # Creamos el método mensaje
    def mensaje(self):
        #print('Bienvenido al sistema')
        messagebox.showinfo(message='Bienvenido al sistema ' + self.text1.get() , title='Saludo')
    
# Programa principal
Objeto_ventana = App()

# fuente: https://www.youtube.com/watch?v=8yqg-KpBmow&ab_channel=VladimirGuajardoGonzalez
# documentación relevante: https://realpython.com/python-gui-tkinter/