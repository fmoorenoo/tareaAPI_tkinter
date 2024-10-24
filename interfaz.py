import tkinter as tk
from tkinter import ttk
from tkinter.font import Font

from PIL import Image, ImageTk
import requests
from models.api_response import APIResponse


def cargarProducto(lista_productos: APIResponse, direccion: int):
    global label_img, labelTitulo, labelDesc, labelPrecio, labelStock, labelRating, indice
    if direccion == "anterior":
        indice -= 1
        if indice < 0:
            indice = len(lista_productos.products) - 1
    elif direccion == "siguiente":
        indice += 1
        if indice >= len(lista_productos.products):
            indice = 0
    else:
        indice = direccion

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
    global label_img, labelTitulo, labelDesc, labelPrecio, labelStock, labelRating, indice, boton_buscar
    indice = 0
    v_producto = tk.Tk()
    v_producto.title("Productos")
    v_producto.geometry('775x265')
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

    boton_buscar = ttk.Button(frame, text="Buscador", command=lambda: ventanaBuscador(lista_productos))
    boton_buscar.grid(row=0, column=2, padx=10, pady=20)

    labelDesc = ttk.Label(frame, text=lista_productos.products[indice].description, wraplength=300, anchor="w", justify="left")
    labelDesc.grid(row=1, column=1, padx=10)

    labelPrecio = ttk.Label(frame, text=f"Price: {lista_productos.products[indice].price}$", font=fuente)
    labelPrecio.grid(row=2, column=0, padx=10)

    labelStock = ttk.Label(frame, text=f"Stock: {lista_productos.products[indice].stock}", font=fuente)
    labelStock.grid(row=2, column=1, padx=10)

    labelRating = ttk.Label(frame, text=f"Rating: {lista_productos.products[indice].rating}", font=fuente)
    labelRating.grid(row=2, column=2, padx=10)

    boton_anterior = ttk.Button(frame, text="Anterior", command=lambda: cargarProducto(lista_productos, "anterior"))
    boton_anterior.grid(row=3, column=0, padx=10, pady=20)

    boton_siguiente = ttk.Button(frame, text="Siguiente", command=lambda: cargarProducto(lista_productos, "siguiente"))
    boton_siguiente.grid(row=3, column=2, padx=10, pady=20)

    v_producto.mainloop()


def ventanaBuscador(lista_productos):
    global boton_buscar
    boton_buscar.config(state="disabled")

    v_busqueda = tk.Tk()
    v_busqueda.title("Buscador")
    v_busqueda.geometry('655x70+630+300')
    v_busqueda.configure(bg='#B0C4C9')
    fuente = Font(family="Helvetica", size=16, weight="bold")
    frame = tk.Frame(v_busqueda)
    frame.pack()

    labelTitulo = ttk.Label(frame, text="Buscador de productos", font=fuente)
    labelTitulo.grid(row=0, column=0, padx=10)

    entrada = ttk.Entry(frame, font=fuente)
    entrada.grid(row=0, column=1, padx=10)

    boton_busqueda = ttk.Button(frame, text="Buscar", command=lambda: mostrarResultados(entrada.get().lower(), lista_productos))
    boton_busqueda.grid(row=0, column=2, padx=10, pady=20)

    boton_cerrar = ttk.Button(frame, text="Cerrar ventana", command=lambda: cerrarBuscador(v_busqueda))
    boton_cerrar.grid(row=0, column=3, padx=10, pady=0)

    v_busqueda.protocol("WM_DELETE_WINDOW", lambda: cerrarBuscador(v_busqueda))



def mostrarResultados(titulo, lista_productos):
    resultados = []
    if titulo.strip() == "":
        print("No se encontraron resultados")
    else:
        for producto in lista_productos.products:
            if titulo in producto.title.lower():
                resultados.append((producto.title))

        if resultados:
            ventanaResultados(resultados, lista_productos)



def ventanaResultados(resultados, lista_productos):
    v_resultados = tk.Tk()
    v_resultados.title("Búsqueda")
    v_resultados.geometry('350x850+1400+150')
    v_resultados.configure(bg='#B0C4C9')

    frame = tk.Frame(v_resultados)
    frame.pack()

    for titulo in resultados:
        lista_titulos = []
        for producto in lista_productos.products:
            lista_titulos.append(producto.title)
        indice_producto = lista_titulos.index(titulo)

        boton_producto = ttk.Button(frame, text=titulo, command=lambda i = indice_producto : cargarProducto(lista_productos, i))
        boton_producto.pack(pady=5)



def cerrarBuscador(ventana):
    global boton_buscar
    boton_buscar.config(state="normal")
    ventana.destroy()
