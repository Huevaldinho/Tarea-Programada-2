#Elaborado por: Felipe Obando y Sebastián Bermúdez.
#Fecha elaboración: 06/05/2021 8:30 pm
#Última modificación: 24/05/2021 
#Versión: 3.9.2

#Importación de librerias.
from enum import auto
from os import pardir
from re import T
from tkinter import *
from tkinter import StringVar, ttk
from tkinter.constants import COMMAND
from tkinter import messagebox
from typing import Collection, Literal
from funciones import *

#Funciones para interfaz gráfica.
def insertar():
    """
    Función: Crear ventana para insertar un donador en la base de datos.
    Entrada: N/A.
    Salida: N/A.
    """
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
        """
        Función: Limpiar la ventana con datos.
        Entrada: N/A.
        Salida: N/A.
        """
        cedulaAlmacen.set("")
        nombreAlmacen.set("")
        fechaNacimientoAlmacen.set("")
        sangreAlmacen.set("")
        sexoAlmacen.set(False)
        pesoAlmacen.set(0)
        telefonoAlmacen.set("")
        correoAlmacen.set("")
    def validarTodo():
        """
        Función: Validar que los datos introducidos sean válidos.
        Entrada: N/A.
        Salida: N/A.
        """
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
    """
    Función: Crear ventana para generar lista de donadores.
    Entrada: N/A.
    Salida: N/A.
    """
    ventanaGenerar=Toplevel()
    ventanaGenerar.title("Generar Donadores")
    ventanaGenerar.geometry("370x100")
    ventanaGenerar.resizable(width=False, height=False)

    cuantosAlmacen=IntVar()

    cuantos_label=Label(ventanaGenerar,text="¿Cuántos donadores desea generar?")
    entrada=Entry(ventanaGenerar,textvariable=cuantosAlmacen,width=20,bd=5)

    cuantos_label.grid(row=0,column=0,padx=4,pady=7)
    entrada.grid(row=0,column=1,columnspan=2,padx=7,pady=7)

    def genera():
        """
        Función: Generar lista según tamaño solicitado
        Entrada: N/A.
        Salida: N/A.
        """
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
    """
    Función: Actualizar información de un donador.
    Entrada: N/A.
    Salida: N/A.
    """
    ventanaActualizar=Toplevel()
    ventanaActualizar.title("Actualizar Donadores")
    ventanaActualizar.geometry("270x110")
    ventanaActualizar.resizable(width=False, height=False)

    cedulaAlmacen=StringVar()

    cuantos_label=Label(ventanaActualizar,text="Cédula del donador")
    entrada=Entry(ventanaActualizar,textvariable=cedulaAlmacen,width=20,bd=5)
    cuantos_label.grid(row=0,column=0,padx=4,pady=7)
    entrada.grid(row=0,column=1,columnspan=2,padx=7,pady=7)

    def verificarActualizacion():
        """
        Función: Actualizar información de un donador.
        Entrada: N/A.
        Salida: N/A.
        """
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
                        """
                        Función:Limpiar datos en ventana.
                        Entrada: N/A.
                        Salida: N/A.
                        """
                        nombreAlmacen.set("")
                        fechaNacimientoAlmacen.set("")
                        sangreAlmacen.set("")
                        sexoAlmacen.set(False)
                        pesoAlmacen.set(0)
                        telefonoAlmacen.set("")
                        correoAlmacen.set("")
                    
                    def verificarActualizacionValido():
                        """
                        Función: Valida la información que se tiene desea actualizar.
                        Entrada: N/A.
                        Salida: N/A.
                        """
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
    botonSalirVentanaActualizar.grid(row=5,column=5,padx=10,pady=10)
    botonSalirVentanaActualizar.grid(row=2,column=0,padx=10,pady=10)
    botonSalirVentanaActualizar.place(relx=0.5,rely=0.86,anchor=CENTER)
def eliminar():
    """
    Función: Crear ventana para eliminar un donador.
    Entrada: N/A.
    Salida: N/A.
    """
    ventanaEliminar=Toplevel()
    ventanaEliminar.geometry("500x170")
    ventanaEliminar.resizable(width=False, height=False)
    ventanaEliminar.title("Eliminar Donadores")
    cedula_var=StringVar()
    justi=StringVar()

    def validarJustificacion():
        """
        Función: Valida que se seleccione una opción correcta.
        Entrada: N/A.
        Salida: N/A.
        """
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
    
    cedula_entry = Entry(ventanaEliminar,textvariable = cedula_var,width=52,bd=5)#entrada
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
    """
    Función: Crear ventna para insertar lugar de votación en una provincia.
    Entrada: N/A.
    Salida: N/A.
    """
    ventanaInsertarLugar=Toplevel()
    ventanaInsertarLugar.title("Insertar lugar de donación")
    ventanaInsertarLugar.geometry("345x165")
    clave_var=StringVar()
    valor_var=StringVar()
    def insetarLugarNuevo():
        """
        Función: Ingresar el nuevo lugar de donación.
        Entrada: N/A.
        Salida: N/A.
        """
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

def reportes():#Reportes.
    """
    Función: Crear ventana para reportes de donadores.
    Entrada: N/A.
    Salida: N/A.
    """
    ventanaReportes=Toplevel()
    ventanaReportes.geometry("540x500")
    ventanaReportes.title("Reportes")
    ventanaReportes.resizable(width=False, height=False)
    def donadoresxProvincia():#1. Donadores por provincia.
        """
        Función: Crear reporete de donador por provincia.
        Entrada: N/A.
        Salida: N/A.
        """
        ventanaDonadoresxProvincia=Toplevel()
        ventanaDonadoresxProvincia.title("Reporte: Donadores por provincia")
        provinciaSeleccionada=StringVar()
        lista=["San José","Alajuela","Cartago","Heredia","Guanacaste","Puntarenas","Limón"]
        def validarProvinciaSeleccionada():
            """
            Función: Validar que se seleccione una provincia válida.
            Entrada: N/A.
            Salida: N/A.
            """
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
    def rangoEdad():#Por rango de edad.
        """
        Función: Crear reporte por rango de edad.
        Entrada: N/A.
        Salida: N/A.
        """
        ventanaDonadoresxProvincia=Toplevel()
        ventanaDonadoresxProvincia.title("Reporte: Donadores por rango de edad")
        inicio_var=StringVar()
        fin_var=StringVar()
        def validarInicioFin():
            """
            Función: Validar que se ingrese un inicio en la interfaz gráfica.
            Entrada: N/A.
            Salida: N/A.
            """
            if not inicio_var.get():#debe tener fecha de incicio obligatoriamente.
                messagebox.showerror("Error al ingresar rango","Debe ingresar una edad de inicio.")
                inicio_var.set("")
                fin_var.set("")
                return
            validado=validarInicioMayorFin(inicio_var.get(),fin_var.get())#manda a validar las edades.
            if validado==False:
                inicio_var.set("")
                fin_var.set("")
                messagebox.showerror("Error al ingresar fecha","Rango inválido.")
                return
            if validado[0]:#obtiene True|False de la validación
                print(validado[0])
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
        etiquetaRangoEdad=Label(ventanaDonadoresxProvincia,text="Ingrese el rango de edad deseado")
        etiquetaInicio=Label(ventanaDonadoresxProvincia,text="Edad inicial")
        etiquetaFin=Label(ventanaDonadoresxProvincia,text="Edad final")

        entradaInicio=Entry(ventanaDonadoresxProvincia,textvariable=inicio_var,bd=5)
        entradaFin=Entry(ventanaDonadoresxProvincia,textvariable=fin_var,bd=5)

        botonGenerar=Button(ventanaDonadoresxProvincia,text="Generar",command=validarInicioFin)
        botonSalirDonadoresxProvincia=Button(ventanaDonadoresxProvincia,text="Regresar",command=ventanaDonadoresxProvincia.destroy)

        etiquetaRangoEdad.grid(row=0,column=1,padx=10,pady=10)
        etiquetaInicio.grid(row=1,column=0,padx=10,pady=10)
        etiquetaFin.grid(row=2,column=0,padx=10,pady=10)
        entradaInicio.grid(row=1,column=1,columnspan=3,padx=10,pady=10)
        entradaFin.grid(row=2,column=1,columnspan=3,padx=10,pady=10)
        botonGenerar.grid(row=3,column=1,padx=10,pady=10)
        botonSalirDonadoresxProvincia.grid(row=4,column=1,padx=10,pady=10)
        return 
    def tipoSangre():
        """
        Función: Crear reporte por tipo de sangre seleccionada.
        Entrada: N/A.
        Salida: N/A.
        """
        ventanaSangre=Toplevel()
        ventanaSangre.title("Reporte por tipo de sangre")
        ventanaSangre.geometry("420x100")
        ventanaSangre.resizable(width=False, height=False)
        sangreAlmacen=StringVar()
        
        sangreLabel=Label(ventanaSangre,text="Seleccione el tipo de sangre")
        opcionesSangre=ttk.Combobox(ventanaSangre,textvariable=sangreAlmacen,values=["O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-"])

        def validarTipoSangre():
            """
            Función: Validar que se seleccione un tipo de sangre.
            Entrada: N/A.
            Salida: N/A.
            """
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
        """
        Función: Crear ventana de todos los donadores activos.
        Entrada: N/A.
        Salida: N/A.
        """
        if reporteTodo():
            messagebox.showinfo("Reporte generado","Reporte generado correctamente.")
        else:
            messagebox.showerror("Reporte no generado","Error al generar el reporte.")
    def mujerO():
        """
        Función: Crear reporte de mujeres con tipo de sangre O-.
        Entrada: N/A.
        Salida: N/A.
        """
        if mujeresDonantesO():
            messagebox.showinfo("Reporte generado","Reporte generado correctamente.")
        else:
            messagebox.showerror("Reporte no generado","Error al generar el reporte.")
    def aQuienPuedeDonar():
        """
        Función: Crear reporte de posibles receptores según tipo de sangre.
        Entrada: N/A.
        Salida: N/A.
        """
        ventanaAquienDonar=Toplevel()
        ventanaAquienDonar.title("¿A quién puede donar?")
        ventanaAquienDonar.geometry("420x100")
        ventanaAquienDonar.resizable(width=False, height=False)
        sangreAlmacen=StringVar()
        
        sangreLabel=Label(ventanaAquienDonar,text="Seleccione el tipo de sangre")
        opcionesSangre=ttk.Combobox(ventanaAquienDonar,textvariable=sangreAlmacen,values=["O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-"])

        def validarAquienDonar():
            """
            Función: Validar que se ingrese un tipo de sangre correcto.
            Entrada: N/A.
            Salida: N/A.
            """
            if sangreAlmacen.get() in ["O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-"]:
                if quienDonar(sangreAlmacen.get()):
                    messagebox.showinfo("Reporte generado","Reporte de los recibidores posibles del tipo "+sangreAlmacen.get()+" creado satisfactoriamente.")
                    sangreAlmacen.set("")
                else:
                    messagebox.showinfo("Reporte no generado","Error al generar el reporte.")
                    sangreAlmacen.set("")
            else:
                messagebox.showerror("Reporte no generado","Seleccione una opción válida.")
                sangreAlmacen.set("")
        sangreLabel.grid(row=0,column=0,padx=8,pady=8)
        opcionesSangre.grid(row=0,column=1,padx=8,pady=8)
        generarBoton=Button(ventanaAquienDonar,text="Generar Reporte",command=validarAquienDonar)
        salirBoton=Button(ventanaAquienDonar,text="Salir",command=ventanaAquienDonar.destroy)
        generarBoton.grid(row=1,column=1,padx=8,pady=8)
        salirBoton.grid(row=2,column=1,padx=8,pady=8)
        salirBoton.place(relx=0.5,rely=0.86,anchor=CENTER)
        generarBoton.place(relx=0.5,rely=0.57,anchor=CENTER)

    def deQuienPuedeRecibir():
        """
        Función: Crear reporte de posibles donadores de los cuales puedo recibir sangre.
        Entrada: N/A.
        Salida: N/A.
        """
        ventanaDeQuienRecibir=Toplevel()
        ventanaDeQuienRecibir.title("¿De quién puede recibir?")
        ventanaDeQuienRecibir.geometry("420x100")
        ventanaDeQuienRecibir.resizable(width=False, height=False)
        sangreAlmacen=StringVar()
        
        sangreLabel=Label(ventanaDeQuienRecibir,text="Seleccione el tipo de sangre")
        opcionesSangre=ttk.Combobox(ventanaDeQuienRecibir,textvariable=sangreAlmacen,values=["O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-"])

        def validarDeQuienRecibir():
            """
            Función: Validar que se ingrese un tipo de sangre correcto.
            Entrada: N/A.
            Salida: N/A.
            """
            if sangreAlmacen.get() in ["O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-"]:
                if quienRecibir(sangreAlmacen.get()):
                    messagebox.showinfo("Reporte generado","Reporte de los donadores posibles para el tipo "+sangreAlmacen.get()+" creado satisfactoriamente.")
                    sangreAlmacen.set("")
                else:
                    messagebox.showinfo("Reporte no generado","Error al generar el reporte.")
                    sangreAlmacen.set("")
            else:
                messagebox.showerror("Reporte no generado","Seleccione una opción válida.")
                sangreAlmacen.set("")
        sangreLabel.grid(row=0,column=0,padx=8,pady=8)
        opcionesSangre.grid(row=0,column=1,padx=8,pady=8)
        generarBoton=Button(ventanaDeQuienRecibir,text="Generar Reporte",command=validarDeQuienRecibir)
        salirBoton=Button(ventanaDeQuienRecibir,text="Salir",command=ventanaDeQuienRecibir.destroy)
        generarBoton.grid(row=1,column=1,padx=8,pady=8)
        salirBoton.grid(row=2,column=1,padx=8,pady=8)
        salirBoton.place(relx=0.5,rely=0.86,anchor=CENTER)
        generarBoton.place(relx=0.5,rely=0.57,anchor=CENTER)
    def donadoresNOactivos():
        """
        Función: Crear reporte de donadores no activos.
        Entrada: N/A.
        Salida: N/A.
        """
        if reporteDonadoreNOactivos():
            messagebox.showinfo("Reporte generado","Reporte generado correctamente.")
        else:
            messagebox.showerror("Reporte generado","Reporte no creado.")
        return 

    etiquetaDonadoresActivos=Label(ventanaReportes,text="Reporte de Donadores",font=("BiauKai","21","bold"))

    botonDonantesProvincia=Button(ventanaReportes,text="Donantes por provincia",command=donadoresxProvincia,font=("BiauKai","16"),height=3, width=20)
    botonRangoEdad=Button(ventanaReportes,text="Rango de edad",command=rangoEdad,font=("BiauKai","16"),height=3, width=20)
    botonTipoSangre=Button(ventanaReportes,text="Tipo de sangre",command=tipoSangre,font=("BiauKai","16"),height=3, width=20)
    botonListaCompleta=Button(ventanaReportes,text="Lista completa de donadores",command=totalDonadores,font=("BiauKai","16"),height=3, width=20)
    botonMujeresO=Button(ventanaReportes,text="Mujeres donantes O-",command=mujerO,font=("BiauKai","16"),height=3, width=20)
    botonDonar=Button(ventanaReportes,text="¿A quién le puedo donar?",command=aQuienPuedeDonar,font=("BiauKai","16"),height=3, width=20)
    botonRecibir=Button(ventanaReportes,text="¿De quién puedo recibir?",command=deQuienPuedeRecibir,font=("BiauKai","16"),height=3, width=20)
    botonDonadoresNoActivos=Button(ventanaReportes,text="Donantes NO activos",command=donadoresNOactivos,font=("BiauKai","16"),height=3, width=20)

    botonSalirReportes=Button(ventanaReportes,text="Regresar",command=ventanaReportes.destroy)

    etiquetaDonadoresActivos.grid(row=0,columnspan=2,rowspan=2,column=1)
    etiquetaDonadoresActivos.place(relx=0.5,rely=0.07,anchor=CENTER)
    botonDonantesProvincia.grid(row=2,column=0,padx=10,pady=10)
    botonDonantesProvincia.place(relx=0.25,rely=0.20,anchor=CENTER)
    botonRangoEdad.grid(row=3,column=0,padx=10,pady=10)
    botonRangoEdad.place(relx=0.25,rely=0.40,anchor=CENTER)
    botonTipoSangre.grid(row=4,column=0,padx=10,pady=10)
    botonTipoSangre.place(relx=0.25,rely=0.60,anchor=CENTER)
    botonListaCompleta.grid(row=5,column=0,padx=10,pady=10)
    botonListaCompleta.place(relx=0.25,rely=0.80,anchor=CENTER)
    botonMujeresO.grid(row=2,column=1,padx=10,pady=10)
    botonMujeresO.place(relx=0.75,rely=0.20,anchor=CENTER)
    botonDonar.grid(row=3,column=1,padx=10,pady=10)
    botonDonar.place(relx=0.75,rely=0.40,anchor=CENTER)
    botonRecibir.grid(row=4,column=1,padx=10,pady=10)
    botonRecibir.place(relx=0.75,rely=0.60,anchor=CENTER)
    botonDonadoresNoActivos.grid(row=5,column=1,padx=10,pady=10)
    botonDonadoresNoActivos.place(relx=0.75,rely=0.80,anchor=CENTER)

    botonSalirReportes.grid(row=7,column=2,padx=10,pady=10)
    botonSalirReportes.place(relx=0.5,rely=0.93,anchor=CENTER)

def menu():
    """
    Función: Crear interfaz gráfica de menú.
    Entrada: N/A.
    Salida: N/A.
    """
    principal=Tk()#menu principal
    principal.title("Donadores de Sangre Costa Rica")
    principal.geometry("700x740")#le da tamaño a la ventana principal
    principal.config(bg="blue4")
    principal.resizable(width=False, height=False)
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