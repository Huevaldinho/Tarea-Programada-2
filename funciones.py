#prueba conexión con base de datos local.
#import mysql.connector
#cnn=mysql.connector.connect(host="localhost",user="root",passwd="",database="prueba")
#print(cnn)#se conecta a la base de datos.



####################
#VALIDACIONES
####################
import enum
import re
from datetime import *
import pickle
import random
import names
import string
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
        strptime(fecha, '%d/%m/%Y')#valida usando libreria. además sabe los años bisiestos
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

def validarMayorEdad(fechaNacimiento):
    """
    Función: Determinar si una persona es mayor de edad según su fecha de nacimiento (dd/mm/aaaa).
    Entrada:
    -fechaNacimiento(str): Fecha de nacimiento con  formato dd/mm/aaaa
    Salida:
    -True(bool): Si es mayor de edad.
    -False(bool): Si no es mayor de edad.
    """
    fecha_dt = str(strptime(fechaNacimiento, '%d/%m/%Y'))#cambia fecha a tipo date.
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
#2. Generar Donador
#######################
#######################
def generarDonadores(cantidad):
    matriz=[] #base de datos donde se guarda la info de cada persona
    tipoSangre=["O+","O-", "A+", "A-", "B+", "B-", "AB+", "AB-"]
    sexo=["Masculino", "Femenino"]
    extensionCorreo=["@costarricense.cr","@racsa.go.cr","@ccss.sa.cr","@gmail.com"]
    for i in range(cantidad):
        persona=[] #lista de cada persona
        provincia=random.randint(1,9) #inicia cedula
        tomo=""
        asiento=""
        numero1=""
        numero2=""
        for j in range (4):
            tomo+=str(random.randint(0,9))
            asiento+=str(random.randint(0,9))
            numero1+=str(random.randint(0,9)) #para el numero de telefono
            numero2+=str(random.randint(0,9)) #para el numero de telefono
        persona.append(f"{provincia}-{tomo}-{asiento}") #termina cedula
        sexoEleccion=random.choice(sexo)#elige el sexo pero solo para evaluar, si es mujer nombre de mujer o viceversa con hombre
        if sexoEleccion=="Femenino":
            persona.append(names.get_first_name(gender='female')+" "+names.get_last_name()+" "+names.get_last_name()) #mete nombre mujer
        elif sexoEleccion=="Masculino":
            persona.append(names.get_first_name(gender='male')+" "+names.get_last_name()+" "+names.get_last_name()) #mete nombre mujer
        start_date = date(1980, 1, 1) #inica fecha de nacimiento
        end_date = date(2020, 5, 25)
        time_between_dates = end_date - start_date
        random_number_of_days = random.randrange(time_between_dates.days)
        fechaFinal=str(start_date + timedelta(days=random_number_of_days)).split("-")
        persona.append(fechaFinal[2]+"/"+fechaFinal[1]+"/"+fechaFinal[0]) #termina fecha de nacimiento
        persona.append(random.choice(tipoSangre)) #mete tipo de sangre
        persona.append(sexoEleccion) #mete sexo
        persona.append(str(random.randint(50,120))+" kg") #mete peso
        primerNumero=random.choice([2,4,6,7,8,9]) #primer numero de telefono
        persona.append(f"{primerNumero}{numero1}-{numero2}") #mete numero de telefono
        primeroCorreo = ''.join(random.choice(string.ascii_letters+string.digits+".") for i in range(random.randint(6,30))) #inicia correo
        persona.append(primeroCorreo+random.choice(extensionCorreo)) #mete correo
        matriz.append(persona)
    return matriz


#######################
#######################
#4.ELIMINAR DONADOR
#######################
#######################
def eliminarDonador(donadores,eliminar):#cambiar a listas.
# formato: lista=[['cedula','nombreCompleto','fechaNacimiento','sangre','sexo','peso','telefono', 'correo']]
    """
    Función: Eliminar donador.
    Entrada:
    -listaDic(dic): Lista con diccionarios de cada usuario.
    Salida: N/A.
    """
    if revisarLista(donadores,eliminar)==False:
        print("El usuario no se encuentra en la lista")
        return ""
    print("Lista donadores actualizada:",donadores)
    #graba("donadores",donadores)#manda a grabar lista
    print("Usuario eliminado safisfactoriamente.")#debe mostrarse en la interfaz
    #debe regresar al menu
    return ""
def revisarLista(lista,usuario):
    for i,filas in enumerate(lista):
        for j,columna in enumerate(filas):
            if usuario==columna:
                return True
            else:
                break
    return False

listaDonadores=[['7-7775-4349','Jacinto Lohr Vega','24/10/1989','B+','Masculino','73 kg','28931-5016', 'L1jBTVOdpraEa@gmail.com'],['4-6221-2308','Sara Murray Fekete','02/10/2017','AB-','Femenino','106 kg','75168-5115','uhwno0T5@costarricense.cr'],['8-2815-4250', 'Maxine Glover Rapp', '05/04/2007', 'B+', 'Femenino', '93 kg', '26288-9340', 'HPPswwBcOWCxOedBNMrqs8@gmail.com']]
eliminar="7-7775-4349"
eliminarDonador(listaDonadores,eliminar)