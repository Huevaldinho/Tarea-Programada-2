#Este código es para la selección de provincia, la misma lógica sirve para seleccionar el sexo y la justificación.
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
# Configuración de la raíz
root = Tk()
opcion = IntVar()
Radiobutton(root, text="1. San José", variable=opcion, 
            value=1, command=seleccionar).pack()
Radiobutton(root, text="2. Alajuela", variable=opcion, 
            value=2, command=seleccionar).pack()
Radiobutton(root, text="3. Cartago", variable=opcion,   
            value=3, command=seleccionar).pack()
Radiobutton(root, text="4. Cartago", variable=opcion,   
            value=4, command=seleccionar).pack()
Radiobutton(root, text="5. Guanacaste", variable=opcion,   
            value=5, command=seleccionar).pack()
Radiobutton(root, text="6. Puntarenas", variable=opcion,   
            value=6, command=seleccionar).pack()
Radiobutton(root, text="7. Limón.¿", variable=opcion,   
            value=7, command=seleccionar).pack()
Radiobutton(root, text="8. Nacionalizado o naturalizado", variable=opcion,   
            value=8, command=seleccionar).pack()
Radiobutton(root, text="9. Caso especial", variable=opcion,   
            value=9, command=seleccionar).pack()
monitor = Label(root)
monitor.pack()
print(root)
# Finalmente bucle de la aplicación
root.mainloop()



###################################################################################################################
#
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


