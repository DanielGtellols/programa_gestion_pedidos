import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os
from fpdf import FPDF

class Aplicacion:

    def __init__(self):

        self.ventana_principal = tk.Tk()
        self.ventana_principal.title("Gestión de pedidos y fabricación")
        self.cargar_base_de_datos()
        self.cargar_interfaz_grafica()

    def cargar_base_de_datos(self):

        # En este método se cargaría la base de datos, si es que la hubiera.
        # Por simplicidad, para este ejemplo, usaremos una lista en memoria.
        self.pedidos = [
            {"numero": "001", "cliente": "Cliente 1", "fecha": "01/01/2022"},
            {"numero": "002", "cliente": "Cliente 2", "fecha": "02/01/2022"},
            {"numero": "003", "cliente": "Cliente 3", "fecha": "03/01/2022"}
        ]

    def cargar_interfaz_grafica(self):

        # Aquí se define la interfaz gráfica con sus widgets.
        # Por simplicidad, en este ejemplo sólo creamos la ventana principal y un botón de "Listar pedidos".
        self.boton_listar_pedidos = ttk.Button(self.ventana_principal, text="Listar pedidos", command=self.listar_pedidos)
        self.boton_listar_pedidos.pack()

        # Se inicia el bucle principal de la aplicación.
        self.ventana_principal.mainloop()
    def listar_pedidos(self):

        # Crea una ventana secundaria para listar los pedidos.
        self.ventana_listado_pedidos = tk.Toplevel(self.ventana_principal)
        self.ventana_listado_pedidos.title("Listado de pedidos")

        # Se crea un Treeview para mostrar la información de los pedidos.
        self.treeview_pedidos = ttk.Treeview(self.ventana_listado_pedidos)
        self.treeview_pedidos["columns"] = ("cliente", "fecha")
        self.treeview_pedidos.heading("#0", text="Número de pedido")
        self.treeview_pedidos.column("cliente", width=150)
        self.treeview_pedidos.heading("cliente", text="Cliente")
        self.treeview_pedidos.column("fecha", width=100)
        self.treeview_pedidos.heading("fecha", text="Fecha de recepción")
        self.treeview_pedidos.pack()

        # Se rellena el Treeview con la información de los pedidos.
        for pedido in self.pedidos:
            self.treeview_pedidos.insert("", "end", text=pedido["numero"], values=(pedido["cliente"], pedido["fecha"]))

        # Se añaden botones para editar, añadir y borrar pedidos.
        self.boton_editar_pedido = Button(self.ventana_pedidos, text="Editar", command=self.editar_pedido)
        self.boton_editar_pedido.grid(row=5, column=2, pady=5, padx=5)

        self.boton_anadir_pedido = Button(self.ventana_pedidos, text="Añadir", command=self.anadir_pedido)
        self.boton_anadir_pedido.grid(row=5, column=3, pady=5, padx=5)

        self.boton_eliminar_pedido = Button(self.ventana_pedidos, text="Eliminar", command=self.eliminar_pedido)
        self.boton_eliminar_pedido.grid(row=5, column=4, pady=5, padx=5)

        # Se añade un botón para abrir la ventana de referencias.
        self.boton_referencias_pedido = Button(self.ventana_pedidos, text="Ver referencias", command=self.ver_referencias_pedido)
        self.boton_referencias_pedido.grid(row=6, column=3, pady=5, padx=5)

    def ver_referencias_pedido(self):
        """
        Abre la ventana de referencias del pedido seleccionado.
        """
        try:
            self.tree_pedidos.focus()  # Enfoca el Treeview de pedidos.
            # Obtiene el número de pedido seleccionado.
            numero_pedido = int(self.tree_pedidos.item(self.tree_pedidos.selection())['text'])
            self.ventana_referencias = Toplevel()
            self.ventana_referencias.title("Referencias del pedido " + str(numero_pedido))
            self.ventana_referencias.geometry("800x400")

            # Se crea un Treeview para mostrar las referencias del pedido.
            self.tree_referencias = ttk.Treeview(self.ventana_referencias, columns=("referencia", "fecha_entrega", "estado"), selectmode="browse")
            self.tree_referencias.heading("#0", text="ID")
            self.tree_referencias.heading("referencia", text="Referencia")
            self.tree_referencias.heading("fecha_entrega", text="Fecha de entrega")
            self.tree_referencias.heading("estado", text="Estado")
            self.tree_referencias.column("#0", width=50)
            self.tree_referencias.column("referencia", width=150)
            self.tree_referencias.column("fecha_entrega", width=150)
            self.tree_referencias.column("estado", width=150)
            self.tree_referencias.pack(pady=5)

            # Se agregan los botones para editar, añadir y borrar referencias.
            self.boton_editar_referencia = Button(self.ventana_referencias, text="Editar", command=self.editar_referencia)
            self.boton_editar_referencia.grid(row=1, column=0, pady=5, padx=5)

            self.boton_anadir_referencia = Button(self.ventana_referencias, text="Añadir", command=self.anadir_referencia)
            self.boton_anadir_referencia.grid(row=1, column=1, pady=5, padx=5)

            self.boton_eliminar_referencia = Button(self.ventana_referencias, text="Eliminar", command=self.eliminar_referencia)
            self.boton_eliminar_referencia.grid(row=1, column=2, pady=5, padx=5)
                    # Se añade un botón para asignar un plano a una referencia.
        self.boton_asignar_plano = Button(self.frame_referencias, text="Asignar plano", command=self.asignar_plano)
        self.boton_asignar_plano.grid(row=4, column=3, padx=5, pady=5)

        # Se añade un botón para abrir el plano asignado a una referencia.
        self.boton_abrir_plano = Button(self.frame_referencias, text="Abrir plano", command=self.abrir_plano)
        self.boton_abrir_plano.grid(row=4, column=4, padx=5, pady=5)

        # Se añade un botón para imprimir el listado de artículos necesarios para la fabricación de una referencia.
        self.boton_imprimir = Button(self.frame_referencias, text="Imprimir listado", command=self.imprimir)
        self.boton_imprimir.grid(row=5, column=3, padx=5, pady=5)

        # Se añade un botón para volver a la ventana de pedidos.
        self.boton_volver_pedidos = Button(self.frame_referencias, text="Volver", command=self.volver_pedidos)
        self.boton_volver_pedidos.grid(row=5, column=4, padx=5, pady=5)

    def crear_ficha_referencia(self):
        # Se crea una ventana para la ficha de referencia.
        self.ventana_ficha_referencia = Toplevel(self.ventana_principal)
        self.ventana_ficha_referencia.title("Ficha de referencia")
        self.ventana_ficha_referencia.geometry("500x400")

        # Se crea un marco para los datos generales de la referencia.
        self.frame_datos_referencia = Frame(self.ventana_ficha_referencia, padx=10, pady=10)
        self.frame_datos_referencia.pack()

        # Se añaden etiquetas y campos de texto para los datos generales de la referencia.
        Label(self.frame_datos_referencia, text="Referencia:").grid(row=0, column=0, padx=5, pady=5)
        self.campo_referencia = Entry(self.frame_datos_referencia)
        self.campo_referencia.grid(row=0, column=1, padx=5, pady=5)

        Label(self.frame_datos_referencia, text="Fecha de entrega:").grid(row=1, column=0, padx=5, pady=5)
        self.campo_fecha_entrega = Entry(self.frame_datos_referencia)
        self.campo_fecha_entrega.grid(row=1, column=1, padx=5, pady=5)

        Label(self.frame_datos_referencia, text="Estado:").grid(row=2, column=0, padx=5, pady=5)
        self.opciones_estado = ["Entregado", "En fabricación", "Pedido", "Incidencia"]
        self.campo_estado = ttk.Combobox(self.frame_datos_referencia, values=self.opciones_estado)
        self.campo_estado.grid(row=2, column=1, padx=5, pady=5)

        self.campo_estado.bind("<<ComboboxSelected>>", self.mostrar_comentario_incidencia)

        self.label_comentario_incidencia = Label(self.frame_datos_referencia, text="Comentario de incidencia:")
        self.label_comentario_incidencia.grid(row=3, column=0, padx=5, pady=5)

            # Se crea un campo de texto para el comentario de incidencia.
    self.campo_comentario_incidencia = Text(self.frame_datos_referencia, height=5)
    self.campo_comentario_incidencia.grid(row=3, column=1, padx=5, pady=5)

    # Se añade un botón para guardar los cambios en la ficha de referencia.
    self.boton_guardar_cambios = Button(self.ventana_ficha_referencia, text="Guardar cambios", command=self.guardar_cambios_referencia)
    self.boton_guardar_cambios.pack(padx=10, pady=10)

def mostrar_comentario_incidencia(self, event):
    # Se muestra el campo de texto del comentario de incidencia si el estado de la referencia es "Incidencia".
    if self.campo_estado.get() == "Incidencia":
        self.label_comentario_incidencia.grid(row=3, column=0, padx=5, pady=5)
        self.campo_comentario_incidencia.grid(row=3, column=1, padx=5, pady=5)
    else:
        self.label_comentario_incidencia.grid_forget()
        self.campo_comentario_incidencia.grid_forget()

def asignar_plano(self):
    # Se abre un cuadro de diálogo para seleccionar un archivo de plano y se guarda la ruta en la variable self.ruta_plano.
    self.ruta_plano = filedialog.askopenfilename(initialdir="/", title="Seleccionar archivo de plano", filetypes=[("Archivos de plano", "*.pdf")])
    if self.ruta_plano:
        messagebox.showinfo("Plano asignado", "Se ha asignado un plano a la referencia.")

def abrir_plano(self):
    # Se abre el archivo de plano asignado a la referencia.
    if self.ruta_plano:
        os.startfile(self.ruta_plano)
    else:
        messagebox.showwarning("Sin plano asignado", "No se ha asignado ningún plano a la referencia.")

def imprimir(self):
    # Se imprime el listado de artículos necesarios para la fabricación de la referencia.
    pass

def volver_pedidos(self):
    # Se destruye la ventana de la ficha de referencia y se vuelve a la ventana de pedidos.
    self.ventana_ficha_referencia.destroy()

    # Se borran los datos de la tabla de referencias.
    self.borrar_tabla_referencias()

    # Se cargan los pedidos en la tabla de pedidos.
    self.cargar_pedidos()

def asignar_plano(self):
    # Se abre una ventana de selección de archivo.
    archivo = filedialog.askopenfilename(title="Seleccionar plano", filetypes=[("Archivos PDF", "*.pdf")])

    # Se muestra el nombre del archivo seleccionado.
    self.label_nombre_archivo.config(text=os.path.basename(archivo))

def abrir_plano(self):
    # Se obtiene la ruta del archivo seleccionado.
    archivo = os.path.join(os.getcwd(), "planos", self.label_nombre_archivo.cget("text"))

    # Se comprueba si el archivo existe.
    if os.path.isfile(archivo):
        # Se abre el archivo con el programa por defecto.
        os.startfile(archivo)
    else:
        messagebox.showwarning("Archivo no encontrado", "El archivo seleccionado no se encuentra en la carpeta de planos.")

def imprimir(self):
    # Se muestra un mensaje de confirmación.
    respuesta = messagebox.askyesno("Imprimir listado", "¿Desea imprimir el listado de artículos necesarios para la fabricación de la referencia?")

    if respuesta == True:
        # Se abre el archivo con el programa por defecto.
        os.startfile("listado.pdf")

def mostrar_comentario_incidencia(self, event):
    # Se comprueba si el estado seleccionado es incidencia.
    if self.campo_estado.get() == "Incidencia":
        self.campo_comentario_incidencia = Entry(self.frame_datos_referencia)
        self.campo_comentario_incidencia.grid(row=3, column=1, padx=5, pady=5)
    else:
        self.campo_comentario_incidencia.destroy()
        self.label_comentario_incidencia.grid(row=3, column=0, padx=5, pady=5)

def eliminar_referencia(self):
    # Se obtiene la referencia seleccionada.
    referencia = self.tabla_referencias.selection()

    # Se comprueba si se ha seleccionado una referencia.
    if len(referencia) == 0:
        messagebox.showwarning("Eliminar referencia", "Debe seleccionar una referencia para eliminar.")
    else:
        # Se muestra un mensaje de confirmación.
        respuesta = messagebox.askyesno("Eliminar referencia", "¿Está seguro de que desea eliminar la referencia seleccionada?")

        if respuesta == True:
            # Se elimina la referencia de la tabla de referencias.
            self.tabla_referencias.delete(referencia)

    def guardar_cambios(self):
    # Se obtienen los nuevos datos de la referencia.
    nueva_referencia = self.campo_referencia.get()
    nueva_fecha_entrega = self.campo_fecha_entrega.get()
    nuevo_estado = self.campo_estado.get()
    nuevo_comentario_incidencia = self.campo_comentario_incidencia.get("1.0", END)

    # Se actualiza la referencia en la lista de pedidos.
    for pedido in self.lista_pedidos:
        if pedido["Referencia"] == self.referencia_actual:
            pedido["Referencia"] = nueva_referencia
            pedido["Fecha de entrega"] = nueva_fecha_entrega
            pedido["Estado"] = nuevo_estado
            pedido["Comentario de incidencia"] = nuevo_comentario_incidencia

    # Se actualiza la lista de referencias en la interfaz.
    self.actualizar_lista_referencias()

    # Se cierra la ventana de la ficha de referencia.
    self.ventana_ficha_referencia.destroy()

def asignar_plano(self):
    # Se abre una ventana para seleccionar un archivo de plano.
    ruta_plano = filedialog.askopenfilename()

    # Se actualiza la referencia en la lista de pedidos.
    for pedido in self.lista_pedidos:
        if pedido["Referencia"] == self.referencia_actual:
            pedido["Plano"] = ruta_plano

    # Se actualiza la lista de referencias en la interfaz.
    self.actualizar_lista_referencias()

def abrir_plano(self):
    # Se obtiene la ruta del plano asignado a la referencia actual.
    for pedido in self.lista_pedidos:
        if pedido["Referencia"] == self.referencia_actual:
            ruta_plano = pedido["Plano"]
            break

    # Se abre el archivo de plano en el programa predeterminado del sistema operativo.
    os.startfile(ruta_plano)

def imprimir(self):
    # Se obtiene la lista de artículos necesarios para la fabricación de la referencia actual.
    for pedido in self.lista_pedidos:
        if pedido["Referencia"] == self.referencia_actual:
            articulos_necesarios = pedido["Artículos necesarios"]
            break

    # Se crea un archivo de texto con la lista de artículos necesarios.
    with open("listado_articulos.txt", "w") as archivo:
        archivo.write("Listado de artículos necesarios para la fabricación de la referencia:\n\n")
        for articulo in articulos_necesarios:
            archivo.write(f"{articulo['Cantidad']} x {articulo['Nombre']} ({articulo['Referencia']})\n")

    # Se abre el archivo de texto en el programa predeterminado del sistema operativo.
    os.startfile("listado_articulos.txt")

def mostrar_comentario_incidencia(self, event):
    # Se muestra o se oculta el campo de texto del comentario de incidencia según el estado seleccionado.
    estado_actual = self.campo_estado.get()
    if estado_actual == "Incidencia":
        self.campo_comentario_incidencia.pack()
        self.label_comentario_incidencia.pack()
    else:
        self.campo_comentario_incidencia.pack_forget()
        self.label_comentario_incidencia.pack_forget()

def main(self):
    # Se crea la ventana principal de la aplicación.
    self.ventana_principal = Tk()
    self.ventana_principal.title("Gestión de pedidos")
    self.ventana_principal.geometry("800x600")

    # Se crea un marco para los botones de la
        def main(self):
        # Se crea la ventana principal de la aplicación.
        self.ventana_principal = Tk()
        self.ventana_principal.title("Gestión de pedidos")
        self.ventana_principal.geometry("800x600")

        # Se crea un marco para los botones de navegación.
        self.frame_navegacion = Frame(self.ventana_principal, pady=10)
        self.frame_navegacion.pack()

        # Se añaden los botones de navegación.
        self.boton_pedidos = Button(self.frame_navegacion, text="Pedidos", command=self.mostrar_pedidos)
        self.boton_pedidos.pack(side="left", padx=10)

        self.boton_referencias = Button(self.frame_navegacion, text="Referencias", command=self.mostrar_referencias)
        self.boton_referencias.pack(side="left", padx=10)

        # Se llama al método para mostrar la ventana de pedidos.
        self.mostrar_pedidos()

        # Se lanza el bucle principal de la aplicación.
        self.ventana_principal.mainloop()


# Se crea una instancia de la clase y se lanza la aplicación.
app = GestionPedidos()
app.main()



            

