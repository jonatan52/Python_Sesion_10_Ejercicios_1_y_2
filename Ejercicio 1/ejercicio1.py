# Ejercicio 1
# Enunciado del ejercicio:
# En este ejercicio tenéis que crear una lista de RadioButton que muestre la opción que se ha seleccionado y que contenga un botón de reinicio para que deje todo como al principio.
# Al principio no tiene que haber una opción seleccionada.


from tkinter import *




def seleccionar():
    monitor.config(text="{}".format(opcion.get()))

def reset():
    opcion.set(None)
    monitor.config(text="")

# Configuración de la raíz
root = Tk()
root.title("lenguajes de Programación")
opcion = StringVar()
opcion.set(None)

Radiobutton(root, text="Python", variable=opcion, 
            value="python", command=seleccionar).pack(anchor=W)

Radiobutton(root, text="Java", variable=opcion, 
            value="Java", command=seleccionar).pack(anchor=W)

Radiobutton(root, text="Java Script", variable=opcion,   
            value="Java Script", command=seleccionar).pack(anchor=W)

monitor = Label(root)
monitor.pack()

Button(root, text="Reiniciar", command=reset).pack()


root.mainloop()



