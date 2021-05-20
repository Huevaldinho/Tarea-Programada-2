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
"""
#COMBOBOX OBTIENE VALOR SELECCIONADO
import tkinter as tk
from tkinter import StringVar, ttk
from tkinter.constants import COMMAND
def pruebaCombobox():
    app = tk.Tk() #ventana
    app.geometry('400x200')#tamaño ventana
    prueba=StringVar()#manda a pedir el valor seleccionado en el combobox
    def funcion(recibe):
        x=prueba.get()#manda a pedir el valor seleccionado que está en prueba.
        print(x)#solo para ver que sirve
    labelTop = tk.Label(app,text = "Seleccione provincia")
    labelTop.grid(column=0, row=0,padx=10,pady=10)#ubicación de etiqueta

    comboExample = ttk.Combobox(app,textvariable=prueba,values=["San José"
    ,"Alajuela","Cartago","Heredia","Guanacaste","Puntarenas","Limón"
    ,"Nacionalizado o naturalizados","Casos especiales"])#
    comboExample.grid(column=0, row=1,padx=10,pady=10)
    #comboExample.current(0)#pone como determinado alguno de la lista.
    comboExample.bind("<<ComboboxSelected>>", funcion)
    app.mainloop()
pruebaCombobox()
"""
"""
1.Insertar donador
2.Generardonadores. 
3.Actualizar datosdel donador
4.Eliminar donador
5.Insertar lugar de donación según provincia. 
6.Reportes
7.Salir
"""

from enum import auto
from os import pardir
from re import T
from tkinter import *
from tkinter import StringVar, ttk
from tkinter.constants import COMMAND
from tkinter import messagebox
from typing import Collection, Literal
from funciones import *

def insertar():
    #usar toplevel() en secundarias en vez de Tk, para no consumir tanto recurso o algo así XD.
    ventanaInsertar=Toplevel()
    ventanaInsertar.resizable(width=False, height=False)
    
    ventanaInsertar.title("Insertar Donador")

    cedulaAlmacen=StringVar()
    nombreAlmacen=StringVar()
    fechaNacimientoAlmacen=StringVar()
    sangreAlmacen=StringVar()
    sexoAlmacen=BooleanVar()
    pesoAlmacen=IntVar()
    telefonoAlmacen=StringVar()
    correoAlmacen=StringVar()

    cedula_label=Label(ventanaInsertar,text="Cédula")
    nombre_label=Label(ventanaInsertar,text="Nombre Completo")
    fechaNacimiento_label=Label(ventanaInsertar,text="Fecha de Nacimiento")
    sangre_label=Label(ventanaInsertar,text="Tipo de Sangre")
    sexo_label=Label(ventanaInsertar,text="Sexo")
    peso_label=Label(ventanaInsertar,text="Peso (kg)")
    telefono_label=Label(ventanaInsertar,text="Teléfono")
    correo_label=Label(ventanaInsertar,text="Correo Electrónico")

    cedula_entry=Entry(ventanaInsertar,textvariable=cedulaAlmacen,width=30 ,bd=5)
    nombre_entry=Entry(ventanaInsertar,textvariable=nombreAlmacen,width=30 ,bd=5)
    fechaNacimiento_entry=Entry(ventanaInsertar,textvariable=fechaNacimientoAlmacen,width=30 ,bd=5)
    sangre_entry=ttk.Combobox(ventanaInsertar,textvariable=sangreAlmacen,values=["O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-"])
    sexo_masculino=Radiobutton(ventanaInsertar, text='Masculino', variable=sexoAlmacen, value=True,width=30 ,bd=5)
    sexo_femenino=Radiobutton(ventanaInsertar, text='Femenino', variable=sexoAlmacen, value=False,width=30 ,bd=5)
    peso_entry=Entry(ventanaInsertar,textvariable=pesoAlmacen,width=30 ,bd=5)
    telefono_entry=Entry(ventanaInsertar,textvariable=telefonoAlmacen,width=30 ,bd=5)
    correo_entry=Entry(ventanaInsertar,textvariable=correoAlmacen,width=30 ,bd=5)

    cedula_label.grid(row=0,column=0,padx=5,pady=5)
    nombre_label.grid(row=1,column=0,padx=5,pady=5)
    fechaNacimiento_label.grid(row=2,column=0,padx=5,pady=5)
    sangre_label.grid(row=3,column=0,padx=5,pady=5)
    sexo_label.grid(row=4,column=0,padx=5,pady=5)
    peso_label.grid(row=6,column=0,padx=5,pady=5)
    telefono_label.grid(row=7,column=0,padx=5,pady=5)
    correo_label.grid(row=8,column=0,padx=5,pady=5)

    cedula_entry.grid(row=0,column=1,columnspan=4,padx=5,pady=5)
    nombre_entry.grid(row=1,column=1,columnspan=4,padx=5,pady=5)
    fechaNacimiento_entry.grid(row=2,column=1,columnspan=4,padx=5,pady=5)
    sangre_entry.grid(row=3,column=1,columnspan=4,padx=5,pady=5)
    sexo_masculino.grid(row=4,column=1,columnspan=4,padx=5,pady=5)
    sexo_femenino.grid(row=5,column=1,columnspan=4,padx=5,pady=5)
    peso_entry.grid(row=6,column=1,columnspan=4,padx=5,pady=5)
    telefono_entry.grid(row=7,column=1,columnspan=4,padx=5,pady=5)
    correo_entry.grid(row=8,column=1,columnspan=4,padx=5,pady=5)

    def limpiar():
        cedulaAlmacen.set("")
        nombreAlmacen.set("")
        fechaNacimientoAlmacen.set("")
        sangreAlmacen.set("")
        sexoAlmacen.set(False)
        pesoAlmacen.set(0)
        telefonoAlmacen.set("")
        correoAlmacen.set("")

    def validarTodo():
        try:
            if validarCedula(cedulaAlmacen.get()):
                if revisarLista(cedulaAlmacen.get())==False:
                    if validarNombreCompleto(nombreAlmacen.get()):
                        if validarFecha(fechaNacimientoAlmacen.get()):
                            if validarPeso(pesoAlmacen.get()):
                                if validarTelefono(telefonoAlmacen.get()):
                                    if validarCorreo(correoAlmacen.get()):
                                        lista=[nombreAlmacen.get(),
                                        cedulaAlmacen.get(),
                                        sangreAlmacen.get(),
                                        sexoAlmacen.get(),
                                        fechaNacimientoAlmacen.get(),
                                        pesoAlmacen.get(),
                                        correoAlmacen.get(),
                                        telefonoAlmacen.get(),
                                        1,
                                        0]
                                        matriz=lee("donadores")
                                        matriz.append(lista)
                                        graba("donadores",matriz)
                                        messagebox.showinfo("Donador Registrado","Donador Registrado con Éxito")
                                        limpiar()
                                    else:
                                        messagebox.showerror("Error de Formato","El correo electrónico contiene un formato incorrecto.")
                                        limpiar()
                                else:
                                    messagebox.showerror("Error de Formato","El número de teléfono contiene un formato incorrecto.")
                                    limpiar()
                            else:
                                messagebox.showerror("Error de Formato","El peso contiene un formato incorrecto. Debe ser mayor a 50 kg.")
                                limpiar()
                        else:
                            messagebox.showerror("Error de Formato","La fecha de nacimiento contiene un formato incorrecto.")
                            limpiar()
                    else:
                        messagebox.showerror("Error de Formato","El nombre contiene un formato incorrecto.")
                        limpiar()
                else:
                    messagebox.showerror("Error de datos","La persona que ha ingresado ya se encuentra como donante.")
                    limpiar()
            else:
                messagebox.showerror("Cédula Inválida","El formato de la cédula es incorrecto.")
                limpiar()
        except:
            messagebox.showerror("Error de formato","Los datos que ha ingresado son inválidos.")
    
    botonSalirVentanaInsertar=Button(ventanaInsertar,text="Regresar",command=ventanaInsertar.destroy)#sale de la ventana insertar
    botonLimpiarVentanaInsertar=Button(ventanaInsertar,text="Limpiar",command=limpiar)
    botonRegistrarVentanaInsertar=Button(ventanaInsertar,text="Registrar",command=validarTodo)

    botonSalirVentanaInsertar.grid(row=9,column=0,padx=5,pady=5)
    botonRegistrarVentanaInsertar.grid(row=9,column=2,padx=5,pady=5)
    botonLimpiarVentanaInsertar.grid(row=9,column=4,padx=5,pady=5)
def generar():
    ventanaGenerar=Toplevel()
    ventanaGenerar.title("Generar Donadores")
    ventanaGenerar.geometry("450x100")
    ventanaGenerar.resizable(width=False, height=False)

    cuantosAlmacen=IntVar()

    cuantos_label=Label(ventanaGenerar,text="¿Cuántos donadores desea generar?")
    entrada=Entry(ventanaGenerar,textvariable=cuantosAlmacen,width=20,bd=5)

    cuantos_label.grid(row=0,column=0,padx=4,pady=7)
    entrada.grid(row=0,column=1,columnspan=2,padx=7,pady=7)

    def genera():
        try:
            if cuantosAlmacen.get()==0:
                messagebox.showerror("Lista no generada","Digite un valor mayor a 0")
            else:
                graba("donadores",generarDonadores(cuantosAlmacen.get()))
                messagebox.showinfo("Donadores Generados","Donadores generados con éxito en el archivo de nombre \"donadores\"")
                cuantosAlmacen.set(0)
        except:
            messagebox.showerror("Acción Incompletada","Digite un valor válido")

    botonGenerar=Button(ventanaGenerar,text="Generar",width=8,command=genera)
    botonGenerar.grid(row=1,column=0,padx=10,pady=10)
    botonGenerar.place(relx=0.5,rely=0.57,anchor=CENTER)
    botonSalirVentanaGenerar=Button(ventanaGenerar,text="Salir",command=ventanaGenerar.destroy)#sale de la ventana insertar
    botonSalirVentanaGenerar.grid(row=2,column=0,padx=10,pady=10)
    botonSalirVentanaGenerar.place(relx=0.5,rely=0.86,anchor=CENTER)
def actualizar():
    ventanaActualizar=Toplevel()
    ventanaActualizar.title("Actualizar Donadores")
    ventanaActualizar.geometry("350x100")
    ventanaActualizar.resizable(width=False, height=False)

    cedulaAlmacen=StringVar()

    cuantos_label=Label(ventanaActualizar,text="Cédula del donador")
    entrada=Entry(ventanaActualizar,textvariable=cedulaAlmacen,width=20,bd=5)
    cuantos_label.grid(row=0,column=0,padx=4,pady=7)
    entrada.grid(row=0,column=1,columnspan=2,padx=7,pady=7)

    def verificarActualizacion():
        if cedulaAlmacen.get()=="":
            messagebox.showerror("Cédula Inválida","Ingrese una cédula")
        else:
            if validarCedula(cedulaAlmacen.get()):
                for i in lee("donadores"):
                    if cedulaAlmacen.get()==i[1]:
                        condicion=True
                        break
                    else:
                        condicion=False
                if condicion==False:
                    messagebox.showerror("Datos Erróneos","La persona con el número de cédula "+cedulaAlmacen.get()+" no está registrada en la base de datos del \
Banco de Sangre aún.")
                else:
                    ventanaInsertar=Toplevel()
                    ventanaInsertar.resizable(width=False, height=False)
                    ventanaInsertar.title("Insertar Donador")

                    nombreAlmacen=StringVar()
                    fechaNacimientoAlmacen=StringVar()
                    sangreAlmacen=StringVar()
                    sexoAlmacen=BooleanVar()
                    pesoAlmacen=IntVar()
                    telefonoAlmacen=StringVar()
                    correoAlmacen=StringVar()

                    nombre_label=Label(ventanaInsertar,text="Nombre Completo")
                    fechaNacimiento_label=Label(ventanaInsertar,text="Fecha de Nacimiento")
                    sangre_label=Label(ventanaInsertar,text="Tipo de Sangre")
                    sexo_label=Label(ventanaInsertar,text="Sexo")
                    peso_label=Label(ventanaInsertar,text="Peso (kg)")
                    telefono_label=Label(ventanaInsertar,text="Teléfono")
                    correo_label=Label(ventanaInsertar,text="Correo Electrónico")

                    nombre_entry=Entry(ventanaInsertar,textvariable=nombreAlmacen,width=30 ,bd=5)
                    fechaNacimiento_entry=Entry(ventanaInsertar,textvariable=fechaNacimientoAlmacen,width=30 ,bd=5)
                    sangre_entry=ttk.Combobox(ventanaInsertar,textvariable=sangreAlmacen,values=["O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-"])
                    sexo_masculino=Radiobutton(ventanaInsertar, text='Masculino', variable=sexoAlmacen, value=True,width=30 ,bd=5)
                    sexo_femenino=Radiobutton(ventanaInsertar, text='Femenino', variable=sexoAlmacen, value=False,width=30 ,bd=5)
                    peso_entry=Entry(ventanaInsertar,textvariable=pesoAlmacen,width=30 ,bd=5)
                    telefono_entry=Entry(ventanaInsertar,textvariable=telefonoAlmacen,width=30 ,bd=5)
                    correo_entry=Entry(ventanaInsertar,textvariable=correoAlmacen,width=30 ,bd=5)

                    nombre_label.grid(row=0,column=0,padx=5,pady=5)
                    fechaNacimiento_label.grid(row=1,column=0,padx=5,pady=5)
                    sangre_label.grid(row=2,column=0,padx=5,pady=5)
                    sexo_label.grid(row=3,column=0,padx=5,pady=5)
                    peso_label.grid(row=5,column=0,padx=5,pady=5)
                    telefono_label.grid(row=6,column=0,padx=5,pady=5)
                    correo_label.grid(row=7,column=0,padx=5,pady=5)

                    nombre_entry.grid(row=0,column=1,columnspan=4,padx=5,pady=5)
                    fechaNacimiento_entry.grid(row=1,column=1,columnspan=4,padx=5,pady=5)
                    sangre_entry.grid(row=2,column=1,columnspan=4,padx=5,pady=5)
                    sexo_masculino.grid(row=3,column=1,columnspan=4,padx=5,pady=5)
                    sexo_femenino.grid(row=4,column=1,columnspan=4,padx=5,pady=5)
                    peso_entry.grid(row=5,column=1,columnspan=4,padx=5,pady=5)
                    telefono_entry.grid(row=6,column=1,columnspan=4,padx=5,pady=5)
                    correo_entry.grid(row=7,column=1,columnspan=4,padx=5,pady=5)
                    def limpiar():
                        nombreAlmacen.set("")
                        fechaNacimientoAlmacen.set("")
                        sangreAlmacen.set("")
                        sexoAlmacen.set(False)
                        pesoAlmacen.set(0)
                        telefonoAlmacen.set("")
                        correoAlmacen.set("")
                    
                    def verificarActualizacionValido():
                        try:
                            if validarCedula(cedulaAlmacen.get()):
                                if validarNombreCompleto(nombreAlmacen.get()):
                                    if validarFecha(fechaNacimientoAlmacen.get()):
                                        if validarPeso(pesoAlmacen.get()):
                                            if validarTelefono(telefonoAlmacen.get()):
                                                if validarCorreo(correoAlmacen.get()):
                                                    lista=[nombreAlmacen.get(),
                                                    cedulaAlmacen.get(),
                                                    sangreAlmacen.get(),
                                                    sexoAlmacen.get(),
                                                    fechaNacimientoAlmacen.get(),
                                                    pesoAlmacen.get(),
                                                    correoAlmacen.get(),
                                                    telefonoAlmacen.get(),
                                                    1,
                                                    0]
                                                    matriz=lee("donadores")
                                                    matriz.append(lista)
                                                    graba("donadores",matriz)
                                                    messagebox.showinfo("Cambios Registrados","Datos actualizados correctamente.")
                                                    limpiar()
                                                else:
                                                    messagebox.showerror("Error de Formato","El correo electrónico contiene un formato incorrecto.")
                                                    limpiar()
                                            else:
                                                messagebox.showerror("Error de Formato","El número de teléfono contiene un formato incorrecto.")
                                                limpiar()
                                        else:
                                            messagebox.showerror("Error de Formato","El peso contiene un formato incorrecto. Debe ser mayor a 50 kg.")
                                            limpiar()
                                    else:
                                        messagebox.showerror("Error de Formato","La fecha de nacimiento contiene un formato incorrecto.")
                                        limpiar()
                                else:
                                    messagebox.showerror("Error de Formato","El nombre contiene un formato incorrecto.")
                                    limpiar()
                            else:
                                messagebox.showerror("Cédula Inválida","El formato de la cédula es incorrecto.")
                                limpiar()
                        except:
                            messagebox.showerror("Error de formato","Los datos que ha ingresado son inválidos.")
                        ventanaInsertar.destroy

                    botonSalirVentanaInsertar=Button(ventanaInsertar,text="Regresar",command=ventanaInsertar.destroy)#sale de la ventana insertar
                    botonLimpiarVentanaInsertar=Button(ventanaInsertar,text="Limpiar",command=limpiar)
                    botonRegistrarVentanaInsertar=Button(ventanaInsertar,text="Registrar",command=verificarActualizacionValido)
                    botonSalirVentanaInsertar.grid(row=9,column=0,padx=5,pady=5)
                    botonRegistrarVentanaInsertar.grid(row=9,column=2,padx=5,pady=5)
                    botonLimpiarVentanaInsertar.grid(row=9,column=4,padx=5,pady=5)
            else:
                messagebox.showerror("Cédula Inválida","La cédula "+cedulaAlmacen.get()+" no cumple con el formato correcto.")

    botonDeCambios=Button(ventanaActualizar,text="Actualizar",width=8,command=verificarActualizacion)
    botonDeCambios.grid(row=1,column=0,padx=10,pady=10)
    botonDeCambios.place(relx=0.5,rely=0.57,anchor=CENTER)
    botonSalirVentanaActualizar=Button(ventanaActualizar,text="Salir",command=ventanaActualizar.destroy)
    botonSalirVentanaActualizar.grid(row=2,column=0,padx=10,pady=10)
    botonSalirVentanaActualizar.place(relx=0.5,rely=0.86,anchor=CENTER)
def eliminar():
    ventanaEliminar=Toplevel()
    ventanaEliminar.geometry("500x170")
    ventanaEliminar.resizable(width=False, height=False)
    ventanaEliminar.title("Eliminar Donadores")
    cedula_var=StringVar()
    justi=StringVar()

    def validarJustificacion():
        if validarCedula(cedula_var.get())==False:
            messagebox.showerror("Error cédula","Cédula inválida, intente de nuevo.")
            cedula_var.set("")
            return ""
        lista=["Peso menor a 50 kgs.",
    "Persona ha recibido un trasplante de órgano.",
    "Padece enfermedades como tuberculosis, cáncer o cualquier enfermedad coronaria.",
    "Donante adicto a alguna droga.","Padeció hepatitis B o C.",
    "Padece de mal de Chagas."]
        if justi.get()==lista[0]:
            seleccion=1
        elif justi.get()==lista[1]:
            seleccion=2
        elif justi.get()==lista[2]:
            seleccion=3
        elif justi.get()==lista[3]:
            seleccion=4
        elif justi.get()==lista[4]:
            seleccion=5
        elif justi.get()==lista[5]:
            seleccion=6
        else:
            messagebox.showerror("Error de justificación","Debe ingresar una justificación válida.")
            cedula_var.set("")
            justi.set("")
            return 
        
        confirma=messagebox.askquestion("Eliminar","¿Desea eliminar a este donador?")
        if confirma=="yes":
            eliminar=eliminarDonador(cedula_var.get(),seleccion)
            if eliminar==False:
                messagebox.showerror("Error al eliminar","Este donador ya se encuentra inactivo")
                cedula_var.set("")
                justi.set("")
                return
            if eliminar=="":
                messagebox.showerror("Error de donador","El donador no se encuentra registrado.")
                cedula_var.set("")
                justi.set("")
                return
            else:
                messagebox.showinfo("Eliminado","Donador eliminado satisfactoriamente.")
                cedula_var.set("")
                justi.set("")
                return
        else:
            messagebox.showinfo("Eliminación cancelada","No se ha eliminado el donador")
            cedula_var.set("")
            justi.set("")
        return 

    cedula_label = Label(ventanaEliminar, text = 'Cédula del donador')
    
    cedula_entry = Entry(ventanaEliminar,textvariable = cedula_var,width=33,bd=5)#entrada
    botonSalirVentanaEliminar=Button(ventanaEliminar,text="Salir",command=ventanaEliminar.destroy)
    lista=["Peso menor a 50 kgs.",
    "Persona ha recibido un trasplante de órgano.",
    "Padece enfermedades como tuberculosis, cáncer o cualquier enfermedad coronaria.",
    "Donante adicto a alguna droga.","Padeció hepatitis B o C.",
    "Padece de mal de Chagas."]
    desplegableJustificaciones = ttk.Combobox(ventanaEliminar,width=50,textvariable=justi,values=lista)
    botonEliminar=Button(ventanaEliminar,text = 'Eliminar donador',width=15,command=validarJustificacion)#, command=lambda:submit(cedula_var)
    
    cedula_label.grid(row=2,column=0,padx=10,pady=10)
    cedula_entry.grid(row=2,column=1,columnspan=5,padx=10,pady=10)
    desplegableJustificaciones.grid(row=3,column=1,columnspan=5,padx=10,pady=10)
    #desplegableJustificaciones.bind("<<ComboboxSelected>>")meter parámetro que llama a funcion.
    botonEliminar.grid(row=4,column=1,padx=10,pady=10)
    botonEliminar.place(relx=0.5,rely=0.7,anchor=CENTER)
    botonSalirVentanaEliminar.grid(row=5,column=1,padx=10,pady=10)
    botonSalirVentanaEliminar.place(relx=0.5,rely=0.9,anchor=CENTER)

def insertarLugar():
    ventanaInsertarLugar=Toplevel()
    ventanaInsertarLugar.title("Insertar lugar de donación")
    ventanaInsertarLugar.geometry("410x165")
    clave_var=StringVar()
    valor_var=StringVar()
    def insetarLugarNuevo():
        lista=["San José","Alajuela","Cartago","Heredia","Guanacaste","Puntarenas","Limón"]
        if not clave_var.get().capitalize() in lista:
            messagebox.showerror("Error al seleccionar provincia","Ha ingresado una pronvicia incorrecta.")
            clave_var.set("")
            valor_var.set("")
            return 
        if not valor_var.get():
            messagebox.showerror("Error al ingresar nuevo lugar","Debe ingresar un nuevo lugar.")
            clave_var.set("")
            valor_var.set("")
            return
        if agregarLugarDonacion(clave_var.get(),valor_var.get()):   
            messagebox.showinfo("Nuevo lugar agregado","Se ha agregado correctamente el nuevo lugar de donación.")
        else:
            messagebox.showerror("Error al insertar lugar","Este lugar ya está registrado en esta provincia.")
        clave_var.set("")
        valor_var.set("")
        return ""
    etiquetaProvincia=Label(ventanaInsertarLugar,text="Seleccione la provincia")
    etiquetaNuevoLugar=Label(ventanaInsertarLugar,text="Nuevo lugar de donación")

    listaProvincias=["San José","Alajuela","Cartago","Heredia","Guanacaste","Puntarenas","Limón"]
    provincias=ttk.Combobox(ventanaInsertarLugar,textvariable=clave_var,values=listaProvincias)
    entradaLugarNuevo=Entry(ventanaInsertarLugar,textvariable=valor_var,width=21,bd=5)
    botonInsertarNuevoLugar=Button(ventanaInsertarLugar,text="Insertar",width=8,command=insetarLugarNuevo)
    botonSalirVentanaInsertarLugar=Button(ventanaInsertarLugar,text="Salir",command=ventanaInsertarLugar.destroy)
    

    etiquetaProvincia.grid(row=0,column=0,padx=10,pady=10)
    provincias.grid(row=0,column=1,columnspan=4,padx=10,pady=10)
    etiquetaNuevoLugar.grid(row=1,column=0,padx=10,pady=10)
    entradaLugarNuevo.grid(row=1,column=1,columnspan=6,padx=10,pady=10)

    botonInsertarNuevoLugar.grid(row=2,column=1,columnspan=3,padx=10,pady=10)
    botonInsertarNuevoLugar.place(relx=0.5,rely=0.7,anchor=CENTER)
    botonSalirVentanaInsertarLugar.grid(row=3,column=1,columnspan=3,padx=10,pady=10)
    botonSalirVentanaInsertarLugar.place(relx=0.5,rely=0.9,anchor=CENTER)

def reportes():
    ventanaReportes=Toplevel()
    ventanaReportes.geometry("320x500")
    ventanaReportes.title("Reportes")
    def donadoresxProvincia():
        #DONADORES POR PROVINCIA
        ventanaDonadoresxProvincia=Toplevel()
        ventanaDonadoresxProvincia.title("Reporte: Donadores por provincia")
        provinciaSeleccionada=StringVar()
        lista=["San José","Alajuela","Cartago","Heredia","Guanacaste","Puntarenas","Limón"]

        def validarProvinciaSeleccionada():
            lista=["San José","Alajuela","Cartago","Heredia","Guanacaste","Puntarenas","Limón"]
            if provinciaSeleccionada.get() in lista:#Si escogió una opción del desplegable.
                if generarReporte(provinciaSeleccionada.get()):
                    messagebox.showinfo("Reporte generado","Reporte generado correctamente.")
                else:
                    messagebox.showerror("Error al crear reporte","No se ha creado reporte.")
            else:
                messagebox.showerror("Error al seleccionar provincia","Debe seleccionar una provincia válida.")
            provinciaSeleccionada.set("")
            return 
        etiquetaDonadores=Label(ventanaDonadoresxProvincia,text="Seleccione una provincia")
        provincia=ttk.Combobox(ventanaDonadoresxProvincia,textvariable=provinciaSeleccionada,values=lista)
        botonReporte=Button(ventanaDonadoresxProvincia,text="Generar reporte",command=validarProvinciaSeleccionada)

        botonSalirDonadoresxPronvcia=Button(ventanaDonadoresxProvincia,text="Regresar",command=ventanaDonadoresxProvincia.destroy)

        etiquetaDonadores.grid(row=0,column=1,padx=10,pady=10)
        provincia.grid(row=1,column=1,columnspan=3,padx=10,pady=10)
        botonReporte.grid(row=2,column=1,columnspan=2,padx=10,pady=10)

        botonSalirDonadoresxPronvcia.grid(row=4,column=2,padx=10,pady=10)
        return
    def rangoEdad():
        #DONADORES POR RANGO DE EDAD.
        ventanaDonadoresxProvincia=Toplevel()
        ventanaDonadoresxProvincia.title("Reporte: Donadores por rango de edad")
        inicio_var=StringVar()
        fin_var=StringVar()
        def validarInicioFin():
            if not inicio_var.get():#debe tener fecha de incicio obligatoriamente.
                messagebox.showerror("Error al ingresar rango","Debe ingresar una edad de inicio.")
                inicio_var.set("")
                fin_var.set("")
                return
            #no tiene sentido decir reporte NO creado cuando haya algo malo porque antes de mandar a 
            #hacer el reporte se valida y muestra un error.
            validado=validarInicioMayorFin(inicio_var.get(),fin_var.get())#manda a validar las edades.
            if validado[0]:#obtiene True|False de la validación
                if validado[1]==1:#saca el valor 1 de la tupla, 1. Es solo inicio, 2. inicio y fin.
                    revisarRango(inicio_var.get(),fin_var.get())#manda a hacer el reporte.
                else:
                    revisarRango(inicio_var.get(),fin_var.get())
                messagebox.showinfo("Reporte generado","Reporte creado satisfactoriamente.")  
            else:
                messagebox.showerror("Error al ingresar fecha","Rango inválido.")
            inicio_var.set("")
            fin_var.set("")
            return

        etiquetaRangoEdad=Label(ventanaDonadoresxProvincia,text="Ingresar rango")
        etiquetaInicio=Label(ventanaDonadoresxProvincia,text="Edad inicial")
        etiquetaFin=Label(ventanaDonadoresxProvincia,text="Edad final")

        entradaInicio=Entry(ventanaDonadoresxProvincia,textvariable=inicio_var)
        entradaFin=Entry(ventanaDonadoresxProvincia,textvariable=fin_var)

        botonGenerar=Button(ventanaDonadoresxProvincia,text="Generar",command=validarInicioFin)
        botonSalirDonadoresxProvincia=Button(ventanaDonadoresxProvincia,text="Regresar",command=ventanaDonadoresxProvincia.destroy)

        etiquetaRangoEdad.grid(row=0,column=1,padx=10,pady=10)
        etiquetaInicio.grid(row=1,column=0,padx=10,pady=10)
        etiquetaFin.grid(row=2,column=0,padx=10,pady=10)
        entradaInicio.grid(row=1,column=1,columnspan=3,padx=10,pady=10)
        entradaFin.grid(row=2,column=1,columnspan=3,padx=10,pady=10)
        botonGenerar.grid(row=3,column=1,padx=10,pady=10)

        botonSalirDonadoresxProvincia.grid(row=5,column=1,columnspan=4,padx=10,pady=10)
        return 
    def tipoSangre():
        ventanaSangre=Toplevel()
        ventanaSangre.title("Reporte por tipo de sangre")
        ventanaSangre.geometry("420x100")
        ventanaSangre.resizable(width=False, height=False)
        sangreAlmacen=StringVar()
        
        sangreLabel=Label(ventanaSangre,text="Seleccione el tipo de sangre")
        opcionesSangre=ttk.Combobox(ventanaSangre,textvariable=sangreAlmacen,values=["O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-"])

        def validarTipoSangre():
            if sangreAlmacen.get() in ["O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-"]:
                if reporteTipodeSangre(sangreAlmacen.get()):
                    messagebox.showinfo("Reporte generado","Reporte creado satisfactoriamente.")
                    sangreAlmacen.set("")
                else:
                    messagebox.showinfo("Reporte no generado","Error al generar el reporte.")
                    sangreAlmacen.set("")
            else:
                messagebox.showerror("Reporte no generado","Seleccione una opción válida.")
                sangreAlmacen.set("")
        sangreLabel.grid(row=0,column=0,padx=8,pady=8)
        opcionesSangre.grid(row=0,column=1,padx=8,pady=8)
        generarBoton=Button(ventanaSangre,text="Generar Reporte",command=validarTipoSangre)
        salirBoton=Button(ventanaSangre,text="Salir",command=ventanaSangre.destroy)
        generarBoton.grid(row=1,column=1,padx=8,pady=8)
        salirBoton.grid(row=2,column=1,padx=8,pady=8)
        salirBoton.place(relx=0.5,rely=0.86,anchor=CENTER)
        generarBoton.place(relx=0.5,rely=0.57,anchor=CENTER)
    def totalDonadores():
        if reporteTodo():
            messagebox.showinfo("Reporte generado","Reporte generado correctamente.")
        else:
            messagebox.showerror("Reporte no generado","Error al generar el reporte.")
    def mujerO():
        if mujeresDonantesO():
            messagebox.showinfo("Reporte generado","Reporte generado correctamente.")
        else:
            messagebox.showerror("Reporte no generado","Error al generar el reporte.")
    #ULTIMO REPORTE DONADORES NO ACTIVOS.
    def donadoresNOactivos():
        if reporteDonadoreNOactivos():
            messagebox.showinfo("Reporte generado","Reporte generado correctamente.")
        else:
            messagebox.showerror("Reporte no generado","Reporte no creado.")
        return 

    etiquetaDonadoresActivos=Label(ventanaReportes,text="Donadores activos")

    botonDonantesProvincia=Button(ventanaReportes,text="Donantes por provincia",command=donadoresxProvincia)
    botonRangoEdad=Button(ventanaReportes,text="Rango de edad",command=rangoEdad)
    botonTipoSangre=Button(ventanaReportes,text="Tipo de sangre",command=tipoSangre)
    botonListaCompleta=Button(ventanaReportes,text="Lista completa de donadores",command=totalDonadores)
    botonMujeresO=Button(ventanaReportes,text="Mujeres donantes O-",command=mujerO)
    botonDonar=Button(ventanaReportes,text="¿A quién le puedo donar?")
    botonRecibir=Button(ventanaReportes,text="¿De quién puedo recibir?")

    etiquetaDonadoresNoActivos=Label(ventanaReportes,text="Donadores NO activos")
    botonDonadoresNoActivos=Button(ventanaReportes,text="Donantes NO activos",command=donadoresNOactivos)

    botonSalirReportes=Button(ventanaReportes,text="Regresar",command=ventanaReportes.destroy)

    etiquetaDonadoresActivos.grid(row=0,column=3,padx=10,pady=10)

    botonDonantesProvincia.grid(row=1,column=3,padx=10,pady=10)
    botonRangoEdad.grid(row=2,column=3,padx=10,pady=10)
    botonTipoSangre.grid(row=3,column=3,padx=10,pady=10)
    botonListaCompleta.grid(row=4,column=3,padx=10,pady=10)
    botonMujeresO.grid(row=5,column=3,padx=10,pady=10)
    botonDonar.grid(row=6,column=3,padx=10,pady=10)
    botonRecibir.grid(row=7,column=3,padx=10,pady=10)

    etiquetaDonadoresNoActivos.grid(row=8,column=3,padx=10,pady=10)
    botonDonadoresNoActivos.grid(row=9,column=3,padx=10,pady=10)

    botonSalirReportes.grid(row=10,column=2,padx=10,pady=10)

def menu():#NO TOCAR, YA ESTÁ LISTO.
    principal=Tk()#menu principal
    principal.title("Donadores de Sangre Costa Rica")
    principal.geometry("700x740")#le da tamaño a la ventana principal
    principal.config(bg="OrangeRed3")
    principal.resizable(width=False, height=False)#NO QUITAR PARA QUE NO ESTEN TOCANDO EL TAMAÑO.
    imagen=PhotoImage(file='donacion(1).png')
    imagen_label=Label(principal,image=imagen)
    imagen_label.grid(row=8,column=1,padx=10,pady=10)
    imagen_label.place(relx=0.5, rely=0.29, anchor=CENTER)
    #1. Insertar donador
    botonInsertar=Button(principal,text="Insertar Donadores",font=("BiauKai","21", "bold"),width=43,command=insertar)
    botonInsertar.grid(row=0,column=1,padx=10,pady=10)
    botonInsertar.place(relx=0.5, rely=0.61, anchor=CENTER)
    #Llama a la función generar.
    botonGenerar=Button(principal,text="Generar Donadores",font=("BiauKai","21", "bold"),command=generar,width=43)
    botonGenerar.grid(row=0,column=1,padx=10,pady=10)
    botonGenerar.place(relx=0.5, rely=0.67, anchor=CENTER)
    #Llama a la función actualizar.
    botonActualizar=Button(principal,text="Actualizar Datos Del Donador",font=("BiauKai","21", "bold"),width=43,command=actualizar)
    botonActualizar.grid(row=2,column=1,padx=10,pady=10)
    botonActualizar.place(relx=0.5, rely=0.73, anchor=CENTER)
    #Llama a la función eliminar.
    botonEliminar=Button(principal,text="Eliminar Donador",font=("BiauKai","21", "bold"),width=43,command=eliminar)
    botonEliminar.grid(row=3,column=1,padx=10,pady=10)
    botonEliminar.place(relx=0.5, rely=0.79, anchor=CENTER)
    #Llama a la función insertar lugar.
    botonInsertarLugar=Button(principal,text="Insertar Lugar de Donación Según Provincia",font=("BiauKai","21", "bold"),width=43,command=insertarLugar)
    botonInsertarLugar.grid(row=4,column=1,padx=10,pady=10)
    botonInsertarLugar.place(relx=0.5, rely=0.85, anchor=CENTER)
    #Llama a la función reporte.
    botonReportes=Button(principal,text="Reportes",font=("BiauKai","21", "bold"),width=43,command=reportes)
    botonReportes.grid(row=5,column=1,padx=10,pady=10)
    botonReportes.place(relx=0.5, rely=0.91, anchor=CENTER)
    #Llama a la función salir
    botonSalir=Button(principal,text="Salir",font=("BiauKai","21", "bold"),width=43,command=quit)
    botonSalir.grid(row=7,column=1,padx=10,pady=10)#termina la ventana
    botonSalir.place(relx=0.5, rely=0.97, anchor=CENTER)
    principal.mainloop()
menu()