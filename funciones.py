#prueba conexión con base de datos local.
import mysql.connector
cnn=mysql.connector.connect(host="localhost",user="root",passwd="",database="prueba")
print(cnn)#se conecta a la base de datos.