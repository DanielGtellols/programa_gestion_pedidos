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

        # Se define la tabla de pedidos.
        self.tabla_pedidos = ttk.Treeview(cuadro_tabla, columns=("referencia", "nombre", "fecha_entrega", "cantidad"))
        self.tabla_pedidos.column("#0", width=0, stretch=NO)
        self.tabla_pedidos.column("referencia", anchor=CENTER, width=100)
        self.tabla_pedidos.heading("referencia", text="Referencia")
        self.tabla_pedidos.column("nombre", anchor=CENTER, width=200)
        self.tabla_pedidos.heading("nombre", text="Nombre")
        self.tabla_pedidos.column("fecha_entrega", anchor=CENTER, width=100)
        self.tabla_pedidos.heading("fecha_entrega", text="Fecha de entrega")
        self.tabla_pedidos.column("cantidad", anchor=CENTER, width=100)
        self.tabla_pedidos.heading("cantidad", text="Cantidad")
        self.tabla_pedidos.bind("<Double-1>", self.editar_pedido)

        # Se define la barra de desplazamiento de la tabla.
        barra_desplazamiento = ttk.Scrollbar(cuadro_tabla, orient=VERTICAL, command=self.tabla_pedidos.yview)
        self.tabla_pedidos.configure(yscrollcommand=barra_desplazamiento.set)

        # Se empaquetan la tabla y la barra de desplazamiento.
        self.tabla_pedidos.pack(fill=BOTH, expand=YES)
        barra_desplazamiento.pack(side=RIGHT, fill=Y)

        # Se cargan los pedidos en la tabla.
        self.cargar_tabla_pedidos()

    def cargar_tabla_pedidos(self):
        """Carga los pedidos en la tabla de pedidos."""
        # Se eliminan los pedidos previos de la tabla.
        for pedido in self.tabla_pedidos.get_children():
            self.tabla_pedidos.delete(pedido)

        # Se agregan los pedidos de la lista de pedidos a la tabla.
        for id_pedido, pedido in self.pedidos.items():
            referencia, nombre, fecha_entrega, cantidad = pedido
            self.tabla_pedidos.insert("", END, text=id_pedido, values=(referencia, nombre, fecha_entrega, cantidad))

    def editar_pedido(self, event):
        """Abre la ventana de edición del pedido seleccionado al hacer doble clic en él."""
        item = self.tabla_pedidos.selection()[0]
        id_pedido = self.tabla_pedidos.item(item)["text"]
        referencia, nombre, fecha_entrega, cantidad = self.pedidos[id_pedido]

        # Se crea la ventana de edición.
        self.ventana_editar_pedido = Toplevel()
        self.ventana_editar_pedido.title("Editar pedido")

        # Se define el cuadro de referencia del pedido.
        cuadro_referencia = ttk.Frame(self.ventana_editar_pedido)
        cuadro_referencia.pack(fill=X, padx=10, pady=5)
        ttk.Label(cuadro_referencia, text="Referencia:", width=15).pack(side=LEFT)
        entrada_referencia = ttk.Entry(cuadro_referencia, width=30)
        entrada_referencia.pack(side=LEFT, padx=5)
        entrada_referencia.insert(0, referencia)

        # Se define el cuadro de nombre del pedido.
        cuadro_nombre = ttk.Frame(self.ventana_editar_pedido)
        cuadro_nombre.pack(fill=X, padx=10, pady=5)
        ttk.Label(cuadro_nombre, text="Nombre:", width=40).pack(side=LEFT)
        self.nombre_pedido = ttk.Entry(cuadro_nombre, width=30)
        self.nombre_pedido.pack(side=LEFT, padx=5)


