# Ejercicio 2
# Enunciado del ejercicio:

# En este segundo ejercicio, tendréis que crear una interfaz sencilla la cual debe de contener una lista de elementos seleccionables, 
# también debe de tener un label con el texto que queráis.


from tkinter import *
root = Tk()
lenguajes = StringVar()
listbox = Listbox(root)
label = Label(text="Lenguajes de programación")
label.pack()
for lenguaje in ["Python", "Java", "c++", "Ruby", "Go", "Java Script"]:
 listbox.insert(END, lenguaje)
listbox.pack()

label.pack()
root.mainloop()
    