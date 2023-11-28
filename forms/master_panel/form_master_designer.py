import tkinter as tk
from tkinter import ttk
import util.generic as utl
import mysql.connector as sql
from tkinter import messagebox

class MasterPanelDesigner:
    def obtener_cantidad_ordenes_departamentos(self):
        pass
    def obtener_cantidad_ordenes_tecnicos(self):
        pass
    def limitar_caracteres(self):
        pass                          
    def crear_departamento(self):
        pass
    def editar_departamento(self):
        pass
    def borrar_departamento(self):
        pass
    def guardar_datos_actualizados_empleados(self):
        pass
    def borrar_empleado(self):
        pass
    def obtener_datos(self):
        pass
    def guardar_datos(self):
        pass
    def obtener_jefes_empleados(self):
        pass
       
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('MASTER')
        self.ventana.config(bg='#808080')
        utl.centrar_ventana(self.ventana,380,125)
        icono = utl.leer_imagen("./images/icon.png", (200, 200))
        self.ventana.iconphoto(True, icono)
        self.ventana.resizable(width=False, height=False)        
        #Crear botones
        btn_empleados = ttk.Button(self.ventana, text="Empleados", command=self.mostrar_empleados, style='TButton', width=20)
        btn_departamentos = ttk.Button(self.ventana, text="Departamentos", command=self.mostrar_departamentos, style='TButton', width=20)
        btn_ordenes_tecnicos = ttk.Button(self.ventana, text="Ordenes por Tecnicos", command=self.mostrar_ordenes_tecnicos, style='TButton', width=20)
        btn_ordenes_departamento = ttk.Button(self.ventana, text="Ordenes Departamento", command=self.mostrar_ordenes_departamentos, style='TButton', width=20)
        #Ajustar el tamaño texto del boton
        btn_empleados.configure(style='TButton.Large.TButton')
        btn_departamentos.configure(style='TButton.Large.TButton')
        btn_ordenes_tecnicos.configure(style='TButton.Large.TButton')
        btn_ordenes_departamento.configure(style='TButton.Large.TButton')   
        #Ajustar el padding de los botones
        btn_empleados.configure(padding=(20, 10))
        btn_departamentos.configure(padding=(20, 10))
        btn_ordenes_tecnicos.configure(padding=(20, 10))
        btn_ordenes_departamento.configure(padding=(20, 10))  
        #Posicionar botones
        btn_empleados.grid(row=0, column=0, padx=10, pady=10)
        btn_departamentos.grid(row=0, column=1, padx=10, pady=10)
        btn_ordenes_tecnicos.grid(row=1, column=0, padx=10, pady=10)
        btn_ordenes_departamento.grid(row=1, column=1, padx=10, pady=10)
        #Inicializar el tree view
        self.tree = None
        #Inicializar la ventana principal    
        self.ventana.mainloop()
        #Ventana para ver los empleados de la base de datos
    def mostrar_empleados(self):
        #Crear una nueva ventana toplevel para mostrar los empleados
        ventana_empleados = tk.Toplevel(self.ventana)
        ventana_empleados.title('Empleados')
        self.ventana_empleados = ventana_empleados
        self.ventana.resizable(width=False, height=False)
        #Conectar al db usando la funcion obtener_datos
        self.obtener_datos()
        #Crear el TreeView para mostrar los empleados
        self.tree = ttk.Treeview(ventana_empleados, columns=('Nombre', 'RUN'), show='headings')
        self.tree.heading('Nombre', text='Nombre')
        self.tree.heading('RUN', text='RUN')
        #Insertar datos en el TreeView
        for self.empleado in self.empleados:
            self.tree.insert('', 'end', values=self.empleado)
        #Ajustar el ancho de las columnas
        for col in ('Nombre', 'RUN'):
            self.tree.column(col, width=100, anchor='center')
        self.tree.pack()
        #Crear botones
        ttk.Button(ventana_empleados, text="Crear", command=self.crear_empleado).pack(side='left', padx=10, pady=10)
        ttk.Button(ventana_empleados, text="Editar", command=self.editar_empleado).pack(side='left', padx=10, pady=10)
        ttk.Button(ventana_empleados, text="Borrar", command=self.borrar_empleado).pack(side='left', padx=10, pady=10)  
        #ventana para crear empleados
    def crear_empleado(self):
            #Crear la ventana toplevelpara crear empleados
            self.ventana_creacion_empleado = tk.Toplevel(self.ventana_empleados)
            self.ventana_creacion_empleado.title('Crear Empleado')
            self.ventana_creacion_empleado.resizable(width=False, height=False)
            self.ventana_creacion_empleado.bind("<Return>", (lambda event: self.guardar_datos()))
            #Conseguir los datos de los jefes
            jefes = self.obtener_jefes_empleados()
            #Entrys
            tk.Label(self.ventana_creacion_empleado, text='RUN:').pack()
            entry_var=tk.StringVar()
            self.entry_run = tk.Entry(self.ventana_creacion_empleado,textvariable=entry_var)
            self.entry_run.pack()
            self.entry_run.bind('<Key>', lambda event: self.limitar_caracteres(entry_var, 12))

            tk.Label(self.ventana_creacion_empleado, text='Nombre y Apellido:').pack()
            self.entry_nombre = tk.Entry(self.ventana_creacion_empleado)
            self.entry_nombre.pack()

            tk.Label(self.ventana_creacion_empleado, text='Fecha de Nacimiento (YYYY-MM-DD):').pack()
            self.entry_fecha_nacimiento = tk.Entry(self.ventana_creacion_empleado)
            self.entry_fecha_nacimiento.pack()

            tk.Label(self.ventana_creacion_empleado, text='Rol:').pack()
            self.combo_id_rol = ttk.Combobox(self.ventana_creacion_empleado, values=['ADMIN', 'USUARIO', 'TECNICO'],state='readonly')
            self.combo_id_rol.pack()

            tk.Label(self.ventana_creacion_empleado, text='Departamento:').pack()
            self.combo_id_dep = ttk.Combobox(self.ventana_creacion_empleado, values=['JEFATURA', 'TIC', 'TECNICOS'],state='readonly')
            self.combo_id_dep.pack()

            tk.Label(self.ventana_creacion_empleado, text='Jefe:').pack()
            self.combo_id_jefe = ttk.Combobox(self.ventana_creacion_empleado,values=jefes,state='readonly')
            self.combo_id_jefe.pack()

            tk.Label(self.ventana_creacion_empleado, text='Password:').pack()
            self.entry_password = tk.Entry(self.ventana_creacion_empleado, show='*')
            self.entry_password.pack()

            # Boton para guardar los datos
            btn_guardar = ttk.Button(self.ventana_creacion_empleado, text="Guardar", command=self.guardar_datos)
            btn_guardar.pack() 
        #Ventana para editar empleados
    def editar_empleado(self):
        # Obtener la selecciOn actual en el Treeview
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showerror("Error", "Por favor, selecciona un empleado para editar.")
            return
        #Obtener el nombre del empleado seleccionado
        nombre_empleado = self.tree.item(seleccion, 'values')[0]
        #Conectar a la base de datos
        db = sql.connect(host="localhost", user="root", passwd="", database="sistema_ordenes")
        cursor = db.cursor()
        try:
            #Obtener el id del empleado desde la tabla empleados
            cursor.execute("SELECT id, run, nombre, fecha_nacimiento, id_rol, id_dep FROM empleados WHERE nombre = %s", (nombre_empleado,))
            resultado = cursor.fetchone()
            if resultado:
                self.id_empleado, run, nombre, fecha_nacimiento, id_rol_num, id_dep_num = resultado
                #Leer todos los resultados antes de realizar otra consulta
                cursor.fetchall()
                id_rol = {1:"ADMIN",2:"USUARIO",3:"TECNICO"}.get(id_rol_num, None)
                id_dep = {1:"JEFATURA",2:"TIC",3:"TECNICOS"}.get(id_dep_num, None)
                #Crear la ventana de edicion de empleados y usuarios
                ventana_edicion = tk.Toplevel(self.ventana_empleados)
                ventana_edicion.title('Editar Empleado')
                self.ventana_edicion = ventana_edicion
                self.ventana_edicion.resizable(width=False, height=False)
                #variables
                self.run_var= tk.StringVar(self.ventana_edicion)
                self.nombre_var= tk.StringVar(self.ventana_edicion)
                self.fecha_nacimiento_var= tk.StringVar(self.ventana_edicion)
                self.id_rol_var= tk.StringVar(self.ventana_edicion)
                self.id_dep_var= tk.StringVar(self.ventana_edicion)
                self.correo_var= tk.StringVar(self.ventana_edicion)
                self.contraseña_var= tk.StringVar(self.ventana_edicion)
                
                #Entrys
                tk.Label(ventana_edicion, text='RUN:').pack()
                self.run = tk.Entry(ventana_edicion,textvariable=self.run_var)
                self.run.insert(0, run)
                self.run.pack()
                self.run.bind('<Key>', lambda event: self.limitar_caracteres(self.run_var, 12))

                tk.Label(ventana_edicion, text='Nombre y Apellido:').pack()
                self.nombre = tk.Entry(ventana_edicion,textvariable=self.nombre_var)
                self.nombre.insert(0, nombre)
                self.nombre.pack()

                tk.Label(ventana_edicion, text='Fecha de Nacimiento (YYYY-MM-DD):').pack()
                self.fecha_nacimiento = tk.Entry(ventana_edicion,textvariable=self.fecha_nacimiento_var)
                self.fecha_nacimiento.insert(0, fecha_nacimiento)
                self.fecha_nacimiento.pack()

                tk.Label(ventana_edicion, text='Rol:').pack()
                self.id_rol = ttk.Combobox(ventana_edicion, textvariable=self.id_rol_var, values=['ADMIN', 'USUARIO', 'TECNICO'], state='readonly', font=("Arial", 12))
                self.id_rol.set(id_rol)
                self.id_rol.pack()
                
                tk.Label(ventana_edicion, text='Dep:').pack()
                self.id_dep = ttk.Combobox(ventana_edicion, textvariable=self.id_dep_var, values=['JEFATURA', 'TIC', 'TECNICOS'], state='readonly', font=("Arial", 12))
                self.id_dep.set(id_dep)
                self.id_dep.pack()

                tk.Label(ventana_edicion, text='Correo:').pack()
                self.correo = tk.Entry(ventana_edicion,textvariable=self.correo_var)
                #Cargar el correo del usuario desde la base de datos
                cursor.execute("SELECT correo FROM usuarios WHERE id = %s", (self.id_empleado,))
                correo_actual = cursor.fetchone()[0]
                self.correo.insert(0, correo_actual)
                self.correo.pack()

                tk.Label(ventana_edicion, text='Contraseña:').pack()
                self.contraseña = tk.Entry(ventana_edicion, show='*',textvariable=self.contraseña_var)
                #Cargar la contraseña del usuario desde la base de datos
                cursor.execute("SELECT password FROM usuarios WHERE id = %s", (self.id_empleado,))
                contraseña_actual = cursor.fetchone()[0]
                self.contraseña.insert(0, contraseña_actual)
                self.contraseña.pack()

                #Boton para guardar los datos actualizados
                boton_guardar_actualizados = ttk.Button(ventana_edicion, text="Actualizar", command=self.guardar_datos_actualizados_empleados)
                boton_guardar_actualizados.pack()
                #Confirmar los cambios, cerrar la db y consulta
                cursor.close()
                db.commit()
                db.close()
            else:
                messagebox.showwarning("Advertencia", "No se encontro el empleado en la base de datos.")
        except Exception as e:
            #Manejar errores
            messagebox.showerror("Error", f"Error al editar el empleado: {str(e)}")

    def mostrar_departamentos(self):
        #Crear una nueva ventana toplevel para mostrar los departamentos
        ventana_departamentos = tk.Toplevel(self.ventana)
        ventana_departamentos.title('Departamentos')
        self.ventana_departamentos = ventana_departamentos
        self.ventana_departamentos.resizable(width=False, height=False)
        #Conectar a la base de datos y obtener datos de la tabla departamentos
        db = sql.connect(host="localhost", user="root", passwd="", database="sistema_ordenes")
        cursor = db.cursor()
        try:
            #Ejecutar la consulta para obtener datos de la tabla departamentos
            cursor.execute("SELECT * FROM departamentos")
            departamentos = cursor.fetchall()
            #cerrar db y consulta
            cursor.close()
            db.close()
            #Crear el treeview para mostrar los departamentos
            self.tree_departamentos = ttk.Treeview(ventana_departamentos, columns=('ID', 'Nombre'), show='headings')
            self.tree_departamentos.heading('ID', text='ID')
            self.tree_departamentos.heading('Nombre', text='Nombre')
            #Insertar datos en el treeview
            for departamento in departamentos:
                self.tree_departamentos.insert('', 'end', values=departamento)
            #Ajustar el ancho de las columnas
            for col in ('ID', 'Nombre'):
                self.tree_departamentos.column(col, width=100, anchor='center')          
            self.tree_departamentos.pack()
            #Crear botones
            ttk.Button(ventana_departamentos, text="Crear", command=self.crear_departamento).pack(side='left', padx=10, pady=10)
            ttk.Button(ventana_departamentos, text="Editar", command=self.editar_departamento).pack(side='left', padx=10, pady=10)
            ttk.Button(ventana_departamentos, text="Borrar", command=self.borrar_departamento).pack(side='left', padx=10, pady=10)
        except Exception as e:
            #Manejar errores
            messagebox.showerror("Error", f"Error al obtener datos de departamentos: {str(e)}")
    
    def mostrar_ordenes_tecnicos(self):
        #Crear una nueva ventana toplevel para mostrar ordenes por tecnico
        self.ventana_ordenes_tecnicos = tk.Toplevel(self.ventana)
        self.ventana_ordenes_tecnicos.title('Ordenes Tecnicos')
        self.ventana_ordenes_tecnicos.resizable(width=False, height=False)
        #Obtener la cantidad de ordenes en estado 3 por run_tecnico
        self.ordenes_tecnicos = self.obtener_cantidad_ordenes_tecnicos()
        #Crear el TreeView para mostrar las ordenes por tecnico
        self.tree_ordenes_tecnicos = ttk.Treeview(self.ventana_ordenes_tecnicos, columns=('RUN Tecnico', 'Cantidad Ordenes'), show='headings')
        self.tree_ordenes_tecnicos.heading('RUN Tecnico', text='RUN Tecnico')
        self.tree_ordenes_tecnicos.heading('Cantidad Ordenes', text='Cantidad Ordenes')
        #Insertar datos en el TreeView
        for orden_tecnico in self.ordenes_tecnicos:
            self.tree_ordenes_tecnicos.insert('', 'end', values=orden_tecnico)
        #Ajustar el ancho de las columnas
        for col in ('RUN Tecnico', 'Cantidad Ordenes'):
            self.tree_ordenes_tecnicos.column(col, width=150, anchor='center')
        self.tree_ordenes_tecnicos.pack()
    
    def mostrar_ordenes_departamentos(self):
        #Crear una nueva ventana toplevel para mostrar las ordenes por departamento
        ventana_ordenes_departamentos = tk.Toplevel(self.ventana)
        ventana_ordenes_departamentos.title('Ordenes por Departamento')
        self.ventana_ordenes_departamentos = ventana_ordenes_departamentos
        self.ventana_ordenes_departamentos.resizable(width=False, height=False)
        #Obtener la cantidad de ordenes por id_dep y departamento
        ordenes_departamentos = self.obtener_cantidad_ordenes_departamentos()
        #Crear el treeview para mostrar las ordenes por departamento
        self.tree_ordenes_departamentos = ttk.Treeview(ventana_ordenes_departamentos, columns=('ID Departamento', 'Departamento', 'Cantidad Ordenes'), show='headings')
        self.tree_ordenes_departamentos.heading('ID Departamento', text='ID Departamento')
        self.tree_ordenes_departamentos.heading('Departamento', text='Departamento')
        self.tree_ordenes_departamentos.heading('Cantidad Ordenes', text='Cantidad Ordenes')
        #Insertar datos en el treeview
        for orden_departamento in ordenes_departamentos:
            self.tree_ordenes_departamentos.insert('', 'end', values=orden_departamento)
        #Ajustar el ancho de las columnas
        for col in ('ID Departamento', 'Departamento', 'Cantidad Ordenes'):
            self.tree_ordenes_departamentos.column(col, width=150, anchor='center')
        self.tree_ordenes_departamentos.pack()