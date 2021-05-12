#Este código es para la selección de provincia, la misma lógica sirve para seleccionar el sexo y la justificación.
"""
from tkinter import *
from funciones import *
from tkinter import messagebox
def helloCallBack():
    messagebox.showerror("Error","Debe ingresar ambos datos")

def seleccionar():
    monitor.config(text="{}".format(opcion.get()))
def reset():
    opcion.set(None)
    monitor.config(text="")
#Selecctor de provincias
root = Tk()
opcion = IntVar()
def escogido():
    escogio=opcion.get()
    print(escogio)
Radiobutton(root, text="1.Su peso bajó a menos de 50 kgms", variable=opcion,value=1,command=seleccionar).pack()
Radiobutton(root, text="2.No se puede donar sangre si la persona ha sido trasplantada, es decir, ha recibido un trasplante de órgano", variable=opcion,value=2, command=seleccionar).pack()
Radiobutton(root, text="3.Enfermedades como: tuberculosis, cáncer o cualquier enfermedad coronaria.", variable=opcion,value=3, command=seleccionar).pack()   
Radiobutton(root, text="4.Si el donante esadicto a ningún tipo de droga.", variable=opcion,value=4, command=seleccionar).pack()   
Radiobutton(root, text="5.Padecióhepatitis B o C.", variable=opcion,value=5, command=seleccionar).pack()   
Radiobutton(root, text="6.Si has padecido de mal de Chagas no puedes donar.", variable=opcion,value=6, command=seleccionar).pack()
    
monitor = Label(root)
monitor.pack()
# Finalmente bucle de la aplicación
root.mainloop()
###################################################################################################################
#
"""
from tkinter import *
from funciones import *
from tkinter import messagebox
root=Tk()#ventana principal
root.geometry("600x400")#le da tamaño a la ventana principal
name_var=StringVar()#almacena el texto que se meta en el cuadro de username
passw_var=StringVar()#almacena el texto que se meta en el cuadro de la contraseña
cedula_var=StringVar()
def submit():#función que se llama cuando se le da el boton submit.
    name=name_var.get()#toma lo que se ingrese en el cuadro de usuario
    password=passw_var.get()#toma lo que se ignrese en el cuadro de contraseña.
    cedula=cedula_var.get()
    if validarCedula(cedula):
        #print("The name is : " + name)
        #print("The password is : " + password)
        print("La cédula es:",cedula)
    else:
        messagebox.showerror("Error", "Cédula inválida")
    cedula_var.set("")
    name_var.set("")#reinicia el contenido del cuadro
    passw_var.set("")#reinicia el contenido del cuadro
#Etiqueta del username
name_label = Label(root, text = 'Username', font=('times new roman',10, 'bold'))
name_label.grid(row=0,column=0)#ordena la etiqueta en la matriz
#cuadro de entrada de dato de username
name_entry = Entry(root,textvariable = name_var, font=('calibre',10,'normal'))
name_entry.grid(row=0,column=1)#ordena el cuadro de ingresar en la matriz
#Etiqueta del cedula
cedula_label = Label(root, text = 'Cedula', font=('arial',10, 'bold'))
cedula_label.grid(row=1,column=0)
#cuadro de entrada de dato cedula
cedula_entry = Entry(root,textvariable = cedula_var, font=('calibre',10,'normal'))
cedula_entry.grid(row=1,column=1)
#Etiqueta de la contraseña
passw_label = Label(root, text = 'Password', font = ('calibre',10,'bold'))
passw_label.grid(row=2,column=0)
#Cuadro de entrada de la contraseña
passw_entry=Entry(root, textvariable = passw_var, font = ('calibre',10,'normal'), show = '*')
passw_entry.grid(row=2,column=1)
#Crear el boton
#el boton llama a función submit
sub_btn=Button(root,text = 'Ingresar', command = submit)
sub_btn.grid(row=3,column=1)
root.mainloop()#muestra la ventana haciendo un ciclo infinito

#COMBOBOX OBTIENE VALOR SELECCIONADO
import tkinter as tk
from tkinter import StringVar, ttk
from tkinter.constants import COMMAND
from tkinter import messagebox
def pruebaCombobox():
    app = tk.Tk() #ventana
    app.geometry('400x200')#tamaño ventana
    prueba=StringVar()#manda a pedir el valor seleccionado en el combobox
    def funcion(recibe):
        listaJustificaciones=["Su peso bajó a menos de 50 kgms.",
"No se puede donar sangre si la persona ha sido trasplantada, es decir, ha recibido un trasplante de órgano.",
"Enfermedades como: tuberculosis, cáncer o cualquier enfermedad coronaria.",
"Si el donante esadicto a ningún tipo de droga.","Padecióhepatitis B o C.",
"Si has padecido de mal de Chagas no puedes donar."]
        x=prueba.get()#manda a pedir el valor seleccionado que está en prueba.
        if x==listaJustificaciones[0]:
            print(1,x)
        elif x==listaJustificaciones[1]:
            print(2,x)
        elif x==listaJustificaciones[2]:
            print(3,x)
        elif x==listaJustificaciones[3]:
            print(4,x)
        elif x==listaJustificaciones[4]:
            print(5,x)
        else:
            print(6,x)
        print("PREGUNTAR SI CONFIRMA")
        confirma=messagebox.askquestion("Confirmar eliminación", "Desea eliminarlo?")
        print(confirma)#retorna yes o no
        if confirma=="yes":
            print("entra")
        else:
            print("no hace nada")
        return
    labelTop = tk.Label(app,text = "Seleccione provincia")
    labelTop.grid(column=0, row=0,padx=10,pady=10)#ubicación de etiqueta

    comboExample = ttk.Combobox(app,textvariable=prueba,values=["Su peso bajó a menos de 50 kgms."
    ,"No se puede donar sangre si la persona ha sido trasplantada, es decir, ha recibido un trasplante de órgano.",
    "Enfermedades como: tuberculosis, cáncer o cualquier enfermedad coronaria.",
    "Si el donante esadicto a ningún tipo de droga.","Padecióhepatitis B o C.",
    "Si has padecido de mal de Chagas no puedes donar."])#
    comboExample.grid(column=0, row=1,padx=10,pady=10)
    #comboExample.current(0)#pone como determinado alguno de la lista.
    comboExample.bind("<<ComboboxSelected>>", funcion)
    app.mainloop()
pruebaCombobox()
