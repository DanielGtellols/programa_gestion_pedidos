import tkinter as tk
from tkinter import ttk, messagebox, filedialog

# Crear la clase de la vista
class VistaPedidos:
    def __init__(self):
        # Crear la ventana principal
        self.ventana_principal = tk.Tk()
        self.ventana_principal.title('Pedidos')

        # Crear el contenedor principal
        self.contenedor_principal = ttk.Frame(self.ventana_principal, padding=(30, 15))
        self.contenedor_principal.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

        # Crear la tabla de pedidos
        self.tabla_pedidos = ttk.Treeview(self.contenedor_principal, columns=('numero_pedido', 'cliente', 'fecha_recepcion'))
        self.tabla_pedidos.heading('numero_pedido', text='Número de pedido')
        self.tabla_pedidos.heading('cliente', text='Cliente')
        self.tabla_pedidos.heading('fecha_recepcion', text='Fecha de recepción')
        self.tabla_pedidos.column('numero_pedido', width=150)
        self.tabla_pedidos.column('cliente', width=150)
        self.tabla_pedidos.column('fecha_recepcion', width=150)
        self.tabla_pedidos.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

        # Crear el botón de añadir pedido
        self.boton_anadir_pedido = ttk.Button(self.contenedor_principal, text='Añadir pedido', command=self.mostrar_dialogo_anadir_pedido)
        self.boton_anadir_pedido.grid(column=0, row=1, sticky=tk.W)

        # Crear el botón de eliminar pedido
        self.boton_eliminar_pedido = ttk.Button(self.contenedor_principal, text='Eliminar pedido', command=self.eliminar_pedido_seleccionado)
        self.boton_eliminar_pedido.grid(column=1, row=1, sticky=tk.W)

        # Crear la tabla de referencias
        self.tabla_referencias = ttk.Treeview(self.contenedor_principal, columns=('nombre', 'cantidad', 'estado', 'comentario', 'fecha_entrega'))
        self.tabla_referencias.heading('nombre', text='Nombre')
        self.tabla_referencias.heading('cantidad', text='Cantidad')
        self.tabla_referencias.heading('estado', text='Estado')
        self.tabla_referencias.heading('comentario', text='Comentario')
        self.tabla_referencias.heading('fecha_entrega', text='Fecha de entrega')
        self.tabla_referencias.column('nombre', width=150)
        self.tabla_referencias.column('cantidad', width=150)
        self.tabla_referencias.column('estado', width=150)
        self.tabla_referencias.column('comentario', width=150)
        self.tabla_referencias.column('fecha_entrega', width=150)
        self.tabla_referencias.grid(column=0, row=2, columnspan=2, sticky=(tk.N, tk.W, tk.E, tk.S))
# Crear el botón de añadir referencia
        self.boton_anadir_referencia = ttk.Button(self.contenedor_principal, text='Añadir referencia', command=self.mostrar_dialogo_anadir_referencia)
        self.boton_anadir_referencia.grid(column=0, row=3, sticky=tk.W)

# Crear el botón de eliminar referencia
        self.boton_eliminar_referencia = ttk.Button(self.contenedor_principal, text='Eliminar referencia', command=self.eliminar_referencia_seleccionada)
        self.boton_eliminar_referencia.grid(column=1, row=3, sticky=tk.W)


    # Configurar el comportamiento de la ventana al cerrarla
    self.ventana_principal.protocol("WM_DELETE_WINDOW", self.cerrar_aplicacion)

def iniciar_aplicacion(self):
    # Arrancar la aplicación
    self.ventana_principal.mainloop()

def mostrar_dialogo_anadir_pedido(self):
    # Mostrar un diálogo para añadir un nuevo pedido
    pass

def eliminar_pedido_seleccionado(self):
    # Eliminar el pedido seleccionado en la tabla de pedidos
    pass

def mostrar_dialogo_anadir_referencia(self):
    # Mostrar un diálogo para añadir una nueva referencia al pedido seleccionado
    pass

def eliminar_referencia_seleccionada(self):
    # Eliminar la referencia seleccionada en la tabla de referencias
    pass

def cerrar_aplicacion(self):
    # Cerrar la aplicación
    self.ventana_principal.destroy()

def eliminar_referencia_seleccionada(self):
    referencia_seleccionada = self.tabla_referencias.focus()
    if referencia_seleccionada():
        referencia = self.tabla_referencias.item(referencia_seleccionada)
        pedido = self.pedido_seleccionado
        if referencia and pedido:
            referencia_id = referencia['values'][0]
            for i, ref in enumerate(pedido.referencias):
                if ref.id == referencia_id:
                    del pedido.referencias[i]
                    break
            self.tabla_referencias.delete(referencia_seleccionada)
    # Método para mostrar el diálogo de añadir pedido
    def mostrar_dialogo_anadir_pedido(self):
        dialogo_anadir_pedido = tk.Toplevel()
        dialogo_anadir_pedido.title('Añadir pedido')

        # Crear el contenedor principal del diálogo
        contenedor_principal = ttk.Frame(dialogo_anadir_pedido, padding=(30, 15))
        contenedor_principal.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

        # Crear las etiquetas y los campos de entrada del diálogo
        etiqueta_numero_pedido = ttk.Label(contenedor_principal, text='Número de pedido:')
        etiqueta_numero_pedido.grid(column=0, row=0, sticky=tk.W)
        campo_numero_pedido = ttk.Entry(contenedor_principal)
        campo_numero_pedido.grid(column=1, row=0, sticky=tk.W)

        etiqueta_cliente = ttk.Label(contenedor_principal, text='Cliente:')
        etiqueta_cliente.grid(column=0, row=1, sticky=tk.W)
        campo_cliente = ttk.Entry(contenedor_principal)
        campo_cliente.grid(column=1, row=1, sticky=tk.W)

        etiqueta_fecha_recepcion = ttk.Label(contenedor_principal, text='Fecha de recepción:')
        etiqueta_fecha_recepcion.grid(column=0, row=2, sticky=tk.W)
        campo_fecha_recepcion = ttk.Entry(contenedor_principal)
        campo_fecha_recepcion.grid(column=1, row=2, sticky=tk.W)

        # Crear los botones del diálogo
        boton_cancelar = ttk.Button(contenedor_principal, text='Cancelar', command=dialogo_anadir_pedido.destroy)
        boton_cancelar.grid(column=0, row=3, sticky=tk.E)

        boton_guardar = ttk.Button(contenedor_principal, text='Guardar', command=lambda: self.guardar_pedido(campo_numero_pedido.get(), campo_cliente.get(), campo_fecha_recepcion.get(), dialogo_anadir_pedido))
        boton_guardar.grid(column=1, row=3, sticky=tk.E)


    # Método para guardar un nuevo pedido
    def guardar_pedido(self, numero_pedido, cliente, fecha_recepcion, dialogo_anadir_pedido):
        # TODO: Implementar la lógica para guardar un nuevo pedido en la base de datos
        self.tabla_pedidos.insert('', 'end', text=numero_pedido, values=(numero_pedido, cliente, fecha_recepcion))
        dialogo_anadir_pedido.withdraw()


    # Método para eliminar el pedido seleccionado de la tabla de pedidos
    def eliminar_pedido_seleccionado(self):
        # Obtener el elemento seleccionado en la tabla de pedidos
        item_seleccionado = self.tabla_pedidos.focus()

        # Comprobar que se ha seleccionado un elemento
        if not item_seleccionado:
            messagebox.showwarning('Eliminar pedido', 'Por favor, seleccione un pedido.')
            return

        # Obtener el número de pedido del elemento seleccionado
        numero_pedido = self.tabla_pedidos.item(item_seleccionado)['text']

        # Preguntar al usuario si está seguro de que desea eliminar el pedido
        confirmacion = messagebox.askyesno('Eliminar pedido', f'¿Está seguro de que desea eliminar el pedido {numero_pedido}?')

        if confirmacion:
            # TODO: Implementar la lógica para eliminar el pedido de la base de datos
            self.tabla_pedidos.delete(item_seleccionado)
 # Configurar el comportamiento de la ventana al cerrarla
self.ventana_principal.protocol('WM_DELETE_WINDOW', self.cerrar_programa)

# Inicializar la lista de pedidos
self.lista_pedidos = []

# Iniciar la ventana principal
self.ventana_principal.mainloop()

# Método para mostrar el diálogo de añadir pedido
   def mostrar_dialogo_anadir_pedido(self):
    # Crear la ventana de diálogo
    self.dialogo_anadir_pedido = tk.Toplevel(self.ventana_principal)
    self.dialogo_anadir_pedido.title('Añadir pedido')

    # Crear el contenedor principal
    contenedor_principal = ttk.Frame(self.dialogo_anadir_pedido, padding=(30, 15))
    contenedor_principal.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

    # Crear los campos de entrada
    ttk.Label(contenedor_principal, text='Número de pedido:').grid(column=0, row=0, sticky=tk.W)
    numero_pedido = ttk.Entry(contenedor_principal, width=30)
    numero_pedido.grid(column=1, row=0, sticky=tk.W)

    ttk.Label(contenedor_principal, text='Cliente:').grid(column=0, row=1, sticky=tk.W)
    cliente = ttk.Entry(contenedor_principal, width=30)
    cliente.grid(column=1, row=1, sticky=tk.W)

    ttk.Label(contenedor_principal, text='Fecha de recepción:').grid(column=0, row=2, sticky=tk.W)
    fecha_recepcion = ttk.Entry(contenedor_principal, width=30)
    fecha_recepcion.grid(column=1, row=2, sticky=tk.W)

    # Crear el botón de añadir
    boton_anadir = ttk.Button(contenedor_principal, text='Añadir', command=lambda: self.anadir_pedido(numero_pedido.get(), cliente.get(), fecha_recepcion.get()))
    boton_anadir.grid(column=0, row=3, columnspan=2)

    # Configurar el comportamiento de la ventana al cerrarla
    self.dialogo_anadir_pedido.protocol('WM_DELETE_WINDOW', self.cerrar_dialogo_anadir_pedido)

    # Centrar la ventana de diálogo en la pantalla
    self.centra_ventana(self.dialogo_anadir_pedido)

# Método para añadir un pedido a la lista de pedidos
   def anadir_pedido(self, numero_pedido, cliente, fecha_recepcion):
    # Comprobar que todos los campos están rellenados
    if not numero_pedido or not cliente or not fecha_recepcion:
        messagebox.showerror('Error', 'Por favor, rellena todos los campos')
        return

    # Añadir el pedido a la lista de pedidos
    self.lista_pedidos.append({'numero_pedido': numero_pedido, 'cliente': cliente, 'fecha_recepcion': fecha_recepcion})

    # Añadir el pedido a la tabla de pedidos
    self.tabla_pedidos.insert('', 'end', text=numero_pedido, values=(numero_pedido, cliente, fecha_recepcion))

    # Cerrar el diálogo de añadir pedido
    self.cerrar_dialogo_anadir_pedido()

# Método para cerrar el diálogo de añadir pedido
   def cerrar_dialogo_anadir_pedido(self):
    self.dialogo_anadir_pedido.withdraw()

   # Método para eliminar el pedido seleccionado de la lista de pedidos y de la tabla de pedidos
   def eliminar_pedido_seleccionado(self):
    # Crear la clase de la vista
class VistaPedidos:
    def __init__(self):
        # Crear la ventana principal
        self.ventana_principal = tk.Tk()
        self.ventana_principal.title('Pedidos')

        # Crear el contenedor principal
        self.contenedor_principal = ttk.Frame(self.ventana_principal, padding=(30, 15))
        self.contenedor_principal.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

        # Crear la tabla de pedidos
        self.tabla_pedidos = ttk.Treeview(self.contenedor_principal, columns=('numero_pedido', 'cliente', 'fecha_recepcion'))
        self.tabla_pedidos.heading('numero_pedido', text='Número de pedido')
        self.tabla_pedidos.heading('cliente', text='Cliente')
        self.tabla_pedidos.heading('fecha_recepcion', text='Fecha de recepción')
        self.tabla_pedidos.column('numero_pedido', width=150)
        self.tabla_pedidos.column('cliente', width=150)
        self.tabla_pedidos.column('fecha_recepcion', width=150)
        self.tabla_pedidos.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

        # Crear el botón de añadir pedido
        self.boton_anadir_pedido = ttk.Button(self.contenedor_principal, text='Añadir pedido', command=self.mostrar_dialogo_anadir_pedido)
        self.boton_anadir_pedido.grid(column=0, row=1, sticky=tk.W)

        # Crear el botón de eliminar pedido
        self.boton_eliminar_pedido = ttk.Button(self.contenedor_principal, text='Eliminar pedido', command=self.eliminar_pedido_seleccionado)
        self.boton_eliminar_pedido.grid(column=1, row=1, sticky=tk.W)

        # Crear la tabla de referencias
        self.tabla_referencias = ttk.Treeview(self.contenedor_principal, columns=('nombre', 'cantidad', 'estado', 'comentario', 'fecha_entrega'))
        self.tabla_referencias.heading('nombre', text='Nombre')
        self.tabla_referencias.heading('cantidad', text='Cantidad')
        self.tabla_referencias.heading('estado', text='Estado')
        self.tabla_referencias.heading('comentario', text='Comentario')
        self.tabla_referencias.heading('fecha_entrega', text='Fecha de entrega')
        self.tabla_referencias.column('nombre', width=150)
        self.tabla_referencias.column('cantidad', width=150)
        self.tabla_referencias.column('estado', width=150)
        self.tabla_referencias.column('comentario', width=150)
        self.tabla_referencias.column('fecha_entrega', width=150)
        self.tabla_referencias.grid(column=0, row=2, columnspan=2, sticky=(tk.N, tk.W, tk.E, tk.S))
        
        # Crear el botón de añadir referencia
        self.boton_anadir_referencia = ttk.Button(self.contenedor_principal, text='Añadir referencia', command=self.mostrar_dialogo_anadir_referencia)
        self.boton_anadir_referencia.grid(column=0, row=3, sticky=tk.W)

        # Crear el botón de eliminar referencia

        def mostrar_dialogo_anadir_pedido(self):
    dialogo_anadir_pedido = tk.Toplevel()
    dialogo_anadir_pedido.title('Añadir pedido')

    # Crear el contenedor principal del diálogo
    contenedor_principal = ttk.Frame(dialogo_anadir_pedido, padding=(30, 15))
    contenedor_principal.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

    # Crear los campos de entrada del número de pedido, cliente y fecha de recepción
    ttk.Label(contenedor_principal, text='Número de pedido:').grid(column=0, row=0, sticky=tk.W)
    numero_pedido = tk.StringVar()
    ttk.Entry(contenedor_principal, width=30, textvariable=numero_pedido).grid(column=1, row=0, sticky=tk.W)

    ttk.Label(contenedor_principal, text='Cliente:').grid(column=0, row=1, sticky=tk.W)
    cliente = tk.StringVar()
    ttk.Entry(contenedor_principal, width=30, textvariable=cliente).grid(column=1, row=1, sticky=tk.W)

    ttk.Label(contenedor_principal, text='Fecha de recepción:').grid(column=0, row=2, sticky=tk.W)
    fecha_recepcion = tk.StringVar()
    ttk.Entry(contenedor_principal, width=30, textvariable=fecha_recepcion).grid(column=1, row=2, sticky=tk.W)

    # Crear el botón de añadir pedido
    ttk.Button(contenedor_principal, text='Añadir', command=lambda: self.añadir_pedido(numero_pedido.get(), cliente.get(), fecha_recepcion.get())).grid(column=0, row=3, sticky=tk.W)

# Método para añadir un pedido a la tabla de pedidos
   def añadir_pedido(self, numero_pedido, cliente, fecha_recepcion):
    # Crear un objeto Pedido y añadirlo a la lista de pedidos
    pedido = Pedido(numero_pedido, cliente, fecha_recepcion)
    self.lista_pedidos.append(pedido)

    # Añadir el pedido a la tabla de pedidos
    self.tabla_pedidos.insert('', 'end', values=(pedido.numero_pedido, pedido.cliente, pedido.fecha_recepcion))

    # Cerrar el diálogo de añadir pedido
    self.dialogo_anadir_pedido.withdraw()

# Método para eliminar el pedido seleccionado en la tabla de pedidos
   def eliminar_pedido_seleccionado(self):
    # Obtener el pedido seleccionado en la tabla de pedidos
    pedido_seleccionado = self.tabla_pedidos.focus()
    if pedido_seleccionado:
        # Eliminar el pedido de la lista de pedidos
        pedido = self.lista_pedidos[self.tabla_pedidos.index(pedido_seleccionado)]
        self.lista_pedidos.remove(pedido)

        # Eliminar el pedido de la tabla de pedidos
        self.tabla_pedidos.delete(pedido_seleccionado)

        # Eliminar las referencias del pedido de la tabla de referencias
        for referencia in pedido.referencias:
            self.tabla_referencias.delete(referencia.id)

# Método para mostrar el diálogo de añadir referencia
   def mostrar_dialogo_anadir_referencia(self):
    dialogo_anadir_referencia = tk.Toplevel()
    dialogo_anadir_referencia.title('Añadir referencia')

    # Crear el contenedor principal del diálogo
    contenedor_principal = ttk.Frame(dialogo_anadir_referencia, padding=(30, 15))
    contenedor_principal.grid(column=0, row   
    class ReferenceCard:
    def __init__(self, reference, delivery_date, status, comment):
        self.reference = reference
        self.delivery_date = delivery_date
        self.status = status
        self.comment = comment
        self.articles = []

    def add_article(self, article):
        self.articles.append(article)

class Article:
    def __init__(self, quantity, reference, description, comment):
        self.quantity = quantity
        self.reference = reference
        self.description = description
        self.comment = comment

class ReferenceCardWindow(QMainWindow):
    def __init__(self, reference_card):
        super().__init__()

        self.reference_card = reference_card

        self.setWindowTitle("Ficha de Referencia")

        # Crear widgets de la ventana
        self.reference_label = QLabel("Referencia: " + self.reference_card.reference)
        self.delivery_date_label = QLabel("Fecha de Entrega: " + self.reference_card.delivery_date)
        self.status_label = QLabel("Estado: ")
        self.status_combo = QComboBox()
        self.status_combo.addItems(["Entregado", "En fabricación", "Pedido", "Incidencia"])
        self.status_combo.setCurrentText(self.reference_card.status)
        self.status_comment_label = QLabel("Comentario:")
        self.status_comment_edit = QTextEdit(self.reference_card.comment)
        self.articles_table = QTableWidget()
        self.articles_table.setColumnCount(4)
        self.articles_table.setHorizontalHeaderLabels(["Cantidad", "Referencia", "Descripción", "Comentario"])
        self.add_article_button = QPushButton("Añadir artículo")
        self.delete_article_button = QPushButton("Eliminar artículo")

        # Configurar layout de la ventana
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        grid_layout = QGridLayout()
        central_widget.setLayout(grid_layout)
        grid_layout.addWidget(self.reference_label, 0, 0)
        grid_layout.addWidget(self.delivery_date_label, 1, 0)
        grid_layout.addWidget(self.status_label, 2, 0)
        grid_layout.addWidget(self.status_combo, 2, 1)
        grid_layout.addWidget(self.status_comment_label, 3, 0)
        grid_layout.addWidget(self.status_comment_edit, 4, 0, 1, 2)
        grid_layout.addWidget(self.articles_table, 5, 0, 1, 2)
        grid_layout.addWidget(self.add_article_button, 6, 0)
        grid_layout.addWidget(self.delete_article_button, 6, 1)

        # Conectar botones a funciones
        self.add_article_button.clicked.connect(self.add_article)
        self.delete_article_button.clicked.connect(self.delete_article)

        # Rellenar tabla de artículos
        self.update_articles_table()

    def add_article(self):
        article_dialog = AddArticleDialog()
        if article_dialog.exec_():
            article = article_dialog.get_article()
            self.reference_card.add_article(article)
            self.update_articles_table()

    def delete_article(self):
        selected_rows = set([index.row() for index in self.articles_table.selectedIndexes()])
        self.reference_card.articles = [article for i, article in enumerate(self.reference_card.articles) if i not in selected_rows]
        self.update_articles_table()

    def update_articles_table(self):
        self.articles_table.setRowCount(len(self.reference_card.articles))
        for row, article in enumerate(self.reference_card.articles):
            quantity_item = QTableWidgetItem(str(article.quantity))
            reference_item = QTableWidgetItem(article.reference)
            description_item = QTableWidgetItem(article.description)
            comment_item = QTableWidgetItem(article.comment)
            self.articles_table.setItem(row,
        
 import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from reportlab.lib.pagesizes import letter, landscape
from reportlab.pdfgen import canvas

# Clase para la ventana principal
class PedidosApp:

    def __init__(self, master):
        self.master = master
        master.title("Pedidos y fabricación")
        master.resizable(False, False)

        # Variables de control para los campos de entrada
        self.pedido_num_var = tk.StringVar()
        self.cliente_var = tk.StringVar()
        self.fecha_rec_var = tk.StringVar()
        self.ref_var = tk.StringVar()
        self.fecha_ent_var = tk.StringVar()
        self.estado_var = tk.StringVar()
        self.comentario_var = tk.StringVar()
        self.cantidad_var = tk.StringVar()
        self.articulo_var = tk.StringVar()
        self.descripcion_var = tk.StringVar()
        self.comment_art_var = tk.StringVar()

        # Variables para los widgets de Treeview
        self.pedido_treeview = None
        self.ref_treeview = None
        self.articulo_treeview = None

        # Lista de pedidos
        self.pedidos = []

        # Llamada a la función para cargar los pedidos guardados
        self.cargar_pedidos()

        # Creación de los widgets de la ventana principal
        self.create_widgets()

    def create_widgets(self):
        # Etiqueta y campo de entrada para el número de pedido
        pedido_num_label = ttk.Label(self.master, text="Número de pedido:")
        pedido_num_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        pedido_num_entry = ttk.Entry(self.master, textvariable=self.pedido_num_var)
        pedido_num_entry.grid(row=0, column=1, padx=5, pady=5)

        # Etiqueta y campo de entrada para el cliente
        cliente_label = ttk.Label(self.master, text="Cliente:")
        cliente_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        cliente_entry = ttk.Entry(self.master, textvariable=self.cliente_var)
        cliente_entry.grid(row=1, column=1, padx=5, pady=5)

        # Etiqueta y campo de entrada para la fecha de recepción
        fecha_rec_label = ttk.Label(self.master, text="Fecha de recepción:")
        fecha_rec_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        fecha_rec_entry = ttk.Entry(self.master, textvariable=self.fecha_rec_var)
        fecha_rec_entry.grid(row=2, column=1, padx=5, pady=5)

        # Botón para añadir un pedido
        add_pedido_button = ttk.Button(self.master, text="Añadir pedido", command=self.add_pedido)
        add_pedido_button.grid(row=0
   import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

class Pedido:
    def __init__(self, num_pedido, cliente, fecha_recepcion):
        self.num_pedido = num_pedido
        self.cliente = cliente
        self.fecha_recepcion = fecha_recepcion
        self.referencias = []

... class Referencia:
...     def __init__(self, referencia, fecha_entrega, estado, comentario=None):
...         self.referencia = referencia
...         self.fecha_entrega = fecha_entrega
...         self.estado = estado
...         self.comentario = comentario
...         self.articulos = []
... 
... class Articulo:
...     def __init__(self, cantidad, referencia, descripcion, comentario=None):
...         self.cantidad = cantidad
...         self.referencia = referencia
...         self.descripcion = descripcion
...         self.comentario = comentario
... 
... class Application(tk.Frame):
...     def __init__(self, master=None):
...         super().__init__(master)
...         self.master = master
...         self.master.title("Gestión de Pedidos y Fabricación")
...         self.master.geometry("800x600")
...         self.create_widgets()
... 
...     def create_widgets(self):
...         # Crear el treeview para mostrar la lista de pedidos
...         self.treeview_pedidos = ttk.Treeview(self.master, columns=("num_pedido", "cliente", "fecha_recepcion"))
...         self.treeview_pedidos.heading("#0", text="Pedido")
...         self.treeview_pedidos.heading("num_pedido", text="Número de Pedido")
...         self.treeview_pedidos.heading("cliente", text="Cliente")
...         self.treeview_pedidos.heading("fecha_recepcion", text="Fecha de Recepción")
...         self.treeview_pedidos.bind("<Double-1>", self.on_pedidos_select)
...         self.treeview_pedidos.pack(side="left", fill="y")
... 
...         # Crear los botones para añadir, editar y borrar pedidos
...         self.button_add_pedido = ttk.Button(self.master, text="Añadir Pedido", command=self.add_pedido)
...         self.button_add_pedido.pack(side="top", padx=10, pady=10)
... 
...         self.button_edit_pedido = ttk.Button(self.master, text="Editar Pedido", command=self.edit_pedido)
...         self.button_edit_pedido.pack(side="top", padx=10, pady=10)
... 
...         self.button_delete_pedido = ttk.Button(self.master, text="Borrar Pedido", command=self.delete_pedido)
...         self.button_delete_pedido.pack(side="top", padx=10, pady=10)
... 
...         # Crear los campos de entrada para el formulario de pedido
...         self.label_num_pedido = ttk.Label(self.master, text="Número de Pedido")
...         self.label_num_pedido.pack(side="top", padx=10, pady=10)
... 
...         self.entry_num_pedido = ttk.Entry(self.master)
...         self.entry_num_pedido.pack(side="top", padx=10, pady=10)
... 
...         self.label_cliente = ttk.Label(self.master, text="Cliente")
...         self.label_cliente.pack(side="top", padx=10, pady=10)
... 
...         self.entry_cliente = ttk.Entry(self.master)
...         self.entry_cliente.pack(side="top", padx=10, pady=10)
... 
...         self.label_fecha_recepcion = ttk.Label(self.master, text="Fecha de Recepción")
...         self.label_fecha_recepcion.pack(side="top", padx=10, pady=10)
... 
...         self.entry_fecha_recepcion = ttk.Entry(self.master)
...         self.entry_fecha_recepcion.pack(side="top", padx=10, pady=10)
... 
  class NuevaReferencia(tk.Toplevel):
    def __init__(self, parent, pedido):
        super().__init__(parent)
        self.pedido = pedido
        self.title("Nueva Referencia")
        
        tk.Label(self, text="Referencia").grid(row=0, column=0)
        self.referencia_entry = tk.Entry(self)
        self.referencia_entry.grid(row=0, column=1)
        
        tk.Label(self, text="Fecha de Entrega").grid(row=1, column=0)
        self.fecha_entry = tk.Entry(self)
        self.fecha_entry.grid(row=1, column=1)
        
        tk.Label(self, text="Estado").grid(row=2, column=0)
        self.estado_entry = tk.StringVar(self)
        self.estado_entry.set("Pedido")
        self.estado_menu = tk.OptionMenu(self, self.estado_entry, "Entregado", "En Fabricación", "Pedido", "Incidencia")
        self.estado_menu.grid(row=2, column=1)
        
        tk.Button(self, text="Guardar", command=self.guardar_referencia).grid(row=3, column=1)
    
    def guardar_referencia(self):
        referencia = self.referencia_entry.get()
        fecha = self.fecha_entry.get()
        estado = self.estado_entry.get()
        self.pedido.agregar_referencia(referencia, fecha, estado)
        self.withdraw()
class DetallesPedido(tk.Toplevel):
    def __init__(self, parent, pedido):
        super().__init__(parent)
        self.pedido = pedido
        self.title(f"Pedido {self.pedido.numero}")
        
        # listamos las referencias del pedido
        tk.Label(self, text="Referencias:").grid(row=0, column=0)
        self.referencias_listbox = tk.Listbox(self, width=50)
        self.referencias_listbox.grid(row=1, column=0, columnspan=2)
        for referencia in self.pedido.referencias:
            self.referencias_listbox.insert(tk.END, referencia)
        
        # botones de edición
        tk.Button(self, text="Editar Pedido", command=self.editar_pedido).grid(row=2, column=0)
        tk.Button(self, text="Nueva Referencia", command=self.nueva_referencia).grid(row=2, column=1)
        tk.Button(self, text="Eliminar Pedido", command=self.eliminar_pedido).grid(row=2, column=2)
        
        # detalles de la referencia seleccionada
        self.referencias_listbox.bind("<<ListboxSelect>>", self.mostrar_detalle_referencia)
        tk.Label(self, text="Referencia Seleccionada:").grid(row=3, column=0)
        self.referencia_seleccionada_label = tk.Label(self, text="")
...         self.referencia_seleccionada_label.grid(row=3, column=1)
...         
...         tk.Label(self, text="Detalles de Referencia:").grid(row=4, column=0)
...         self.detalle_referencia_textbox = tk.Text(self, width=50, height=10)
...         self.detalle_referencia_textbox.grid(row=5, column=0,
... 
... import tkinter as tk
... 
... class Article:
...     def __init__(self, quantity, reference, description, comment):
...         self.quantity = quantity
...         self.reference = reference
...         self.description = description
...         self.comment = comment
... 
... class Reference:
...     def __init__(self, reference_number, delivery_date, status, comment=""):
...         self.reference_number = reference_number
...         self.delivery_date = delivery_date
...         self.status = status
...         self.comment = comment
...         self.article_list = []
... 
... class Order:
...     def __init__(self, order_number, client, reception_date):
...         self.order_number = order_number
...         self.client = client
...         self.reception_date = reception_date
...         self.reference_list = []
... 
... class Application(tk.Tk):
...     def __init__(self):
...         super().__init__()
...         self.title("Gestión de pedidos y fabricación")
...         self.geometry("800x600")
... 
... if __name__ == "__main__":
...     app = Application()
...     app.mainloop()
