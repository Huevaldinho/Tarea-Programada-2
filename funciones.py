#prueba conexión con base de datos local.
import mysql.connector
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
    -cedula(int): Número de cédula costarricense.
    Salida:
    -True: Si la cédula es válida.
    -False: La cédula no es válida.
    """
    if re.match("^[1-9]{1}[-]{1}[0-9]{4}[-]{1}[0-9]{4}$",cedula):
        return True
    else:
        return False
#07/05/2021 2:00 pm / 5 minutos haciendose.
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
    dicc={}
    try:
        f=open(nomArchLeer,"rb")
        dicc = pickle.load(f)
        f.close()
    except:
        print("Error al leer el archivo: ", nomArchLeer)
    return dicc


#######################
#######################
#4.ELIMINAR DONADOR
#######################
#######################
def eliminarDonador(listaDic):
    """
    Función: Eliminar donador.
    Entrada:
    -listaDic(dic): Lista con diccionarios de cada usuario.
    Salida: N/A.
    """
    while True:
        cedula=solicitarCedula()#manda a pedir la cédula
        if validarCedula(cedula):#manda a validar la cédula
            for persona in range(len(listaDic)):#para revisar la cédula esta en lista.
                usuarioCedula=listaDic[persona]#saca el usuario(diccionario)
                if usuarioCedula["cedula"]==cedula:#si la cédula del usuario está registrada.
                    posicion=persona
                    if usuarioCedula["estado"]==0:#si la persona ya está inactiva.
                        print("Este usuario ya se encuentra inactivo")
                        return #se sale porque ya está inactivo.
                    break#salgase, ya encontró la cédula
                if usuarioCedula["cedula"]!=cedula and persona==len(listaDic)-1:
                    print("Esa cédula aún no se ha registrada.")
                    return ""
            justi="ALGO"#parte de la interfaz
            usuarioCedula=listaDic[posicion]#saca la posición de la persona en la lista
            usuarioCedula["estado"]=0#cambia el estado a inactivo
            usuarioCedula["justificaion"]=justi#le agrega la justificación.
            graba("donadores",listaDic)
            print("Usuario eliminado safisfactoriamente.")#debe mostrarse en la interfaz
            #debe regresar al menu
            break
        else:
            print("Cédula inválida")
            continue
    return ""
print("Lista en disco duro:",lee("donadores"))
listaDonadores=[{"cedula": "9-0139-0105", "estado": 0},{"cedula": "2-5432-2222", "estado": 0},
{"cedula": "8-6456-5454", "estado": 0},{"cedula": "5-0246-0545", "estado": 1},
{"cedula": "1-2311-3412", "estado": 1},{"cedula": "3-0125-5745", "estado": 1}]
print("Lista en RAM, creada: ",listaDonadores)
eliminarDonador(listaDonadores)
#print(lee("donadores"))