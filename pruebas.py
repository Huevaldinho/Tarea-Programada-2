from tkinter import *
#raiz es un objeto
raiz=Tk()#ventana
raiz.title("Nombre del programa en la barra")#agreta titulo a la barra del programa.
raiz.resizable(1,1)#permite o no modificar el tamaño de la ventana. primer 1 es verdadero 0 falso. o True False.
raiz.iconbitmap("a.ico")#icono de la barra.
raiz.geometry("650x350")#le da tamaño al objeto raiz.
raiz.config(bg="gray")
raiz.mainloop()#hace que siempre esté a la espera de un evento.#SIEMPRE DEBE ESTAR AL FINAL  