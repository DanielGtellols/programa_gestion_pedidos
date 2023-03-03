from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

class ProgramaGestionPedidos:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Gestión de Pedidos")
        self.ventana.geometry("800x600")

        # Se define el cuadro de nombre del pedido.
        cuadro_referencia = Frame(self.ventana)
        cuadro_referencia.pack(fill="x")

        etiqueta_referencia = Label(cuadro_referencia, text="Referencia:", width=10)
        etiqueta_referencia.pack(side="left", padx=5, pady=5)

        self.caja_referencia = Entry(cuadro_referencia, width=20)
        self.caja_referencia.pack(side="left", padx=5, pady=5)

        # Se define el cuadro de nombre del cliente.
        cuadro_nombre = Frame(self.ventana)
        cuadro_nombre.pack(fill="x")

        etiqueta_nombre = Label(cuadro_nombre, text="Nombre:", width=10)
        etiqueta_nombre.pack(side="left", padx=5, pady=5)

        self.caja_nombre = Entry(cuadro_nombre, width=20)
        self.caja_nombre.pack(side="left", padx=5, pady=5)

        # Se define el cuadro de fecha de entrega del pedido.
        cuadro_fecha_entrega = Frame(self.ventana)
        cuadro_fecha_entrega.pack(fill="x")

        etiqueta_fecha_entrega = Label(cuadro_fecha_entrega, text="Fecha de Entrega:", width=10)
        etiqueta_fecha_entrega.pack(side="left", padx=5, pady=5)

        self.caja_fecha_entrega = Entry(cuadro_fecha_entrega, width=20)
        self.caja_fecha_entrega.pack(side="left", padx=5, pady=5)

        # Se define el cuadro de cantidad del pedido.
        cuadro_cantidad = Frame(self.ventana)
        cuadro_cantidad.pack(fill="x")

        etiqueta_cantidad = Label(cuadro_cantidad, text="Cantidad:", width=10)
        etiqueta_cantidad.pack(side="left", padx=5, pady=5)

        self.caja_cantidad = Entry(cuadro_cantidad, width=20)
        self.caja_cantidad.pack(side="left", padx=5, pady=5)

        # Se define el cuadro de botones para agregar y eliminar pedidos.
        cuadro_botones = Frame(self.ventana)
        cuadro_botones.pack(fill="x")

        boton_agregar = Button(cuadro_botones, text="Agregar Pedido", command=self.agregar_pedido)
        boton_agregar.pack(side="left", padx=5, pady=5)

        boton_eliminar = Button(cuadro_botones, text="Eliminar Pedido", command=self.eliminar_pedido)
        boton_eliminar.pack(side="left", padx=5, pady=5)

        # Se define el cuadro de la tabla de pedidos.
        cuadro_tabla = Frame(self.ventana)
        cuadro_tabla.pack(fill="both", expand=True)

        self.tabla_pedidos = ttk.Treeview(cuadro_tabla, columns=("referencia", "nombre", "fecha_entrega", "cantidad"))
        self.tabla_pedidos.column("#0", width=0, stretch=NO)
        self.tabla_pedidos.column("referencia", anchor=CENTER, width=100)
        self.tabla

