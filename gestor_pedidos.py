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
        self.nuevo_pedido(producto, cantidad)
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
    def nuevo_pedido(self, nombre, producto, cantidad):
        print("\nAñadir pedido\n")
        producto = input("Nombre del producto: ")
        return int(input("Introduce la cantidad de {} que deseas añadir al pedido: ".format(nombre_producto)))
        try:
           cantidad = self.nuevo_pedido(nombre_producto)
        except ValueError:
            print("La cantidad debe ser un número entero.")
            return
        cliente = input("Nombre del cliente: ")
        self.pedidos.append(Pedido(producto, int(cantidad), cliente))
        print("Pedido añadido correctamente.\n")



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
        # Se define el cuadro de fecha de entrega del pedido.
        cuadro_fecha_entrega = ttk.Frame(self.ventana_editar_pedido)
        cuadro_fecha_entrega.pack(fill=X, padx=10, pady=5)
        ttk.Label(cuadro_fecha_entrega, text="Fecha de entrega:", width=40).pack(side=LEFT)
        self.fecha_entrega_pedido = ttk.Entry(cuadro_fecha_entrega, width=30)
        self.fecha_entrega_pedido.pack(side=LEFT, padx=5)

        # Se define el cuadro de cantidad del pedido.
        cuadro_cantidad = ttk.Frame(self.ventana_editar_pedido)
        cuadro_cantidad.pack(fill=X, padx=10, pady=5)
        ttk.Label(cuadro_cantidad, text="Cantidad:", width=40).pack(side=LEFT)
        self.cantidad_pedido = ttk.Entry(cuadro_cantidad, width=30)
        self.cantidad_pedido.pack(side=LEFT, padx=5)

        # Se definen los botones de guardar y cancelar cambios.
        cuadro_botones = ttk.Frame(self.ventana_editar_pedido)
        cuadro_botones.pack(fill=X, padx=10, pady=10)
        cantidad = ''
        ttk.Button(cuadro_botones, text="Guardar cambios", command=self.guardar_cambios_pedido).pack(side=LEFT, padx=5)
        ttk.Button(cuadro_botones, text="Cancelar", command=self.ventana_editar_pedido.destroy).pack(side=LEFT, padx=5)
    def nuevo_pedido(self):
        """Crea un nuevo pedido y lo agrega a la lista de pedidos."""
        nombre = input('Introduce el nombre del cliente: ')
        direccion = input('Introduce la dirección de entrega: ')
        articulos = []
        while True:
            nombre_articulo = input('Introduce el nombre del artículo (o "fin" para salir): ')
            if nombre_articulo == 'fin':
                break
            cantidad = input('Introduce la cantidad de "{}": '.format(nombre_articulo))
            precio = input('Introduce el precio unitario de "{}": '.format(nombre_articulo))
            articulo = Articulo(nombre_articulo, int(cantidad), float(precio))
            articulos.append(articulo)
        pedido = Pedido(nombre, direccion, articulos)
        self.lista_pedidos.append(pedido)
        print('Se ha añadido el pedido correctamente.')

        # Función para mostrar los pedidos pendientes
    def mostrar_pedidos_pendientes(self):
        """Muestra los pedidos pendientes."""
        print('Pedidos pendientes:')
        for pedido in self.lista_pedidos:
            if pedido.estado == 'pendiente':
                print(pedido)

    def guardar_cambios_pedido(self):
        """Guarda los cambios realizados en un pedido en la lista y en el archivo."""
        id_pedido = self.id_pedido_seleccionado.get()
        referencia = self.entry_referencia.get().strip()
        nombre = self.entry_nombre.get().strip()
        fecha_entrega = self.calendario.get_date().strftime("%d/%m/%Y")
        cantidad = self.entry_cantidad.get().strip()
        self.nuevo_pedido(nombre, producto, cantidad)

        # Validación de datos.
        if not referencia or not nombre or not fecha_entrega or not cantidad:
           messagebox.showerror("Error", "Todos los campos son obligatorios.")
           return
    try:
        int(cantidad)
    except ValueError:
        messagebox.showerror("Error", "La cantidad debe ser un número entero.")
        # return

    # Actualización de los datos del pedido.
    self.pedidos[id_pedido] = (referencia, nombre, fecha_entrega, cantidad)
    self.cargar_tabla_pedidos()
    self.ventana_editar_pedido.destroy()

    # Guardado de los datos en el archivo.
    try:
        with open("pedidos.txt", "w") as archivo:
            for pedido in self.pedidos:
                archivo.write(f"{pedido[0]};{pedido[1]};{pedido[2]};{pedido[3]}\n")
        messagebox.showinfo("Éxito", "El pedido ha sido actualizado correctamente.")
    except IOError:
        messagebox.showerror("Error", "No se ha podido guardar el pedido en el archivo.")

    def eliminar_pedido(self):
        """Elimina un pedido de la lista de pedidos."""
        id_pedido = self.obtener_id_pedido_seleccionado()
        if id_pedido is not None:
           respuesta = messagebox.askyesno("Confirmar eliminación", "¿Está seguro de que desea eliminar el pedido seleccionado?")
           if respuesta == YES:
               del self.pedidos[id_pedido]
               self.cargar_tabla_pedidos()
               messagebox.showinfo("Éxito", "El pedido ha sido eliminado correctamente.")
        else:
             messagebox.showwarning("Error", "Debe seleccionar un pedido para eliminar.")
        
    def guardar_pedidos(self):
        """Guarda los datos de los pedidos en un archivo de texto."""
        with open("pedidos.txt", "w") as archivo:
             for pedido in self.pedidos:
                 referencia, nombre, fecha_entrega, cantidad = pedido
                 archivo.write(f"{referencia},{nombre},{fecha_entrega},{cantidad}\n")
                 messagebox.showinfo("Éxito", "Los pedidos han sido guardados correctamente.")
    
    def cargar_pedidos(self):
        """Carga los datos de los pedidos desde un archivo de texto."""
        try:
            with open("pedidos.txt", "r") as archivo:
                for linea in archivo:
                    referencia, nombre, fecha_entrega, cantidad = linea.strip().split(",")
                    self.pedidos.append((referencia, nombre, fecha_entrega, int(cantidad)))
        except FileNotFoundError:
            pass
        
        self.cargar_tabla_pedidos()

    def ordenar_por_fecha(self):
        """Ordena la tabla de pedidos por fecha de entrega."""
        pedidos_ordenados = sorted(self.pedidos, key=lambda x: datetime.strptime(x[2], "%d/%m/%Y"))
        self.pedidos = pedidos_ordenados
        self.cargar_tabla_pedidos()

    def editar_pedido(self, event=None):
        """Abre la ventana de edición del pedido seleccionado al hacer doble clic en la tabla de pedidos."""
        id_pedido = self.obtener_id_pedido_seleccionado()
        if id_pedido is not None:
           pedido = self.pedidos[id_pedido]
           referencia, nombre, fecha_entrega, cantidad = pedido
        
           self.ventana_editar_pedido = Toplevel()
           self.ventana_editar_pedido.title("Editar pedido")
           self.ventana_editar_pedido.resizable(False, False)
        
           # Se define el cuadro de referencia del pedido.
           cuadro_referencia = ttk.Frame(self.ventana_editar_pedido)
           cuadro_referencia.pack(fill=X, padx=10, pady=5)
           ttk.Label(cuadro_referencia, text="Referencia:", width=15).pack(side=LEFT)
           ttk.Entry(cuadro_referencia, textvariable=self.var_referencia, width=30).pack(side=LEFT)
           self.var_referencia.set(referencia)
        
           # Se define el cuadro de nombre del pedido.
           cuadro_nombre = ttk.Frame(self.ventana_editar_pedido)
           cuadro_nombre.pack(fill=X, padx=10, pady=5)
           ttk.Label(cuadro_nombre, text="Nombre:", width=15).pack(side=LEFT)
           ttk.Entry(cuadro_nombre, textvariable=self.var_nombre, width=30).pack(side=LEFT)
           self.var_nombre.set(nombre)
        
           # Se define el cuadro de fecha de entrega del pedido.
           cuadro_fecha_entrega = ttk.Frame(self.ventana_editar_pedido)
           cuadro_fecha_entrega.pack(fill=X, padx=10, pady=5)
           ttk.Label(cuadro_fecha_entrega, text="Fecha de entrega:", width=15).pack(side=LEFT)
           fecha_entrega_var = StringVar()
           fecha_entrega_var.set(fecha_entrega)
           entrada_fecha_entrega = ttk.Entry(cuadro_fecha_entrega, textvariable=fecha_entrega_var, width=20)
           entrada_fecha_entrega.pack(side=LEFT)

           # Se define el cuadro de cantidad del pedido.
           cuadro_cantidad = ttk.Frame(self.ventana_editar_pedido)
           cuadro_cantidad.pack(fill=X, padx=10, pady=5)
           ttk.Label(cuadro_cantidad, text="Cantidad:", width=15).pack(side=LEFT)
           cantidad_var = StringVar()
           cantidad_var.set(cantidad)
           entrada_cantidad = ttk.Entry(cuadro_cantidad, textvariable=cantidad_var, width=20)
           entrada_cantidad.pack(side=LEFT)

           # Se define el botón de guardar.
           ttk.Button(self.ventana_editar_pedido, text="Guardar", command=lambda: self.guardar_pedido(id_pedido, referencia_var.get(), nombre_var.get(), fecha_entrega_var.get(), cantidad_var.get())).pack(side=LEFT, padx=10)

           # Se define el botón de cancelar.
           ttk.Button(self.ventana_editar_pedido, text="Cancelar", command=self.ventana_editar_pedido.destroy).pack(side=LEFT)

           # Se centra la ventana de edición en la pantalla.
           centrar_ventana(self.ventana_editar_pedido)

    def eliminar_pedido(self):
        """Elimina un pedido de la lista de pedidos."""
        id_pedido = self.obtener_id_pedido_seleccionado()
        if id_pedido is not None:
           respuesta = messagebox.askyesno("Confirmar eliminación", "¿Está seguro de que desea eliminar el pedido seleccionado?")
           if respuesta == YES:
              del self.pedidos[id_pedido]
              self.cargar_tabla_pedidos()
              messagebox.showinfo("Éxito", "El pedido ha sido eliminado correctamente.")
        else:
            messagebox.showwarning("Error", "Debe seleccionar un pedido de la tabla.")

    def guardar_pedido(self, id_pedido, referencia, nombre, fecha_entrega, cantidad):
        """Guarda un pedido en la lista de pedidos."""
        if not referencia or not nombre or not fecha_entrega or not cantidad:
            messagebox.showwarning("Error", "Debe completar todos los campos del formulario.")
        else:
            try:
               fecha_entrega = datetime.strptime(fecha_entrega, "%d/%m/%Y").strftime("%d/%m/%Y")
               cantidad = int(cantidad)
               if cantidad <= 0:
                   raise ValueError
            except ValueError:
                messagebox.showwarning("Error", "La cantidad debe ser un número entero mayor que cero.")
            else:
                # Se actualiza el pedido en la lista de pedidos.
                self.pedidos[id_pedido] = (referencia, nombre, fecha_entrega, cantidad)

                # Se actualiza la tabla de pedidos.
                self.cargar_tabla_pedidos()

                # Se cierra la ventana de edición.
                self.ventana_editar_pedido.destroy()

                # Se muestra un mensaje de éxito.
                messagebox.showinfo("Éxito", "El pedido ha sido actualizado correctamente.")

    def guardar_datos(self):
        """Guarda los datos de los pedidos en un archivo de texto."""
        filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivo de texto", "*.txt")])
        if filename:
            with open(filename, "w") as f:
                for pedido in self.pedidos:
                    f.write(f"{pedido[0]},{pedido[1]},{pedido[2]},{pedido[3]}\n")
            messagebox.showinfo("Éxito", f"Los datos de los pedidos han sido guardados en el archivo {filename}.")

    def ordenar_por_fecha_entrega(self):
        """Ordena los pedidos por fecha de entrega."""
        self.pedidos.sort(key=lambda x: x[2])
        self.cargar_tabla_pedidos()

    def cargar_tabla_pedidos(self):
        """Carga los datos de los pedidos en la tabla de pedidos."""
        for row in self.tabla_pedidos.get_children():
            self.tabla_pedidos.delete(row)

        for i, pedido in enumerate(self.pedidos):
            self.tabla_pedidos.insert("", "end", iid=i, values=pedido)
        
        self.tabla_pedidos.bind("<Double-1>", self.editar_pedido)
    
    def editar_pedido(self, event):
        """Abre una ventana para editar el pedido seleccionado."""
        item = self.tabla_pedidos.selection()[0]
        id_pedido = int(item)
        pedido = self.pedidos[id_pedido]

        self.ventana_editar_pedido = Toplevel(self.ventana_principal)
        self.ventana_editar_pedido.title("Editar pedido")
        self.ventana_editar_pedido.geometry("400x250")
        self.ventana_editar_pedido.resizable(False, False)

        # Se define el cuadro de nombre del pedido.
        cuadro_nombre = ttk.Frame(self.ventana_editar_pedido)
        cuadro_nombre.pack(fill=X, padx=10, pady=5)
        ttk.Label(cuadro_nombre, text="Nombre:", width=15, anchor=E).pack(side=LEFT)
        entry_nombre = ttk.Entry(cuadro_nombre, width=30)
        entry_nombre.pack(side=LEFT)
        entry_nombre.insert(0, pedido[1])

        # Se define el cuadro de fecha de entrega del pedido.
        cuadro_fecha_entrega = ttk.Frame(self.ventana_editar_pedido)
        cuadro_fecha_entrega.pack(fill=X, padx=10, pady=5)
        ttk.Label(cuadro_fecha_entrega, text="Fecha de entrega:", width=15, anchor=E).pack(side=LEFT)
        entry_fecha_entrega = ttk.Entry(cuadro_fecha_entrega, width=30)
        entry_fecha_entrega.pack(side=LEFT)
        entry_fecha_entrega.insert(0, pedido[2])

        # Se define el cuadro de cantidad del pedido.
        cuadro_cantidad = ttk.Frame(self.ventana_editar_pedido)
        cuadro_cantidad.pack(fill=X, padx=10, pady=5)
        ttk.Label(cuadro_cantidad, text="Cantidad:", width=15, anchor=E).pack(side=LEFT)
        # Se define el campo de cantidad del pedido.
        entry_cantidad = ttk.Entry(cuadro_cantidad, width=50)
        entry_cantidad.pack(side=LEFT)

        # Se establece el valor del campo cantidad.
        if id_pedido is not None:
            entry_cantidad.insert(0, self.pedidos[id_pedido][3])

        # Se define el cuadro de botones de la ventana de edición.
        cuadro_botones = ttk.Frame(self.ventana_editar_pedido)
        cuadro_botones.pack(fill=X, padx=10, pady=5)

        # Se define el botón para guardar los cambios del pedido.
        boton_guardar = ttk.Button(cuadro_botones, text="Guardar", command=self.guardar_pedido)
        boton_guardar.pack(side=LEFT, padx=5)

        # Se define el botón para cancelar los cambios del pedido.
        boton_cancelar = ttk.Button(cuadro_botones, text="Cancelar", command=self.ventana_editar_pedido.destroy)
        boton_cancelar.pack(side=LEFT, padx=5)

    def eliminar_pedido(self):
        """Elimina un pedido de la lista de pedidos."""
        id_pedido = self.obtener_id_pedido_seleccionado()
        if id_pedido is not None:
            respuesta = messagebox.askyesno("Confirmar eliminación", "¿Está seguro de que desea eliminar el pedido seleccionado?")
            if respuesta == YES:
                del self.pedidos[id_pedido]
                self.cargar_tabla_pedidos()
                messagebox.showinfo("Éxito", "El pedido ha sido eliminado correctamente.")
        else:
            messagebox.showerror("Error", "Debe seleccionar un pedido para poder eliminarlo.")

    def guardar_pedido(self):
        """Guarda un pedido en la lista de pedidos."""
        # Se obtienen los datos del pedido de los campos de la ventana de edición.
        referencia = self.entry_referencia.get()
        nombre = self.entry_nombre.get()
        fecha_entrega = self.entry_fecha_entrega.get()
        cantidad = self.entry_cantidad.get()

        # Se valida que los campos no estén vacíos.
        if referencia == "" or nombre == "" or fecha_entrega == "" or cantidad == "":
            messagebox.showerror("Error", "Debe completar todos los campos para poder guardar el pedido.")
        else:
            # Se convierte la cantidad a un número entero.
            cantidad = int(cantidad)

            # Se obtiene el id del pedido seleccionado.
            id_pedido = self.obtener_id_pedido_seleccionado()

            if id_pedido is None:
                # Si no hay un pedido seleccionado, se crea uno nuevo.
                self.pedidos.append((referencia, nombre, fecha_entrega, cantidad))
                messagebox.showinfo("Éxito", "El pedido ha sido agregado correctamente.")
            else:
                # Si hay un pedido seleccionado, se actualiza.
                self.pedidos[id_pedido] = (referencia, nombre, fecha_entrega, cantidad)
                messagebox.showinfo("Éxito", "El pedido ha sido actualizado correctamente.")

            # Se actualiza la tabla de pedidos.
            self.cargar_tabla_pedidos()

            # Se cierra la ventana de edición.
            self.ventana_editar_pedido.destroy()

    def guardar_datos(self):
        """Guarda los datos de los pedidos en un archivo de texto."""
        try:
            with open("pedidos.txt", "w") as archivo:
                for pedido in self.pedidos:
                    archivo.write(f"{pedido['nombre']} - {pedido['cantidad']} - {pedido['direccion']} - {pedido['telefono']}\n")
        except IOError:
            messagebox.showerror("Error", "No se pudo guardar los datos del pedido.")
       

               
  
       


