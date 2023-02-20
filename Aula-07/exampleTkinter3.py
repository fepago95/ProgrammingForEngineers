# Calculadora simple de porcentajes.

import tkinter as tk 
import matplotlib.pyplot as plt

from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import filedialog
from collections import defaultdict
from collections import Counter

class Estadisticas:
    num_lineas: int
    num_palabras: int
    num_caracteres: int
    letras: dict

def obtener_estadisticas(ruta_a_fichero: str) -> Estadisticas:
    num_lineas, num_palabras, num_caracteres = 0, 0, 0
    letras = defaultdict(int)
    with open(ruta_a_fichero, 'r') as fr:
        for line in fr.readlines():
            num_lineas += 1
            palabras = len(line.split())
            num_palabras += palabras
            num_caracteres += len(line)
            for k, v in Counter(line.lower()).items():
                letras[k] += v
    return Estadisticas(num_lineas, num_palabras, num_caracteres, letras)

def obtener_texto(ruta_a_fichero: str) -> str:
    with open(ruta_a_fichero, 'r') as fr:
        return fr.read()

def obtener_diagrama(info: dict, nombre_imagen='.diadrama.png') -> str:
    plt.figure(figsize=(5,3))
    plt.bar(x=info.keys(), height=info.values())
    plt.xticks(fontsize=8)
    plt.yticks(fontsize=8)
    plt.savefig(nombre_imagen)
    return nombre_imagen

class AnalizadorDeTexto(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.fichero_seleccionado = None

        self.master = master
        self.pack(padx = 20, pady = 20)
        self.crear_menu()
        self.crear_componentes()
        self.posicionar_componentes()

    def crear_menu(self):
        # Crear barra de menu
        barra_menu = tk.Menu(self.master)

        # Menu archivo
        menu_archivo = tk.Menu(barra_menu, tearoff=0)
        menu_archivo.add_command(label="Abrir", command=self.abrir_archivo)
        menu_archivo.add_separator()
        menu_archivo.add_command(label="Salir", command=self.master.quit)
        barra_menu.add_cascade(label="Archivo", menu=menu_archivo)

        # Menu ayuda
        menu_ayuda = tk.Menu(barra_menu, tearoff=0)
        menu_ayuda.add_command(label="Acerca de", command=self.acerca_de)
        barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)

        self.master.config(menu=barra_menu)

    def acerca_de(self):
        # Simple cuadro de diálogo para mostrar información acerda de la aplicación
        messagebox.showinfo('Acerca de', 'Aplicación de ejemplo usando tkinter.')
        
    def crear_componentes(self):
        # CReamos los componentes y los mantenemos a la espera de que se seleccione algún fichero
        self.label_principal = tk.Label(self, text='Seleccione un fichero en el menu Archivo -> Abrir')

        # Etiqueta dque se utilizará para mostrar la imagen del análisis del fichero
        self.imagen_analisis = tk.Label(self)

        # Componentes de estadística
        self.num_palabras_lbl = tk.Label(self, text='Número de palabras: ')
        self.num_palabras_val = tk.Label(self)
        self.num_lineas_lbl = tk.Label(self, text='Número de líneas: ')
        self.num_lineas_val = tk.Label(self)
        self.num_caracteres_lbl = tk.Label(self, text='Número de caracteres: ')
        self.num_caracteres_val = tk.Label(self)

        # Componente para ver el texto
        self.texto_del_fichero = scrolledtext.ScrolledText(self)

    def posicionar_componentes(self):
        # Posiciona los componentes en función de si se ha seleccionado un fichero para analizar o no
        if not self.fichero_seleccionado:
            self.label_principal.grid(column=0, row=0, rowspan=6, columnspan=6, pady=350)
        else:
            self.imagen_analisis.grid(column=0, row=0, rowspan=6, columnspan=4, sticky='nw')
            self.num_palabras_lbl.grid(column=4, row=0)
            self.num_palabras_val.grid(column=4, row=1)
            self.num_lineas_lbl.grid(column=4, row=2)
            self.num_lineas_val.grid(column=4, row=3)
            self.num_caracteres_lbl.grid(column=4, row=4)
            self.num_caracteres_val.grid(column=4, row=5)
            self.texto_del_fichero.grid(column=0, row=8, columnspan=6, pady=15)

    def abrir_archivo(self):
        # Pide al usuario que seleccione un archivo de texto para analizarlo y mostrar en la aplicación
        ruta_archivo = filedialog.askopenfilename(title='Seleccione un fichero de texto', filetypes=(('Texto', '*.txt'),))
        if ruta_archivo:
            self.fichero_seleccionado = ruta_archivo
            self.label_principal.destroy()
            info, ruta_imagen, texto_de_archivo = self.obtener_informacion_de_fichero(self.fichero_seleccionado)
            self.mostrar_informacion_estadistica(info)       
            self.mostrar_imagen(ruta_imagen)
            self.mostrar_informacion_fichero(texto_de_archivo)
            self.posicionar_componentes()
        
    def obtener_informacion_de_fichero(self, ruta_archivo: str):
        # Analiza el fichero de texto y obtiene las estadisticas, genera la imagen y obtiene el texto
        info = obtener_estadisticas(ruta_archivo)
        ruta_a_imagen = obtener_diagrama(info.letras)
        texto_de_archivo = obtener_texto(ruta_archivo)
        return info, ruta_a_imagen, texto_de_archivo

    def mostrar_informacion_estadisticas(self, info: Estadisticas):
        # Muestra el contenido obtenido tras el análisis del fichero en la aplicación
        self.num_palabras_val.config(text=info.num_palabras)
        self.num_lineas_val.config(text=info.num_lineas)
        self.num_caracteres_val.config(text=info.num_caracteres)

    def mostrar_imagen(self, ruta_imagen):
        # Muestra la imagen generada en la aplicación
        img = tk.PhotoImage(file=ruta_imagen)
        self.imagen_analisis.config(image=img)
        self.imagen_analisis.image = img

    def mostrar_informacion_fichero(self, texto_de_fichero):
        # Agrega el contenido del fichero al componente texto_del_fichero y deja el componente como solo lectura
        self.texto_del_fichero.config(state='normal')
        self.texto_del_fichero.delete('1.0', tk.END)
        self.texto_del_fichero.insert(tk.END, texto_de_fichero)
        self.texto_del_fichero.config(state='disabled')    

if __name__ == '__main__':
    raiz = tk.Tk()
    raiz.title('Analizador de textos')
    raiz.geometry("800x800")
    app = AnalizadorDeTexto(master=raiz)
    raiz.mainloop()

########################################
# idea = https://www.youtube.com/watch?v=LrrTlK2YcCg&ab_channel=diegomoissetdeespanes