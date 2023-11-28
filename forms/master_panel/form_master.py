from forms.master_panel.form_master_designer import MasterPanelDesigner
from tkinter import messagebox
import mysql.connector as sql
import tkinter as tk
from tkinter import simpledialog

class MasterPanel(MasterPanelDesigner):
    def __init__(self):
        super().__init__()
        #funcion para limitar caracteres en un entry variable, cantidad maxima de caracteres
    def limitar_caracteres(self, variable, max_caracteres):
        if len(variable.get()) > max_caracteres:
            variable.set(variable.get()[:max_caracteres])
        #funcion para guardar datos de empleados al crearse
    def guardar_datos(self):
        run = self.run_var.get()
        print(run)
        nombre_apellido = self.nombrenombre_var.get()
        fecha_nacimiento = self.fecha_nacimiento_var.get()
        password = self.password_var.get()
        id_jefe = self.combo_id_jefe.get()
        #id_rol = self.id_rol_var.get()
        #id_dep = self.id_dep_var.get()
        id_rol= {"ADMIN":1,"USUARIO":2,"TECNICO":3}.get(self.id_rol_var.get(), None)
        id_dep = {"JEFATURA":1,"TIC":2,"TECNICOS":3}.get(self.id_dep_var.get(), None)
        if id_rol is not None and id_dep is not None and run != "" and nombre_apellido != "" and fecha_nacimiento != "":
            try:
                #Crear conexion y consulta a la db
                db = sql.connect(host="localhost", user="root", passwd="", database="sistema_ordenes")
                cursor = db.cursor()
                #Obtener nombre y apellido
                nombre, apellido = nombre_apellido.split(maxsplit=1)
                #Crear el usuario automaticamente
                correo = nombre.lower() + apellido.lower() + "@gmail.com"               
                #Insertar datos en la tabla usuarios
                cursor.execute("INSERT INTO usuarios (correo, password, id_rol) VALUES (%s, %s, %s)",
                (correo, password, id_rol))
                #Obtener el último id insertado en la tabla usuarios
                id_usuario_insertado = cursor.lastrowid
                #Insertar datos en la tabla empleados
                cursor.execute("INSERT INTO empleados (id, run, nombre, fecha_nacimiento, id_rol, id_dep, id_jefe) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (id_usuario_insertado, run, nombre_apellido,  fecha_nacimiento, id_rol, id_dep, id_jefe))
                #Confirmar y cerrar base de datos y consulta
                cursor.close()
                db.commit()
                db.close()
                #Cerrar la ventana de creacion de empleados
                messagebox.showinfo("Éxito", "El usuario fue creado con exito")
                self.ventana_creacion_empleado.destroy()
                self.actualizar_tabla_empleados()
            except Exception as e:
                #Mostrar mensaje de error en caso de fallo y el fallo por consola
                messagebox.showinfo("Error", "Error al consultar los datos en la base de datos")
                print(e)
        else:
            print(run,nombre_apellido,fecha_nacimiento,id_rol,id_dep,password)
            messagebox.showinfo("Error", "Ingrese todo los datos")

        #funcion usada en mostrar_empleados para mostrar los empleados
    def obtener_datos(self):
        db = sql.connect(host="localhost", user="root", passwd="", database="sistema_ordenes")
        cursor = db.cursor()
        cursor.execute("SELECT nombre, run FROM empleados")
        self.empleados=cursor.fetchall()
        cursor.close()
        db.close()

        #funciona para actualizar la tabla de los empleados
    def actualizar_tabla_empleados(self):
        #Verificar si self.tree es None
        if self.tree is not None:
            #Limpiar el tree view
            for item in self.tree.get_children():
                self.tree.delete(item)           
            #Mostrar datos actualizados
            self.obtener_datos()          
            #Insertar datos actualizados en el treeview
            for self.empleado in self.empleados:
                self.tree.insert('', 'end', values=self.empleado)

        #Funcion para borrar empleados de la tabla empleados
    def borrar_empleado(self):
       #Seleccion del treeview
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showerror("Error", "Por favor, selecciona un empleado para borrar")
            return
        #Obtener el nombre del empleado seleccionado
        run_empleado = self.tree.item(seleccion, 'values')[1]
        respuesta = messagebox.askyesno("Borrar Empleado", f"¿Estás seguro de borrar el empleado {run_empleado}?")
        if respuesta:
            #Conectar a la base de datos
            db = sql.connect(host="localhost", user="root", passwd="", database="sistema_ordenes")
            cursor = db.cursor()
            try:
                #Obtener el id del empleado desde la tabla empleados
                cursor.execute("SELECT id FROM empleados WHERE run = %s", (run_empleado,))
                resultado = cursor.fetchone()
                if resultado:
                    id_empleado = resultado[0]
                    #Leer los resultados
                    cursor.fetchall()
                    #Borrar el empleado de la tabla empleados
                    cursor.execute("DELETE FROM empleados WHERE id = %s", (id_empleado,))
                    #Borrar el usuario de la tabla usuarios
                    cursor.execute("DELETE FROM usuarios WHERE id = %s", (id_empleado,))
                    #Confirmar los cambios, cerrar la db y consulta
                    cursor.close()
                    db.commit()
                    db.close()
                    #Actualizar la tabla despues de borrar el empleado
                    self.actualizar_tabla_empleados()
                    messagebox.showinfo("Éxito", "Empleado borrado exitosamente.")
                else:
                    messagebox.showwarning("Advertencia", "No se encontró el empleado en la base de datos.")
            except Exception as e:
                #Manejar errores
                messagebox.showerror("Error", f"Error al borrar el empleado: {str(e)}")
        #funcion usada para guardar los datos que se actualizen en la tabla empleados
    def guardar_datos_actualizados_empleados(self):
                    #Obtener los nuevos valores de empleado
                    nuevo_run = self.run_var.get()
                    nuevo_nombre = self.nombre_var.get()
                    nueva_fecha_nacimiento = self.fecha_nacimiento_var.get()
                    id_rol = {'ADMIN':1,'USUARIO':2,'TECNICO':3}.get(self.id_rol_var.get(), None)
                    id_dep = {'JEFATURA':1,'TIC':2,'TECNICOS':3}.get(self.id_dep_var.get(), None)
                    #conectar la base de datos y crear consulta
                    db = sql.connect(host="localhost", user="root", passwd="", database="sistema_ordenes")
                    cursor = db.cursor()
                    try:
                        #Actualizar la tabla empleados
                        cursor.execute("UPDATE empleados SET run=%s, nombre=%s, foto= NULL, fecha_nacimiento=%s, id_rol=%s, id_dep=%s WHERE id=%s",
                                    (nuevo_run, nuevo_nombre, nueva_fecha_nacimiento, id_rol,id_dep, self.id_empleado))
                        #Actualizar la tabla usuarios
                        nuevo_correo = self.correo_var.get()
                        nueva_contraseña = self.contraseña_var.get()
                        cursor.execute("UPDATE usuarios SET correo=%s, password=%s WHERE id=%s",
                                    (nuevo_correo, nueva_contraseña,self.id_empleado))
                        #Confirmar los cambios, cerrar la db y consulta
                        cursor.close()
                        db.close()
                        db.commit()
                        #Cerrar la ventana de edicion
                        messagebox.showinfo("Éxito", "Datos actualizados con éxito.")
                        self.ventana_edicion.destroy()
                        #Actualizar la tabla después de editar el empleado
                        self.actualizar_tabla_empleados()
                        messagebox.showinfo("Éxito", "Empleado actualizado exitosamente.")
                    except Exception as e:
                        #Manejar errores
                        messagebox.showerror("Error", f"Error al editar el empleado: {str(e)}")
                        print(e)
        #Funcion para obtener los usuarios que sean jefes en editar empleados
    def obtener_jefes_empleados(self):
            db = sql.connect(host="localhost", user="root", passwd="", database="sistema_ordenes")
            cursor = db.cursor()
            cursor.execute("SELECT id_emp FROM empleados WHERE id_dep=1")
            jefes = cursor.fetchall()
            cursor.close()
            db.close()
            return jefes
        #funcion para crear un nuevo departamento
    def crear_departamento(self):
        #Nombre del nuevo departamento
        nombre_departamento = simpledialog.askstring("Crear Departamento", "Ingrese el nombre del nuevo departamento:")
        if nombre_departamento:
            try:
                db = sql.connect(host="localhost", user="root", passwd="", database="sistema_ordenes")
                cursor = db.cursor()
                cursor.execute("INSERT INTO departamentos (departamento) VALUES (%s)", (nombre_departamento,))
                cursor.close()
                db.commit()
                db.close()
                messagebox.showinfo("Éxito", f"Se creó el departamento: {nombre_departamento}")
                self.actualizar_treeview_departamentos()
            except Exception as e:
                messagebox.showerror("Error", f"Error al crear el departamento: {str(e)}")
        #editar un departamento
    def editar_departamento(self):
        #seleccion del treeview
        seleccion = self.tree_departamentos.selection()
        if not seleccion:
            messagebox.showerror("Error", "Selecciona un departamento para editar.")
            return
        #Obtener el id_dep y departamento de la seleccion en el treeview
        id_departamento = self.tree_departamentos.item(seleccion, 'values')[0]
        nombre_departamento = self.tree_departamentos.item(seleccion, 'values')[1]
        #dialogo para ingresar el nuevo nombre
        nuevo_nombre = tk.simpledialog.askstring("Editar Departamento", f"Ingrese el nuevo nombre para {nombre_departamento}:")
        if nuevo_nombre:
            try:
                db = sql.connect(host="localhost", user="root", passwd="", database="sistema_ordenes")
                cursor = db.cursor()
                cursor.execute("UPDATE departamentos SET departamento = %s WHERE id_dep = %s", (nuevo_nombre, id_departamento))
                cursor.close()
                db.commit()
                db.close()
                messagebox.showinfo("Éxito", f"Se actualizo el departamento {nombre_departamento} a {nuevo_nombre}")
                self.actualizar_treeview_departamentos()
            except Exception as e:
                messagebox.showerror("Error", f"Error al editar el departamento: {str(e)}")
        #borrar un departamento
    def borrar_departamento(self):
        #seleccion del treeview
        seleccion = self.tree_departamentos.selection()
        if not seleccion:
            messagebox.showerror("Error", "Por favor, selecciona un departamento para borrar.")
            return
        #Obtener el ID y departamento seleccionado en el treeview
        id_departamento = self.tree_departamentos.item(seleccion, 'values')[0]
        nombre_departamento = self.tree_departamentos.item(seleccion, 'values')[1]
        #Confirmar para borrar
        respuesta = messagebox.askyesno("Borrar Departamento", f"¿Estás seguro de borrar el departamento {nombre_departamento}?")
        if respuesta:
            try:
                db = sql.connect(host="localhost", user="root", passwd="", database="sistema_ordenes")
                cursor = db.cursor()
                cursor.execute("DELETE FROM departamentos WHERE id_dep = %s", (id_departamento,))
                cursor.close()
                db.commit()
                db.close()
                messagebox.showinfo("Éxito", f"Se borró el departamento: {nombre_departamento}")
                self.actualizar_treeview_departamentos()
            except Exception as e:
                messagebox.showerror("Error", f"Error al borrar el departamento: {str(e)}")
        #funcion para actualizar el treeview de departamentos
    def actualizar_treeview_departamentos(self):
        try:
            db = sql.connect(host="localhost", user="root", passwd="", database="sistema_ordenes")
            cursor = db.cursor()
            cursor.execute("SELECT * FROM departamentos")
            departamentos = cursor.fetchall()
            cursor.close()
            db.close()
            #Limpiar el treeview
            for item in self.tree_departamentos.get_children():
                self.tree_departamentos.delete(item)
            #insertar los datos actualizados en el treeview
            for departamento in departamentos:
                self.tree_departamentos.insert("", "end", values=departamento)
        except Exception as e:
            messagebox.showerror("Error", f"Error al actualizar el TreeView: {str(e)}")
        #obtener la cantidad de ordenes terminadas por tecnico
    def obtener_cantidad_ordenes_tecnicos(self):
        try:
            db = sql.connect(host="localhost", user="root", passwd="", database="sistema_ordenes")
            cursor = db.cursor()
            #Consulta para obtener la cantidad de ordenes en estado 3 por run_tecnico
            cursor.execute("SELECT run_tecnico, COUNT(*) as cantidad FROM ordenes WHERE estado = 3 GROUP BY run_tecnico")
            ordenes_tecnicos = cursor.fetchall()
            cursor.close()
            db.close()
            return ordenes_tecnicos
        except Exception as e:
            messagebox.showerror("Error", f"Error al obtener las ordenes por tecnico: {str(e)}")
        #obtener la cantidad de ordenes por departamento
    def obtener_cantidad_ordenes_departamentos(self):
        try:
            db = sql.connect(host="localhost", user="root", passwd="", database="sistema_ordenes")
            cursor = db.cursor()
            #Consulta para obtener la cantidad de ordenes por id_dep y el nombre del departamento
            cursor.execute("SELECT ordenes.id_dep, departamentos.departamento, COUNT(*) as cantidad FROM ordenes ordenes JOIN departamentos departamentos ON ordenes.id_dep = departamentos.id_dep GROUP BY ordenes.id_dep")
            ordenes_departamentos = cursor.fetchall()
            cursor.close()
            db.close()
            return ordenes_departamentos
        except Exception as e:
            messagebox.showerror("Error", f"Error al obtener las órdenes por departamento: {str(e)}")