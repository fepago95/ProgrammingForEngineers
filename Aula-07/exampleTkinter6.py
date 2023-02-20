# Calculadora en Python con Tkinter con efecto hover

from tkinter import *

# Crea el objeto ventana
ventana = Tk()
ventana.geometry('274x328')
ventana.config(bg= "white")
ventana.iconbitmap(bitmap='icono.ico')
ventana.resizable(0,0)
ventana.title('Calculator')

# Clase para efecto hover
class HoverButton(Button):
	def __init__(self, master, **kw):
		Button.__init__(self,master=master,**kw)
		self.defaultBackground = self["background"]
		self.bind("<Enter>", self.on_enter)
		self.bind("<Leave>", self.on_leave)

	def on_enter(self, e):
		self["background"] = self["activebackground"]

	def on_leave(self, e):
		self["background"] = self.defaultBackground

# Declaración de las funciones
i=0
# Función para agregar los números seleccionados 
def obtener(dato):
	global i
	i+=1
	Resultado.insert(i, dato)

# Función para realizar las operaciones	
def operacion():
	global i
	ecuacion = Resultado.get()
	if i !=0:		
		try:
			# La funcion eval calcula el resultado
			result = str(eval(ecuacion))
			Resultado.delete(0,END)
			Resultado.insert(0,result)
			longitud = len(result)
			i = longitud
		except:
			result = 'ERROR'
			Resultado.delete(0,END)
			Resultado.insert(0,result)
	else:
		pass

# Función para borar número por número
def borrar_uno():
	global i 
	if i==-1:
		pass
	else:
		Resultado.delete(i,last =None)
		i-=1

# Función para borar todo
def borrar_todo():
	Resultado.delete(0, END)	
	#i=0

frame = Frame(ventana, bg ='#022F7F', relief = "raised")
frame.grid(column=0, row=0, padx=6, pady=3)

Resultado = Entry(frame,bg='#B7D0FC', width=18, relief='groove', font = 'Montserrat 16',justif = 'right')
Resultado.grid(columnspan=4 , row=0, pady=3,padx=1, ipadx=1, ipady=1) 

#fila 1
Button1 = HoverButton(frame, text= "1", borderwidth=2, height=2, width=5, 
	font= ('Comic sens MC',12,'bold'),relief = "raised", activebackground="#0B0361", bg ='#AFADC6',  
	anchor="center", command=lambda: obtener(1))  
Button1.grid( column= 0 ,row=1, pady=1,padx=3)

Button2 = HoverButton(frame, text= "2", height=2, width=5, 
	font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", activebackground="#0B0361", bg ='#AFADC6', 
	anchor="center",command=lambda: obtener(2))  
Button2.grid(column =1 , row=1, pady=1,padx=1)

Button3 = HoverButton(frame, text= "3", height=2, width=5,
	font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", activebackground="#0B0361", bg ='#AFADC6', 
	anchor="center",command=lambda: obtener(3))  
Button3.grid(column =2, row=1, pady=1,padx=1)

Button_borrar = HoverButton(frame, text= "⌫", height=2, width=5,
	font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", activebackground="#B28656", 
	bg='#F49E7E',  anchor="center",command=lambda: borrar_uno())  
Button_borrar.grid(column =3, row=1, pady=2,padx=2)

#fila 2
Button4 = HoverButton(frame, text= "4",height=2, width=5,font= ('Comic sens MC',12,'bold'), 
	borderwidth=2,  relief = "raised", activebackground="#0B0361", bg ='#AFADC6', anchor="center",
	command=lambda: obtener(4))  
Button4.grid( column= 0 ,row=2, pady=1,padx=1)

Button5 = HoverButton(frame, text= "5", height=2, width=5,font= ('Comic sens MC',12,'bold'), 
	borderwidth=2,  relief = "raised", activebackground="#0B0361",bg ='#AFADC6', anchor="center",
	command=lambda: obtener(5))  
Button5.grid(column =1 , row=2, pady=1,padx=1)

Button6 = HoverButton(frame, text= "6", height=2, width=5,font= ('Comic sens MC',12,'bold'), 
	borderwidth=2,  relief = "raised", activebackground="#0B0361",bg ='#AFADC6',  anchor="center",
	command=lambda: obtener(6))  
Button6.grid(column =2, row=2, pady=1,padx=1)

Button_mas = HoverButton(frame, text= "+", height=2, width=5,font= ('Comic sens MC',12,'bold'), 
	borderwidth=2,  relief = "raised", activebackground="#274E59", bg='#0CA3CB',  anchor="center",
	command=lambda: obtener('+'))  
Button_mas.grid(column =3, row=2, pady=2,padx=2)

#fila 3
Button7 = HoverButton(frame, text= "7",height=2, width=5, font= ('Comic sens MC',12,'bold'), 
	borderwidth=2,  relief = "raised", activebackground="#0B0361",bg ='#AFADC6',  anchor="center",
	command=lambda: obtener(7))  
Button7.grid( column= 0 ,row=3, pady=1,padx=1)

Button8 = HoverButton(frame, text= "8", height=2, width=5,font= ('Comic sens MC',12,'bold'), 
	borderwidth=2,  relief = "raised", activebackground="#0B0361",bg ='#AFADC6', anchor="center",
	command=lambda: obtener(8))  
Button8.grid(column =1 , row=3, pady=1,padx=1)

Button9 = HoverButton(frame, text= "9", height=2, width=5,font= ('Comic sens MC',12,'bold'), 
	borderwidth=2,  relief = "raised", activebackground="#0B0361",bg ='#AFADC6',  anchor="center",
	command=lambda: obtener(9))  
Button9.grid(column =2, row=3, pady=1,padx=1)

Button_menos = HoverButton(frame, text= "-", height=2, width=5,font= ('Comic sens MC',12,'bold'), 
	borderwidth=2,  relief = "raised", activebackground="#274E59", bg='#0CA3CB',  anchor="center",
	command=lambda: obtener('-'))  
Button_menos.grid(column =3, row=3, pady=2,padx=2)

#fila 4
Button0 = HoverButton(frame, text= "0",height=5, width=5,font= ('Comic sens MC',12,'bold'), 
	borderwidth=2,  relief = "raised", activebackground="#0B0361",bg ='#AFADC6',  anchor="center",
	command=lambda: obtener(0))  
Button0.grid( column= 0, rowspan=2, row=4, pady=1,padx=1)

Button_punto = HoverButton(frame, text= ".", height=2, width=5,font= ('Comic sens MC',12,'bold'), 
	borderwidth=2,  relief = "raised", activebackground="#0B0361",bg ='#AFADC6', anchor="center",
	command=lambda: obtener('.'))  
Button_punto.grid(column =1 , row=4, pady=1,padx=1)

Button_entre = HoverButton(frame, text= "÷", height=2, width=5,font= ('Comic sens MC',12,'bold'), 
	borderwidth=2,  relief = "raised", activebackground="#274E59",bg ='#0CA3CB',  anchor="center",
	command=lambda: obtener('/'))  
Button_entre.grid(column =2, row=4, pady=1,padx=1)

Button_por = HoverButton(frame, text= "x", height=2, width=5,font= ('Comic sens MC',12,'bold'), 
	borderwidth=2,  relief = "raised", activebackground="#274E59", bg='#0CA3CB',  anchor="center",
	command=lambda: obtener('*'))  
Button_por.grid(column =3, row=4, pady=2,padx=2)

#fila 4
Button_igual = HoverButton(frame, text= "=", height=2, width=5,font= ('Comic sens MC',12,'bold'), 
	borderwidth=2,  relief = "raised", activebackground="#942101", bg='#F67E5D', anchor="center",
	command=lambda: operacion())  
Button_igual.grid(column =1 , row=5, pady=1,padx=1)

Button_raiz = HoverButton(frame, text= "√", height=2, width=5,font= ('Comic sens MC',12,'bold'), 
	borderwidth=2,  relief = "raised", activebackground="#274E59",bg ='#0CA3CB', anchor="center",
	command=lambda: obtener('**(1/2)'))  
Button_raiz.grid(column = 2 , row=5, pady=1,padx=1)

Button_borrar = HoverButton(frame, text= "C", height=2, width=5,font= ('Comic sens MC',12,'bold'), 
	borderwidth=2, relief = "raised", activebackground="#40584D", bg='#0CBD6F', anchor="center",
	command=lambda: borrar_todo())  
Button_borrar.grid(column =3, row=5, pady=2,padx=2)

ventana.mainloop()

# fuente: https://www.youtube.com/watch?v=pxi8ec-mqAQ&ab_channel=MagnoEfren
# fuente: https://github.com/MagnoEfren/Calculator_Tkinter/blob/main/calculadora2.py
# documentación relevante: https://realpython.com/python-gui-tkinter/
