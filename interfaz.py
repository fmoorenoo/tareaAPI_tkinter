import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from io import BytesIO
import requests


def mostrarProducto(lista_productos, posicion: int):
    v_producto = tk.Tk()
    v_producto.title("Productos")
    v_producto.geometry('500x500')

    labelTitulo = ttk.Label(v_producto, text=lista_productos.products[posicion].title, padding=10)
    labelTitulo.pack(pady=20)

    labelDesc = ttk.Label(v_producto, text=lista_productos.products[posicion].description, padding=10)
    labelDesc.pack(pady=20)

    r = requests.get(lista_productos.products[posicion].thumbnail)
    imagen = Image.open(BytesIO(r.content))
    photo = ImageTk.PhotoImage(imagen)
    label_img = tk.Label(v_producto, image=photo)
    label_img.pack(pady=20)

    labelPrecio = ttk.Label(v_producto, text=f"Precio: {lista_productos.products[posicion].price}", padding=10)
    labelPrecio.pack(pady=20)

    labelRating = ttk.Label(v_producto, text=f"Valoración: {lista_productos.products[posicion].rating}", padding=10)
    labelRating.pack(pady=20)

#    boton_siguiente = ttk.Button(v_producto, text="Siguiente", command=)
#   boton_siguiente.pack(pady=5)

    v_producto.mainloop()


