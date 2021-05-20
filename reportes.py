#Elaborado por: Felipe Obando y Sebastián Bermúdez.
#Fecha elaboración: 
#Última modificación: 
#Versión: 3.9.2

#Reportes FALTANTES
#6. ¿A quién puede donar?,7. ¿De quién puede recibir?
#lista debe estar en orden: Cédula, Nombre Completo,Tipo de sangre, Teléfono, Correo.

import pickle
import re
#Reportes 1,2,3 y 5.
def reportes1235(matriz):
    nombreReporte=matriz[0]#Saca el nombre del archivo de la matriz
    nombreReporte=re.sub(r"\s+","",nombreReporte)#QUITA LOS ESPACIOS  DEL PRIMER ELEMENTO PARA DARLE ESE NOMBRE AL ARCHIVO.
    fechaCreacion=matriz[1]#saca la fecha de la matriz
    archivo=open(nombreReporte+".html","w")#crea el archivo.
    archivo.write("<!DOCTYPE html>"+'\n''<html lang="es">\n')
    archivo.write("<head>"+ '\n'"\t<title>Reporte</title>\n")
    archivo.write("\t<meta charset='utf-8'>\n""\t<meta name='viewport' content='width=device-width, initial-scale=1'>")
    archivo.write("\t<link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css'>\n")
    archivo.write('\t<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>\n')
    archivo.write('\t<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>\n')
    archivo.write("</head>\n""<body>\n")
    archivo.write('\t<div class="jumbotron text-center">\n'"\t'<h1>"+matriz[0]+"<h1>\n""</div>\n")
    archivo.write('<div class="container">\n')
    archivo.write('\t<h4>Fecha de creacion: '+ fechaCreacion[0:8]+'</h4>\n\t<h4>Hora: '+ fechaCreacion[9:17]+' </h4>\n')
    archivo.write('\t\t<table class="table table-striped">\n\t\t\t<tr>\n')
    archivo.write('\t\t\t\t<th>C&eacutedula</th>\n\t\t\t\t<th>Nombre completo</th>\n\t\t\t\t<th>Fecha de nacimiento</th>\n\t\t\t\t<th>Tel&eacutefono</th>\n\t\t\t\t<th>Correo</th>\n\t\t\t</tr>\n')
    matriz=matriz[2:]
    for i in range(len(matriz)):#ciclo para poner a todos los donadores.
        archivo.write('\t\t<tr>\n')
        archivo.write('\t\t\t<td>'+matriz[i][0]+'</td>\n')#Cédula.
        archivo.write('\t\t\t<td>'+matriz[i][1]+'</td>\n')#Nombre completo.
        archivo.write('\t\t\t<td>'+matriz[i][2]+'</td>\n')#Fecha de nacimiento.
        archivo.write('\t\t\t<td>'+matriz[i][3]+'</td>\n')#Teléfono.
        archivo.write('\t\t\t<td>'+matriz[i][4]+'</td>\n')#Correo.
        archivo.write('\t\t</tr>\n')
    archivo.write("</body>\n"'</html')#Cierra el body y el html
    archivo.close#cierra archivo
    return
def reporte4(matriz):
    nombreReporte=matriz[0]#Saca el nombre del archivo de la matriz
    nombreReporte=re.sub(r"\s+","",nombreReporte)#QUITA LOS ESPACIOS  DEL PRIMER ELEMENTO PARA DARLE ESE NOMBRE AL ARCHIVO.
    fechaCreacion=matriz[1]#saca la fecha de la matriz
    archivo=open(nombreReporte+".html","w")#crea el archivo.
    archivo.write("<!DOCTYPE html>"+'\n''<html lang="es">\n')
    archivo.write("<head>"+ '\n'"\t<title>Reporte</title>\n")
    archivo.write("\t<meta charset='utf-8'>\n""\t<meta name='viewport' content='width=device-width, initial-scale=1'>")
    archivo.write("\t<link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css'>\n")
    archivo.write('\t<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>\n')
    archivo.write('\t<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>\n')
    archivo.write("</head>\n""<body>\n")
    archivo.write('\t<div class="jumbotron text-center">\n'"\t'<h1>"+matriz[0]+"<h1>\n""</div>\n")
    archivo.write('<div class="container">\n')
    archivo.write('\t<h4>Fecha de creacion: '+ fechaCreacion[0:8]+'</h4>\n\t<h4>Hora: '+ fechaCreacion[9:17]+' </h4>\n')
    archivo.write('\t\t<table class="table table-striped">\n\t\t\t<tr>\n')
    archivo.write('\t\t\t\t<th>C&eacutedula</th>\n\t\t\t\t<th>Nombre completo</th>\n\t\t\t\t<th>Tipo de sangre</th>\n\t\t\t\t<th>Fecha de nacimiento</th>\n\t\t\t\t<th>Peso</th>\n\t\t\t\t<th>Sexo</th>\n\t\t\t\t<th>T&eacutelefono</th>\n\t\t\t\t<th>Correo</th>')
    matriz=matriz[2:]
    for i in range(len(matriz)):#ciclo para poner a todos los donadores.
        archivo.write('\t\t<tr>\n')
        archivo.write('\t\t\t<td>'+matriz[i][0]+'</td>\n')#Cédula.
        archivo.write('\t\t\t<td>'+matriz[i][1]+'</td>\n')#Nombre completo.
        archivo.write('\t\t\t<td>'+matriz[i][2]+'</td>\n')#Tipo de sangre
        archivo.write('\t\t\t<td>'+matriz[i][3]+'</td>\n')#Fecha de nacimiento.
        archivo.write('\t\t\t<td>'+matriz[i][4]+'</td>\n')#Peso
        archivo.write('\t\t\t<td>'+matriz[i][5]+'</td>\n')#Sexo
        archivo.write('\t\t\t<td>'+matriz[i][6]+'</td>\n')#Teléfono.
        archivo.write('\t\t\t<td>'+matriz[i][7]+'</td>\n')#Correo.
        archivo.write('\t\t</tr>\n')
    archivo.write("</body>\n"'</html')#Cierra el body y el html
    archivo.close#cierra archivo
    return
def reporteDonadoresNOactivos(matriz):
    nombreReporte=matriz[0]#Saca el nombre del archivo de la matriz
    nombreReporte=re.sub(r"\s+","",nombreReporte)#QUITA LOS ESPACIOS  DEL PRIMER ELEMENTO PARA DARLE ESE NOMBRE AL ARCHIVO.
    fechaCreacion=matriz[1]#saca la fecha de la matriz
    archivo=open(nombreReporte+".html","w")#crea el archivo.
    archivo.write("<!DOCTYPE html>"+'\n''<html lang="es">\n')
    archivo.write("<head>"+ '\n'"\t<title>Reporte</title>\n")
    archivo.write("\t<meta charset='utf-8'>\n""\t<meta name='viewport' content='width=device-width, initial-scale=1'>")
    archivo.write("\t<link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css'>\n")
    archivo.write('\t<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>\n')
    archivo.write('\t<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>\n')
    archivo.write("</head>\n""<body>\n")
    archivo.write('\t<div class="jumbotron text-center">\n'"\t'<h1>"+matriz[0]+"<h1>\n""</div>\n")
    archivo.write('<div class="container">\n')
    archivo.write('\t<h4>Fecha de creacion: '+ fechaCreacion[0:8]+'</h4>\n\t<h4>Hora: '+ fechaCreacion[9:17]+' </h4>\n')
    archivo.write('\t\t<table class="table table-striped">\n\t\t\t<tr>\n')
    archivo.write('\t\t\t\t<th>Justificaci&oacuten</th>\t\t\t\t<th>C&eacutedula</th>\n\t\t\t\t<th>Nombre completo</th>\n\t\t\t\t<th>Tipo de sangre</th>\n\t\t\t\t<th>Fecha de nacimiento</th>\n\t\t\t\t<th>Peso</th>\n\t\t\t\t<th>Sexo</th>\n\t\t\t\t<th>Tel&eacutefono</th>\n\t\t\t\t<th>Correo</th>')
    matriz=matriz[2:]#le quita el nombre y la fecha para trabajar solo con los donadores.
    print(matriz)
    for i in range(len(matriz)):#ciclo para poner a todos los donadores.
        archivo.write('\t\t<tr>\n')
        archivo.write('\t\t\t<td>'+matriz[i][0]+'</td>\n')#Justificación.
        archivo.write('\t\t\t<td>'+matriz[i][1]+'</td>\n')#Cédula.
        archivo.write('\t\t\t<td>'+matriz[i][2]+'</td>\n')#Nombre completo.
        archivo.write('\t\t\t<td>'+matriz[i][3]+'</td>\n')#Tipo de sangre
        archivo.write('\t\t\t<td>'+matriz[i][4]+'</td>\n')#Fecha de nacimiento.
        archivo.write('\t\t\t<td>'+str(matriz[i][5])+'</td>\n')#Peso
        if matriz[i][6]==True:
            archivo.write('\t\t\t<td>'+"Masculino"+'</td>\n')#Sexo
        else:
            archivo.write('\t\t\t<td>'+"Femenino"+'</td>\n')#Sexo
        archivo.write('\t\t\t<td>'+matriz[i][7]+'</td>\n')#Teléfono.
        archivo.write('\t\t\t<td>'+matriz[i][8]+'</td>\n')#Correo.
        archivo.write('\t\t</tr>\n')
    archivo.write("</body>\n"'</html')#Cierra el body y el html
    archivo.close#cierra archivo
    return