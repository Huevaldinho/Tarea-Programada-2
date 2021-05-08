#Este código es para la selección de provincia, la misma lógica sirve para seleccionar el sexo y la justificación.
from tkinter import *
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