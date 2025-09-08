import tkinter as tk
from tkinter import messagebox

# Función que se ejecuta al presionar el botón
def mostrar_mensaje():
    messagebox.showinfo("Saludo", "Hola")

# Ventana principal
ventana = tk.Tk()
ventana.title("Botón de saludo")
ventana.geometry("200x100")

# Botón
boton = tk.Button(ventana, text="Presionar", command=mostrar_mensaje)
boton.pack(pady=20)

# Bucle principal
ventana.mainloop()
