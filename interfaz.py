import tkinter as tk
from tkinter import ttk
from tkinter.font import Font

from PIL import Image, ImageTk
import requests
from models.api_response import APIResponse



def cargarProducto(lista_productos: APIResponse, direccion: int):
    global label_img, labelTitulo, labelDesc, labelPrecio, labelStock, labelRating, indice

    indice += direccion
    if indice >= len(lista_productos.products):
        indice = 0
    elif indice < 0:
        indice = len(lista_productos.products) - 1
    r = requests.get(lista_productos.products[indice].thumbnail, stream=True)
    newImage = ImageTk.PhotoImage(Image.open(r.raw).resize((150, 150)))
    label_img.config(image=newImage)
    label_img.image = newImage

    labelTitulo.config(text=lista_productos.products[indice].title)
    labelDesc.config(text=lista_productos.products[indice].description)
    labelPrecio.config(text=f"Price: {lista_productos.products[indice].price}$")
    labelStock.config(text=f"Stock: {lista_productos.products[indice].stock}")
    labelRating.config(text=f"Rating: {lista_productos.products[indice].rating}")



def mostrarProducto(lista_productos: APIResponse):
    global label_img, labelTitulo, labelDesc, labelPrecio, labelStock, labelRating, indice
    indice = 0
    v_producto = tk.Tk()
    v_producto.title("Productos")
    v_producto.geometry('745x265')
    v_producto.configure(bg='#B0C4C9')
    fuente = Font(family="Helvetica", size=16, weight="bold")
    frame = tk.Frame(v_producto)
    frame.pack()


    r = requests.get(lista_productos.products[indice].thumbnail, stream=True)
    imagen_tk = ImageTk.PhotoImage(Image.open(r.raw).resize((150, 150)))
    label_img = tk.Label(frame, bg='#B0C4C9', image=imagen_tk)
    label_img.image = imagen_tk
    label_img.grid(row=0, column=0, rowspan=2, padx=10, pady=10)

    labelTitulo = ttk.Label(frame, text=lista_productos.products[indice].title, font=fuente)
    labelTitulo.grid(row=0, column=1, padx=10)

    boton_buscar = ttk.Button(frame, text="Buscador", command=lambda: buscarProductos())
    boton_buscar.grid(row=0, column=2, padx=10, pady=20)

    labelDesc = ttk.Label(frame, text=lista_productos.products[indice].description, wraplength=300, anchor="w", justify="left")
    labelDesc.grid(row=1, column=1, padx=10)

    labelPrecio = ttk.Label(frame, text=f"Price: {lista_productos.products[indice].price}$", font=fuente)
    labelPrecio.grid(row=2, column=0, padx=10)

    labelStock = ttk.Label(frame, text=f"Stock: {lista_productos.products[indice].stock}", font=fuente)
    labelStock.grid(row=2, column=1, padx=10)

    labelRating = ttk.Label(frame, text=f"Rating: {lista_productos.products[indice].rating}", font=fuente)
    labelRating.grid(row=2, column=2, padx=10)

    boton_anterior = ttk.Button(frame, text="Anterior", command=lambda: cargarProducto(lista_productos, -1))
    boton_anterior.grid(row=3, column=0, padx=10, pady=20)

    boton_siguiente = ttk.Button(frame, text="Siguiente", command=lambda: cargarProducto(lista_productos, 1))
    boton_siguiente.grid(row=3, column=2, padx=10, pady=20)


    v_producto.mainloop()

def buscarProductos():
    global lista_productos
    v_busqueda = tk.Tk()
    v_busqueda.title("Buscador")
    v_busqueda.geometry('745x265')
    v_busqueda.configure(bg='#B0C4C9')
    fuente = Font(family="Helvetica", size=16, weight="bold")
    frame = tk.Frame(v_busqueda)
    frame.pack()
    labelTitulo = ttk.Label(frame, text="Buscador de productos", font=fuente)
    labelTitulo.grid(row=0, column=0, padx=10)

    entrada = ttk.Entry(frame, font=fuente)
    entrada.grid(row=0, column=1, padx=10)

    boton_buscar = ttk.Button(frame, text="Buscar", command=False)
    boton_buscar.grid(row=0, column=2, padx=10, pady=20)