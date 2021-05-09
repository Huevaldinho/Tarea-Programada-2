from tkinter import *
ventana=Tk()
ventana.title("Calculadora")
ventana.resizable(0,0)
ventana.config(bg="orange")
i=0
#Entrada de texto
e_texto=Entry(ventana,font=("TimesNewRoman 30"))
e_texto.grid(row=0,column=0,columnspan=4,padx=5,pady=5) #posicionar cuadro
#columnspan es cuantas columnas debajo del cuadro

#Funciones
def clickboton(valor):
    global i
    e_texto.insert(i,valor)
    i+=1
def borrar():
    e_texto.delete(0,END)
    global i
    i=0
def operacion():
    ecuacion=e_texto.get()
    result= eval(ecuacion)
    e_texto.delete(0,END)
    e_texto.insert(0,result)
    i=0
#Botones
boton1=Button(ventana,text="1",font=("TimesNewRoman 17"),width=8,height=4,command=lambda: clickboton(1))
boton2=Button(ventana,text="2",font=("TimesNewRoman 17"),width=8,height=4,command=lambda: clickboton(2))
boton3=Button(ventana,text="3",font=("TimesNewRoman 17"),width=8,height=4,command=lambda: clickboton(3))
boton4=Button(ventana,text="4",font=("TimesNewRoman 17"),width=8,height=4, command=lambda: clickboton(4))
boton5=Button(ventana,text="5",font=("TimesNewRoman 17"),width=8,height=4,command=lambda: clickboton(5))
boton6=Button(ventana,text="6",font=("TimesNewRoman 17"),width=8,height=4, command=lambda: clickboton(6))
boton7=Button(ventana,text="7",font=("TimesNewRoman 17"),width=8,height=4,command=lambda: clickboton(7))
boton8=Button(ventana,text="8",font=("TimesNewRoman 17"),width=8,height=4, command=lambda: clickboton(8))
boton9=Button(ventana,text="9",font=("TimesNewRoman 17"),width=8,height=4, command=lambda: clickboton(9))
boton0=Button(ventana,text="0",font=("TimesNewRoman 17"),width=17,height=4, command=lambda: clickboton(0))

boton_borrar=Button(ventana,text="AC",font=("TimesNewRoman 17"),width=8,height=4, command=lambda: borrar())
boton_parentesis1=Button(ventana,text="(",font=("TimesNewRoman 17"),width=8,height=4, command=lambda: clickboton("("))
boton_parentesis2=Button(ventana,text=")",font=("TimesNewRoman 17"),width=8,height=4, command=lambda: clickboton(")"))
boton_punto=Button(ventana,text=".",font=("TimesNewRoman 17"),width=8,height=4, command=lambda: clickboton("."))

boton_suma=Button(ventana,text="+",font=("TimesNewRoman 17"),width=8,height=4, command=lambda: clickboton("+"))
boton_resta=Button(ventana,text="-",font=("TimesNewRoman 17"),width=8,height=4,command=lambda: clickboton("-"))
boton_division=Button(ventana,text="/",font=("TimesNewRoman 17"),width=8,height=4, command=lambda: clickboton("/"))
boton_multiplicacion=Button(ventana,text="*",font=("TimesNewRoman 17"),width=8,height=4, command=lambda: clickboton("*"))
boton_igual=Button(ventana,text="=",font=("TimesNewRoman 17"),width=8,height=4, command=lambda: operacion())

#Posicionar botones
boton_borrar.grid(row=1 ,column=0, padx=5, pady=5)
boton_parentesis1.grid(row=1 ,column=1, padx=5, pady=5)
boton_parentesis2.grid(row=1 ,column=2, padx=5, pady=5)
boton_division.grid(row=1,column=3, padx=5, pady=5)
boton_multiplicacion.grid(row=2 ,column=3, padx=5, pady=5)
boton_suma.grid(row=3 ,column=3, padx=5, pady=5)
boton_resta.grid(row=4 ,column=3, padx=5, pady=5)
boton_igual.grid(row=5 ,column=3, padx=5, pady=5)
boton1.grid(row=4 ,column=0, padx=5, pady=5)
boton2.grid(row=4 ,column=1, padx=5, pady=5)
boton3.grid(row=4 ,column=2, padx=5, pady=5)
boton4.grid(row=3 ,column=0, padx=5, pady=5)
boton5.grid(row=3,column=1, padx=5, pady=5)
boton6.grid(row=3,column=2, padx=5, pady=5)
boton7.grid(row=2,column=0, padx=5, pady=5)
boton8.grid(row=2,column=1, padx=5, pady=5)
boton9.grid(row=2 ,column=2, padx=5, pady=5)
boton0.grid(row=5 ,column=0,columnspan=2)
boton_punto.grid(row=5 ,column=2, padx=5, pady=5)
ventana.mainloop() 