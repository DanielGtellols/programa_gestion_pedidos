import tkinter as tk
from tkinter import ttk
 
class PedidoGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Gestión de Pedidos")
    
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="30 15 30 15")
        main_frame.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
 
        # Label para el número de pedido
        ttk.Label(main_frame, text="Número de Pedido").grid(column=0, row=0, sticky=tk.W)
        self.num_pedido_entry = ttk.Entry(main_frame, width=20)
        self.num_pedido_entry.grid(column=1, row=0, sticky=tk.W)
    
        # Label para el cliente
        ttk.Label(main_frame, text="Cliente").grid(column=0, row=1, sticky=tk.W)
        self.cliente_entry = ttk.Entry(main_frame, width=20)
        self.cliente_entry.grid(column=1, row=1, sticky=tk.W)
 
        # Label para la fecha de recepción
        ttk.Label(main_frame, text="Fecha de Recepción").grid(column=0, row=2, sticky=tk.W)
        self.fecha_recepcion_entry = ttk.Entry(main_frame, width=20)
        self.fecha_recepcion_entry.grid(column=1, row=2, sticky=tk.W)
    
        # Botón para añadir un nuevo pedido
        ttk.Button(main_frame, text="Añadir Pedido", command=self.add_pedido).grid(column=1, row=3, sticky=tk.W)
 
        # Treeview para listar los pedidos existentes
        self.tree = ttk.Treeview(main_frame, columns=("num_pedido", "cliente", "fecha_recepcion"), selectmode="browse")
        self.tree.column("#0", width=0, stretch=tk.NO)
        self.tree.column("num_pedido", anchor=tk.CENTER, width=120)
        self.tree.column("cliente", anchor=tk.CENTER, width=120)
        self.tree.column("fecha_recepcion", anchor=tk.CENTER, width=120)
        self.tree.heading("num_pedido", text="Número de Pedido")
        self.tree.heading("cliente", text="Cliente")
        self.tree.heading("fecha_recepcion", text="Fecha de Recepción")
        self.tree.grid(column=0, row=4, columnspan=2, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.tree.bind("<Double-1>", self.show_pedido)

        # Botón para editar un pedido seleccionado
        ttk.Button(main_frame, text="Editar Pedido", command=self.edit_pedido).grid(column=0, row=5, sticky=tk.W)

        # Botón para eliminar un pedido seleccionado
        ttk.Button(main_frame, text="Eliminar Pedido", command=self.delete_pedido).grid(column=1, row=5, sticky=tk.W)

        self.root.mainloop()

    def add_pedido(self):
        pass

    def edit_pedido(self):
        pass

    def delete_pedido(self):
        pass

    def show_pedido(self, event):
        pass

  if __name__ == '__main__':
    app = PedidoGUI()

cclass RefsPedidoWindow(QtWidgets.QWidget):
    def __init__(self, pedido):
        super().__init__()
        self.pedido = pedido
        self.setWindowTitle("Referencias del Pedido")
        self.setGeometry(100, 100, 600, 400)

SyntaxError: multiple statements found while compiling a single statement
    # Crear tabla de referencias
    self.table_refs = QtWidgets.QTableWidget(self)
    self.table_refs.setRowCount(len(self.pedido.referencias))
    self.table_refs.setColumnCount(3)
    self.table_refs.setHorizontalHeaderLabels(['Referencia', 'Fecha de Entrega', 'Estado'])

    # Rellenar tabla de referencias
    for i, ref in enumerate(self.pedido.referencias):
        self.table_refs.setItem(i, 0, QtWidgets.QTableWidgetItem(ref.referencia))
        self.table_refs.setItem(i, 1, QtWidgets.QTableWidgetItem(ref.fecha_entrega))
        self.table_refs.setItem(i, 2, QtWidgets.QTableWidgetItem(ref.estado))

    # Añadir botones
    self.button_add_ref = QtWidgets.QPushButton('Añadir Referencia')
    self.button_edit_ref = QtWidgets.QPushButton('Editar Referencia')
    self.button_delete_ref = QtWidgets.QPushButton('Borrar Referencia')
    self.button_back = QtWidgets.QPushButton('Volver al Pedido')

    # Añadir layout
    layout = QtWidgets.QVBoxLayout(self)
    layout.addWidget(self.table_refs)
    layout.addWidget(self.button_add_ref)
    layout.addWidget(self.button_edit_ref)
    layout.addWidget(self.button_delete_ref)
    layout.addWidget(self.button_back)

    # Conectar botones a funciones
    self.button_add_ref.clicked.connect(self.add_ref)
    self.button_edit_ref.clicked.connect(self.edit_ref)
    self.button_delete_ref.clicked.connect(self.delete_ref)
    self.button_back.clicked.connect(self.back_to_pedido)

def add_ref(self):
    # Abrir ventana para añadir referencia
    ref_window = AddRefWindow(self.pedido)
    ref_window.exec_()
    # Refrescar tabla de referencias
    self.refresh_table_refs()

def edit_ref(self):
    # Obtener referencia seleccionada
    selected_refs = self.table_refs.selectedIndexes()
    if len(selected_refs) == 0:
        return
    ref_index = selected_refs[0].row()
    ref = self.pedido.referencias[ref_index]
    # Abrir ventana para editar referencia
    ref_window = EditRefWindow(ref)
    ref_window.exec_()
    # Refrescar tabla de referencias
    self.refresh_table_refs()

def delete_ref(self):
    # Obtener referencia seleccionada
    selected_refs = self.table_refs.selectedIndexes()
    if len(selected_refs) == 0:
        return
    ref_index = selected_refs[0].row()
    # Eliminar referencia del pedido
    self.pedido.eliminar_referencia(ref_index)
    # Refrescar tabla de referencias
    self.refresh_table_refs()

def refresh_table_refs(self):
    # Refrescar tabla de referencias
    self.table_refs.setRowCount(len(self.pedido.referencias))
    for i, ref in enumerate(self.pedido.referencias):
        self.table_refs.setItem(i, 0, QtWidgets.QTableWidgetItem(ref.referencia))
        self.table_refs.setItem(i, 1, QtWidgets.QTableWidgetItem(ref.fecha_entrega))
        self.table_refs.setItem(i, 2, QtWidgets.QTableWidgetItem(ref.estado))

def back_to_pedido(self):
    # Volver a ventana de pedido
    self.close()
    self.parent().show()
class Referencia:
    def __init__(self, referencia, fecha_entrega, estado, comentario):
        self.referencia = referencia
        self.fecha_entrega = fecha_entrega
        self.estado = estado
        self.comentario = comentario
        self.articulos = []

    def agregar_articulo(self, articulo):
        self.articulos.append(articulo)

    def eliminar_articulo(self, articulo):
        self.articulos.remove(articulo)

    def editar_articulo(self, articulo, cantidad, referencia, descripcion, comentario):
        articulo.cantidad = cantidad
        articulo.referencia = referencia
        articulo.descripcion = descripcion
        articulo.comentario = comentario

class Articulo:
    def __init__(self, cantidad, referencia, descripcion, comentario):
        self.cantidad = cantidad
        self.referencia = referencia
        self.descripcion = descripcion
        self.comentario = comentario

class ReferenciaFicha(QWidget):
    def __init__(self, referencia):
        super().__init__()
        self.referencia = referencia
        self.initUI()

    def initUI(self):
        # Crear la tabla de artículos
        self.tabla = QTableWidget()
        self.tabla.setColumnCount(4)
        self.tabla.setHorizontalHeaderLabels(["Cantidad", "Referencia", "Descripción", "Comentario"])
        self.tabla.setRowCount(len(self.referencia.articulos))

        # Llenar la tabla de artículos
        for i, articulo in enumerate(self.referencia.articulos):
            cantidad = QTableWidgetItem(str(articulo.cantidad))
            referencia = QTableWidgetItem(articulo.referencia)
            descripcion = QTableWidgetItem(articulo.descripcion)
            comentario = QTableWidgetItem(articulo.comentario)

            self.tabla.setItem(i, 0, cantidad)
            self.tabla.setItem(i, 1, referencia)
            self.tabla.setItem(i, 2, descripcion)
            self.tabla.setItem(i, 3, comentario)

        # Crear los botones de agregar, eliminar y editar
        btn_agregar = QPushButton("Agregar")
        btn_eliminar = QPushButton("Eliminar")
        btn_editar = QPushButton("Editar")

        # Agregar los botones a un layout
        layout_botones = QHBoxLayout()
        layout_botones.addWidget(btn_agregar)
        layout_botones.addWidget(btn_eliminar)
        layout_botones.addWidget(btn_editar)

        # Crear el layout principal
        layout_principal = QVBoxLayout()
        layout_principal.addWidget(self.tabla)
        layout_principal.addLayout(layout_botones)

        # Establecer el layout principal
        self.setLayout(layout_principal)

        # Conectar las señales de los botones a sus respectivas funciones
        btn_agregar.clicked.connect(self.agregar_articulo)
        btn_eliminar.clicked.connect(self.eliminar_articulo)
        btn_editar.clicked.connect(self.editar_articulo)

    def agregar_articulo(self):
    # Obtener la referencia seleccionada
    ref_sel = self.list_ref.get(self.list_ref.curselection())

    # Crear ventana para agregar un nuevo artículo
    win_agregar_art = Toplevel()
    win_agregar_art.title("Agregar artículo")

    # Campos para introducir los datos del artículo
    lbl_ref = Label(win_agregar_art, text="Referencia:")
    lbl_ref.grid(row=0, column=0, padx=5, pady=5)
    lbl_ref_val = Label(win_agregar_art, text=ref_sel)
    lbl_ref_val.grid(row=0, column=1, padx=5, pady=5)

    lbl_cant = Label(win_agregar_art, text="Cantidad:")
    lbl_cant.grid(row=1, column=0, padx=5, pady=5)
    ent_cant = Entry(win_agregar_art)
    ent_cant.grid(row=1, column=1, padx=5, pady=5)

    lbl_desc = Label(win_agregar_art, text="Descripción:")
    lbl_desc.grid(row=2, column=0, padx=5, pady=5)
    ent_desc = Entry(win_agregar_art)
    ent_desc.grid(row=2, column=1, padx=5, pady=5)

    lbl_com = Label(win_agregar_art, text="Comentario:")
    lbl_com.grid(row=3, column=0, padx=5, pady=5)
    ent_com = Entry(win_agregar_art)
    ent_com.grid(row=3, column=1, padx=5, pady=5)

    # Función para agregar el artículo
    def agregar():
        # Obtener los datos del artículo
        cant = ent_cant.get()
        desc = ent_desc.get()
        com = ent_com.get()

        # Validar que se introduzca la cantidad
        if not cant:
            messagebox.showerror("Error", "Debe introducir la cantidad.")
            return

        # Validar que la cantidad sea un número entero
        try:
            cant = int(cant)
        except ValueError:
            messagebox.showerror("Error", "La cantidad debe ser un número entero.")
            return

        # Validar que la cantidad sea mayor a cero
        if cant <= 0:
            messagebox.showerror("Error", "La cantidad debe ser mayor a cero.")
            return

        # Agregar el artículo a la lista de artículos
        articulo = (ref_sel, cant, desc, com)
        self.list_art.append(articulo)

        # Actualizar la lista de artículos
        self.listbox.delete(0, END)
        for articulo in self.list_art:
            self.listbox.insert(END, articulo)

        # Cerrar la ventana de agregar artículo
        win_agregar_art.destroy()

    # Botón para agregar el artículo
    btn_agregar = Button(win_agregar_art, text="Agregar", command=agregar)
    btn_agregar.grid(row=4, column=0, padx=5, pady=5, columnspan=2)
class FichaReferencia(tk.Toplevel):
    def __init__(self, referencia):
        super().__init__()
        self.referencia = referencia
        self.articulos = []
        self.plano = None
        self.geometry("500x500")
        self.title(f"Ficha de referencia {self.referencia}")
        tk.Label(self, text=f"Referencia: {self.referencia}").pack()
        tk.Button(self, text="Agregar artículo", command=self.agregar_articulo).pack()
        tk.Button(self, text="Eliminar artículo", command=self.eliminar_articulo).pack()
        tk.Button(self, text="Editar artículo", command=self.editar_articulo).pack()
        tk.Label(self, text="Artículos:").pack()
        self.articulos_listbox = tk.Listbox(self, height=10, width=50)
        self.articulos_listbox.pack()
        tk.Button(self, text="Asignar plano", command=self.asignar_plano).pack()
        tk.Button(self, text="Abrir plano", command=self.abrir_plano).pack()
        tk.Button(self, text="Imprimir listado de artículos", command=self.imprimir_listado).pack()
        self.actualizar_articulos()
        self.protocol("WM_DELETE_WINDOW", self.cerrar)

    def agregar_articulo(self):
        ventana_agregar_articulo = VentanaAgregarArticulo(self)
        self.wait_window(ventana_agregar_articulo)
        if ventana_agregar_articulo.articulo is not None:
            self.articulos.append(ventana_agregar_articulo.articulo)
            self.actualizar_articulos()

    def eliminar_articulo(self):
        seleccion = self.articulos_listbox.curselection()
        if len(seleccion) == 1:
            self.articulos.pop(seleccion[0])
            self.actualizar_articulos()

    def editar_articulo(self):
        seleccion = self.articulos_listbox.curselection()
        if len(seleccion) == 1:
            ventana_editar_articulo = VentanaEditarArticulo(self, self.articulos[seleccion[0]])
            self.wait_window(ventana_editar_articulo)
            if ventana_editar_articulo.articulo is not None:
                self.articulos[seleccion[0]] = ventana_editar_articulo.articulo
                self.actualizar_articulos()

    def actualizar_articulos(self):
        self.articulos_listbox.delete(0, tk.END)
        for articulo in self.articulos:
            self.articulos_listbox.insert(tk.END, f"{articulo.cantidad} x {articulo.referencia} ({articulo.descripcion})")

    def asignar_plano(self):
        fichero_plano = filedialog.askopenfilename(title="Seleccione el plano", filetypes=[("PDF", "*.pdf")])
        if fichero_plano != "":
            self.plano = fichero_plano

    def abrir_plano(self):
        if self.plano is not None:
            os.startfile(self.plano)

    def imprimir_listado(self):
        listado = f"Listado de artículos necesarios para la referencia {self.referencia}:\n\n"
        for articulo in self.articulos:
            listado += f"{articulo.cantidad} x {articulo.referencia} ({articulo.descripcion})\n"
        print(listado)

    def cerrar(self):
        self.destroy()
class ReferenciaVentana(QtWidgets.QWidget):
    def __init__(self, referencia):
        super().__init__()
        self.referencia = referencia
        self.articulos = self.referencia.articulos
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 500, 500)
        self.setWindowTitle(f"Ficha de referencia: {self.referencia.nombre}")
        self.layout = QtWidgets.QVBoxLayout(self)

        # Tabla de artículos
        self.tabla_articulos = QtWidgets.QTableWidget(self)
        self.tabla_articulos.setColumnCount(4)
        self.tabla_articulos.setHorizontalHeaderLabels(["Cantidad", "Referencia", "Descripción", "Comentario"])
        self.tabla_articulos.setRowCount(len(self.articulos))
        for i, articulo in enumerate(self.articulos):
            cantidad = QtWidgets.QTableWidgetItem(str(articulo.cantidad))
            referencia = QtWidgets.QTableWidgetItem(articulo.referencia)
            descripcion = QtWidgets.QTableWidgetItem(articulo.descripcion)
            comentario = QtWidgets.QTableWidgetItem(articulo.comentario)
            self.tabla_articulos.setItem(i, 0, cantidad)
            self.tabla_articulos.setItem(i, 1, referencia)
            self.tabla_articulos.setItem(i, 2, descripcion)
            self.tabla_articulos.setItem(i, 3, comentario)
        self.tabla_articulos.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tabla_articulos.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.layout.addWidget(self.tabla_articulos)

        # Botones de acción
        self.layout_botones = QtWidgets.QHBoxLayout()
        self.boton_agregar = QtWidgets.QPushButton("Agregar artículo")
        self.boton_agregar.clicked.connect(self.agregar_articulo)
        self.boton_eliminar = QtWidgets.QPushButton("Eliminar artículo")
        self.boton_eliminar.clicked.connect(self.eliminar_articulo)
        self.layout_botones.addWidget(self.boton_agregar)
        self.layout_botones.addWidget(self.boton_eliminar)
        self.layout.addLayout(self.layout_botones)

    def agregar_articulo(self):
        dialogo = ArticuloDialogo(self)
        if dialogo.exec_() == QtWidgets.QDialog.Accepted:
            articulo = dialogo.articulo
            self.referencia.agregar_articulo(articulo)
            self.articulos = self.referencia.articulos
            self.actualizar_tabla_articulos()

    def eliminar_articulo(self):
        indices = [index.row() for index in self.tabla_articulos.selectedIndexes()]
        indices.sort(reverse=True)
        for indice in indices:
            self.referencia.eliminar_articulo(indice)
        self.articulos = self.referencia.articulos
        self.actualizar_tabla_articulos()

    def actualizar_tabla_articulos(self):
        # Limpiar la tabla
        self.tabla_articulos.clearContents()

        # Obtener la referencia seleccionada en la tabla de referencias
        fila_referencia = self.tabla_referencias.currentRow()
        referencia_seleccionada = self.tabla_referencias.item(fila_referencia, 0).text()

        # Obtener la lista de artículos de la referencia seleccionada
        if referencia_seleccionada in self.pedidos[self.pedido_seleccionado]['referencias']:
            lista_articulos = self.pedidos[self.pedido_seleccionado]['referencias'][referencia_seleccionada]['articulos']
        else:
            lista_articulos = []

        # Establecer el número de filas de la tabla
        self.tabla_articulos.setRowCount(len(lista_articulos))

        # Llenar la tabla con los datos de los artículos
        for i, articulo in enumerate(lista_articulos):
            # Crear celdas para cada campo del artículo
            cantidad = QtWidgets.QTableWidgetItem(str(articulo['cantidad']))
            referencia = QtWidgets.QTableWidgetItem(articulo['referencia'])
            descripcion = QtWidgets.QTableWidgetItem(articulo['descripcion'])
            comentario = QtWidgets.QTableWidgetItem(articulo['comentario'])

            # Agregar las celdas a la tabla
            self.tabla_articulos.setItem(i, 0, cantidad)
            self.tabla_articulos.setItem(i, 1, referencia)
            self.tabla_articulos.setItem(i, 2, descripcion)
            self.tabla_articulos.setItem(i, 3, comentario)

