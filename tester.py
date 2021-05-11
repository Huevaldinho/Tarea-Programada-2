
#CONJUNTO DE PRUEBAS TKINTER

#AL FINAL HAY VARIAS POSIBILIDADES DE MANEJO DE TKINTER
    #ES DECIR, COMO USAR, SCROLLBARS, CAJAS DE TEXTO, ETC...
#RECORDAR LA CALCULADORA QUE TAMBIÉN ESTÁ EN EL REPOSITORIO



#"""

#PROGRAMA PRUEBA
#CREADO POR DIOSBEJUCO
#HUMILDAD B)
#diversión ante todo :=====D
"""
from tkinter import *

ventana=Tk()
ventana.config(bg='lightblue')
ventana.title("Pruebas Varias con Nivel")
Mensaje=Label(ventana,text="Digite su nombre y 2 apellidos:",font="Times 24 bold",bg='lightblue',fg='green')
Mensaje.grid(row=0,column=0,columnspan=4,padx=10,pady=8)
entradaNombre=Entry(ventana,width=50 ,bd=5)
entradaNombre.grid(row=1,column=0,columnspan=4,padx=5,pady=5)
def saludo():
    texto=entradaNombre.get()
    listaTexto=texto.split(" ")
    messageVar = Message(ventana, text = 'Bienvenido al programa, su nombre es '+listaTexto[0]+' de primer apellido '+listaTexto[1]+'. \
Su segundo apellido es '+listaTexto[2]+'\n\n'+texto,font="Arial 16",bg='lightblue')
    messageVar.grid(row=3, column=0,columnspan=4)
botonOpcion=Button(ventana,text="Siguiente",bg='beige',command=lambda:saludo())
botonOpcion.grid(row=2, column=0,columnspan=4)
"""#

#
#
#
#
#
#
#
#
#"""
#ventana.mainloop()
#############
"""
cajaTexto=Entry(ventana,font="Arial 30")
cajaTexto.pack()

etiqueta=Label(ventana)
etiqueta.pack()

def textoDeLaCaja():
    texto=cajaTexto.get()
    etiqueta["text"]=texto

boton1=Button(ventana,text="click",command=textoDeLaCaja)
boton1.pack()
"""
"""
boton1=Button(ventana, text="boton1",width=10,height=5)
boton2=Button(ventana, text="boton2",width=10,height=5)
boton3=Button(ventana, text="boton3",width=10,height=5)

boton1.grid(row=0,column=0)
boton2.grid(row=1,column=0)
boton3.grid(row=2,column=0)
"""


"""
root=Tk()
e=Entry(root,width=50 ,bd=5)
e.pack()
e.insert(0,"Enter your name: ")

def myclick():
    label=Label(root,text="Hello, happy to have you!",font='Arial 25')
    label.pack()
 
boton1=Button(root,text="Enter your name: ",command=lambda: myclick())
boton1.pack()

root.mainloop()
"""
"""
#Para matar la ventana
root=Tk()
root.title('Hello this is a test')

buttonquit=Button(root,text="Exit",command=root.quit)
buttonquit.pack()

root.mainloop()
"""
"""
master = Tk()

var1 = IntVar()
Checkbutton(master, text='Male', variable=var1).grid(row=0, sticky=W)
var2 = IntVar()
Checkbutton(master, text='Female', variable=var2).grid(row=1, sticky=W)
def myclick():
    label=Label(master,text="Hello, happy to have you!",font='Arial 25')
    label.grid(row=5,column=0)
boton1=Button(master,text="Enter your name: ",command=lambda: myclick())
boton1.grid(row=3,column=0)

mainloop()
"""
#############
#INICIO DE LAS POSIBILIDADES DE MANEJO DE TKINTER
#OBVIO EXISTEN MUCHAS MÁS, ESTAS SON SOLO ALGUNAS QUE NOS PODRÁN SERVIR
#FALTA INVESTIGAR

#Matar programa
"""
import tkinter as tk
r = tk.Tk()
r.title('Counting Seconds')
button = tk.Button(r, text='Stop', width=25, command=r.destroy)
button.pack()
r.mainloop()
"""
#INTRODUCIR TEXTO
"""
from tkinter import *
master = Tk()
Label(master, text='First Name').grid(row=0)
Label(master, text='Last Name').grid(row=1)
e1 = Entry(master)
e2 = Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
mainloop()
"""
#CAJA DE OPCIONES
    #LISTBOX
"""
from tkinter import *
top = Tk()
Lb = Listbox(top)
Lb.insert(1, 'Python')
Lb.insert(2, 'Java')
Lb.insert(3, 'C++')
Lb.insert(4, 'Any other')
Lb.pack()
top.mainloop()
"""
#MOSTRAR UN MENSAJE
    #MESSAGE
#funciona como el label
"""
from tkinter import *
main = Tk()
messageVar = Message(main, text = 'This is our Message')
messageVar.config(bg='lightblue')
messageVar.pack( )
main.mainloop( )
"""
#BOTON RADIO
#es una disyuncion excluyente, o sea solo uno se escoge
"""
from tkinter import *
root = Tk()
v = IntVar()
Radiobutton(root, text='GfG', variable=v, value=1).pack(anchor=W)
Radiobutton(root, text='MIT', variable=v, value=2).pack(anchor=W)
mainloop()
"""
#SCROLLBAR
"""
from tkinter import *
root = Tk()
scrollbar = Scrollbar(root)
scrollbar.pack( side = LEFT, fill = Y )
mylist = Listbox(root, yscrollcommand = scrollbar.set )
for line in range(25):
    mylist.insert(END, 'This is line number ' + str(line))
mylist.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = mylist.yview )
mainloop()
"""
#SPINBOX
    #rango de opciones (integers)
"""
from tkinter import *

master = Tk()
w = Spinbox(master, from_ = 0, to = 5)
w.pack()
mainloop()
"""
#combobox
import tkinter as tk
from tkinter import ttk

def callbackFunc(event):
     print("New Element Selected")
     
app = tk.Tk() 
app.geometry('200x100')

labelTop = tk.Label(app,
                    text = "Choose your favourite month")
labelTop.grid(column=0, row=0)

comboExample = ttk.Combobox(app, 
                            values=[
                                    "January", 
                                    "February",
                                    "March",
                                    "April"])


comboExample.grid(column=0, row=1)
comboExample.current(1)

comboExample.bind("<<ComboboxSelected>>", callbackFunc)


app.mainloop()