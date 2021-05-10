#prueba conexión con base de datos local.
#import mysql.connector
#cnn=mysql.connector.connect(host="localhost",user="root",passwd="",database="prueba")
#print(cnn)#se conecta a la base de datos.



####################
#VALIDACIONES
####################
import re
from datetime import date
from datetime import datetime
def solicitarCedula():
    cedula=input("Ingrese número de cédula: ")
    return cedula
def validarCedula(cedula):
    """
    Función: Validar número de cédula con formato #-####-####.
    Entrada:
    -cedula(str): Número de cédula costarricense.
    Salida:
    -True: Si la cédula es válida.
    -False: La cédula no es válida.
    """
    if re.match("^[1-9]{1}[-]{1}[0-9]{4}[-]{1}[0-9]{4}$",cedula):
        return True
    else:
        return False
#07/05/2021 2:00 pm / 5 minutos haciendose.
def validarNombreCompleto(nombre): #NO HAY QUE HACER FUNCION DE ENTRADA, ENTRA EN TKINTER
    if re.match('[A-Za-z]{2,25}( [A-Za-z]{2,25}){2}',nombre):
        return True
    return False
def validarFecha(fecha):
    """
    Función: Validar fecha y formato.
    Entrada:
    -fecha(str): Fecha a validar.
    Salida:
    -True: Si está bien.
    -False: Si no está bien.
    """
    try:
        datetime.strptime(fecha, '%d/%m/%Y')#valida usando libreria. además sabe los años bisiestos
        print("Fecha válida")
        return True
    except ValueError:
        print("Fecha inválida")
        return False
#07/05/2021 2:05 pm / 10 minutos haciendose.
def validarCorreo(correo):
    """
    Funcion: Validar que el correo tenga nombre de dominio: ccss o racsa o costarricense o gmail.
    Entrada:
    -correo(str): Correo que se va a revisar si es válido o no.
    Salida:
    -True(bool): Es válido.
    -False(bool): Es inválido.
    """
    correo=correo.lower()
    if re.match("^([a-z0-9_\.-]+)@(ccss|racsa|costarricense|gmail)\.([a-z\.]{2,6})$",correo):
        print("Correo ingresado satisfactoriamente")
        return True
    else:
        print("Correo invalido.")
        return False 
#07/05/2021 2:25 pm / 30 minutos
def validarTelefono(telefono):
    """
    Función: Validar telefono personal o de hogar en Costa Rica.
    Entrada:
    -telefono(str): Telefono a validar.
    Salida:
    -True: Si es válido.
    -False: Si no es válido.
    """
    if re.match("^(2|6|7|8){1}[0-9]{3}[\-]{1}[0-9]{4}$",telefono):
        print("Telefono ingresado satisfactoriamente.")
        return True
    else:
        print("Telefono inválido.")
        return False
#07/05/2021 2:55 pm / 5 minutos.
def validarPeso(peso):
    """
    #SEGÚN LA OMS DEBE SER >50kg.
    Función: Validar si una persona puede donar sangre según su peso.
    Entrada: 
    -peso(int): Peso de la persona
    Salida:
    -True: Si puede donar.
    -False: Si no puede donar.
    """
    if peso<50:
        print("Bajo peso")
        return False
    print("Peso ingresado correctamente.")
    return True

#Falta meter en función que reciba fecha de nacimiento CORREGIR
from datetime import *
def validarMayorEdad(fechaNacimiento):
    """
    Función: Determinar si una persona es mayor de edad según su fecha de nacimiento (dd/mm/aaaa).
    Entrada:
    -fechaNacimiento(str): Fecha de nacimiento con  formato dd/mm/aaaa
    Salida:
    -True(bool): Si es mayor de edad.
    -False(bool): Si no es mayor de edad.
    """
    fecha_dt = str(datetime.strptime(fechaNacimiento, '%d/%m/%Y'))#cambia fecha a tipo date.
    annoNacimiento=int(fecha_dt[0:4])#pasa el año a int para restarlo.
    today = str(date.today())#pasa la fecha actual a str.
    annoActual=int(today[0:4])#pasa el año actual a int para restar.
    if annoActual-annoNacimiento==18:#esta el año de nacimiento al actual para saber si este año cumple los 18. falta el mes.
        mesNacimiento=int(str(fecha_dt[5:7]))#saca el mes de nacimiento
        mesActual=int(today[5:7])#saca el mes actual
        if mesNacimiento==mesActual:
            diaNacimiento=int(str(fecha_dt[8:11]))#saca el dia de nacimiento y lo pasa a int
            diaActual=int(str(today[8:11]))#saca el dia actual y los pasa a int.
            if diaNacimiento<=diaActual:#si el dia actual es menor o igual al actual si es mayor.
                return True
            else:
                return False
        elif mesNacimiento<mesActual:
            return True
        else:
            return False
        pass
    elif annoActual-annoNacimiento>18: 
        return True
    else:
        return False
def provinciaYlugarDeDonacion(cedula): #Punto 1.1
    provincia=[["1","San José"],["2","Alajuela"],["3","Cartago"],["4","Heredia"],["5","Guanacaste"],["6","Puntarenas"],["7","Limón"]]
    lugares={"San José":["El Banco Nacional de sangre", "Hospital México","Hospital San Juan de Dios"],"Alajuela":["Hospital San Rafael de Alajuela","Hospital de \
San Ramón", "Hospital del Cantón Norteño"],"Cartago":["Hospital Max Peralta"],"Heredia":["Hospital San Vicente de Paúl"],"Guanacaste":["Hospital La \
Anexión en Nicoya", "Hospital Enrique Baltodano de Liberia."],"Puntarenas":["Hospital Monseñor Sanabria"],"Limón":["Hospital Tony Facio","Hospital de \
Guápiles"]}
    lugarAsignado=None #para los que son cedula 8 y 9
    for sublista in provincia: #recorre la lista
        if str(cedula)[0]==sublista[0]:
            lugarAsignado=sublista[1]
    if lugarAsignado==None:
        lugarAsignado="San José"
    return "Dado que usted nació en la provincia de: "+lugarAsignado+" usted podría donar en: \n"+"\n".join(lugares[lugarAsignado])
    
#07/05/2021 / 1 hora.
import pickle
def graba(nombreArchivo,listaDic):
    try:
        f=open(nombreArchivo,"wb")
        pickle.dump(listaDic,f)
        f.close()
    except:
        print("Error al grabar el archivo: ", nombreArchivo)
    return
#Función que lee un archivo con una lista de estudiantes
def lee (nomArchLeer):
    try:
        f=open(nomArchLeer,"rb")
        lista = pickle.load(f)
        f.close()
    except:
        print("Error al leer el archivo: ", nomArchLeer)
    return lista


#######################
#######################
#4.ELIMINAR DONADOR
#######################
#######################
def eliminarDonador(donadores):
    """
    Función: Eliminar donador.
    Entrada:
    -listaDic(dic): Lista con diccionarios de cada usuario.
    Salida: N/A.
    """
    while True:
        cedula=solicitarCedula()#manda a pedir la cédula en interfaz gráfica
        if validarCedula(cedula):#manda a validar la cédula
            if cedula in donadores:#si la persona no está registrada
                #pedir justificación en interfaz gráfica.
                if donadores[cedula]["estado"]==0:
                    print("El usuario ya está inactivo")
                    return ""
                justi="algo"#solo para ver como actualizamos datos.
                donadores[cedula]["estado"]=0#cambia el estado a inactivo.
                donadores[cedula]["justificacion"]=justi#pone la justificación seleccionada en la interfaz gráfica.
            else:#no está en la base de datos.
                # esto se debe mostar en interfaz gráfica.
                print("La persona con el número de cédula:",cedula, "no está registrado en la base de datos del Banco de Sangre aún")
                return ""
            break
    print(donadores)
    graba("donadores",donadores)
    print("Usuario eliminado safisfactoriamente.")#debe mostrarse en la interfaz
    #debe regresar al menu
    return ""
personas=lee("donadores")#trae el diccionario de personas
eliminarDonador(personas)#llama a eliminar con el diccionario de personas