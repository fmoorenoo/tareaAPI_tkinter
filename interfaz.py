import tkinter as tk
from tkinter import ttk
from tkinter.font import Font

from PIL import Image, ImageTk
from io import BytesIO
import requests
from models.api_response import APIResponse



def cargarProducto(lista_productos: APIResponse, NuevaPosicion: int):
    global label_img, labelTitulo, labelDesc, labelPrecio, labelStock, labelRating

    r = requests.get(lista_productos.products[NuevaPosicion].thumbnail, stream=True)
    newImage = ImageTk.PhotoImage(Image.open(r.raw).resize((150, 150)))
    label_img.config(image=newImage)
    label_img.image = newImage

    labelTitulo.config(text=lista_productos.products[NuevaPosicion].title)
    labelDesc.config(text=lista_productos.products[NuevaPosicion].description)
    labelPrecio.config(text=f"Price: {lista_productos.products[NuevaPosicion].price}$")
    labelStock.config(text=f"Stock: {lista_productos.products[NuevaPosicion].stock}")
    labelRating.config(text=f"Rating: {lista_productos.products[NuevaPosicion].rating}")



def mostrarProducto(lista_productos: APIResponse):
    global posicion, label_img, labelTitulo, labelDesc, labelPrecio, labelStock, labelRating
    posicion = 0
    v_producto = tk.Tk()
    v_producto.title("Productos")
    v_producto.geometry('705x285')
    v_producto.configure(bg='#B0C4C9')
    fuente = Font(family="Helvetica", size=16, weight="bold")

    frame = ttk.Frame(v_producto)
    frame.pack()

    #r = requests.get(lista_productos.products[posicion].thumbnail, stream=True)
    #imagen = Image.open(BytesIO(r.content)).resize((150, 150))
    #photo = ImageTk.PhotoImage(imagen)
    #label_img = tk.Label(frame, image=photo, bg='#B0C4C9')

    r = requests.get(lista_productos.products[posicion].thumbnail, stream=True)
    imagen_tk = ImageTk.PhotoImage(Image.open(r.raw).resize((150, 150)))
    label_img = tk.Label(frame, bg='#B0C4C9', image=imagen_tk)
    label_img.image = imagen_tk
    label_img.grid(row=0, column=0, rowspan=2, padx=10, pady=10)

    labelTitulo = ttk.Label(frame, text=lista_productos.products[posicion].title, font=fuente)
    labelTitulo.grid(row=0, column=1, padx=10)

    labelDesc = ttk.Label(frame, text=lista_productos.products[posicion].description, wraplength=300, anchor="w", justify="left")
    labelDesc.grid(row=1, column=1, padx=10)

    labelPrecio = ttk.Label(frame, text=f"Price: {lista_productos.products[posicion].price}$", font=fuente)
    labelPrecio.grid(row=2, column=0, padx=10)

    labelStock = ttk.Label(frame, text=f"Stock: {lista_productos.products[posicion].stock}", font=fuente)
    labelStock.grid(row=2, column=1, padx=10)

    labelRating = ttk.Label(frame, text=f"Rating: {lista_productos.products[posicion].rating}", font=fuente)
    labelRating.grid(row=2, column=2, padx=10)

    boton_anterior = ttk.Button(frame, text="Anterior", command=lambda: cargarProducto(lista_productos, posicion-1))
    boton_anterior.grid(row=3, column=0, padx=10, pady=20)

    boton_siguiente = ttk.Button(frame, text="Siguiente", command=lambda: cargarProducto(lista_productos, posicion+1))
    boton_siguiente.grid(row=3, column=2, padx=10, pady=20)


    v_producto.mainloop()


