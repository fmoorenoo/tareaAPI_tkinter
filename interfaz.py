import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk
from models.api_response import APIResponse


def mostrarProducto(lista_productos: APIResponse, posicion: int):
    v_producto = tk.Tk()
    v_producto.title("Productos")
    v_producto.geometry('500x500')
    labelTitulo = ttk.Label(v_producto, text=lista_productos.products[posicion].title , padding=10)
    labelTitulo.pack(pady=20)

    v_producto.mainloop()