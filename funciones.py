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
fechaNacimiento = '08/05/2003'
fecha_dt = str(datetime.strptime(fechaNacimiento, '%d/%m/%Y'))#cambia fecha a tipo date.
annoNacimiento=int(fecha_dt[0:4])#pasa el año a int para restarlo.
today = str(date.today())#pasa la fecha actual a str.
annoActual=int(today[0:4])#pasa el año actual a int para restar.
if annoActual-annoNacimiento==18:#esta el año de nacimiento al actual para saber si este año cumple los 18. falta el mes.
    mesNacimiento=int(str(fecha_dt[5:7]))#saca el mes de nacimiento
    mesActual=int(today[5:7])#saca el mes actual
    print(mesNacimiento,mesActual)
    if mesNacimiento==mesActual:
        diaNacimiento=int(str(fecha_dt[8:11]))#saca el dia de nacimiento y lo pasa a int
        diaActual=int(str(today[8:11]))#saca el dia actual y los pasa a int.
        print("dia",diaNacimiento,"dia",diaActual)
        if diaNacimiento<=diaActual:#si el dia actual es menor o igual al actual si es mayor.
            print("Si es mayor de edad")
        else:
            print("Aún no ha cumplido años por el dia.")
    elif mesNacimiento<mesActual:
        print("Si es mayor de edad.")
    else:
        print("Aún no ha cumplido años por el mes.")
    pass
elif annoActual-annoNacimiento>18: 
    print("Si es mayor de edad")
else:
    print("No es mayor de edad")