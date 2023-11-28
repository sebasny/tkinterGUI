from forms.ordenes_tecnicos.form_tecnicos_designer import TecnicosDesigner
from tkinter import messagebox
import mysql.connector as sql
from datetime import datetime

class Tecnicos(TecnicosDesigner):
    def __init__(self):
        super().__init__()

    def cerrar_ventana(self):
        #Cerrar la ventana actual y abrir la ventana de login
        self.ventana.destroy()
        from forms.login.form_login import FormLogin
        FormLogin()
    #Funcion para limitar caracteres
    def limitar_caracteres(self, event, variable, max_caracteres):
        if len(variable.get()) > max_caracteres:
            variable.set(variable.get()[:max_caracteres])

    def obtener_datos(self):
     try:
        #Establecer conexión a la db
        db = sql.connect(host="localhost", user="root", passwd="", database="sistema_ordenes")
        #crear el gestor de consulta
        cursor = db.cursor()
        #Ejecutar una consulta
        cursor.execute("SELECT id_orden, categoria, estado FROM ordenes WHERE estado <> 3")
        #Obtener todas las filas de resultados
        filas = cursor.fetchall()
        #Cerrar la conexión
        cursor.close()
        db.close()
        #Cambiar los datos de su id a su nombre
        categoria_numero = {1: "Hardware", 2: "Software", 3: "Red"}
        estado_numero = {1: "Abierta", 2: "En Curso"}

        #Insertar los datos en el treeview
        for fila in filas:
            id_orden, categoria, estado = fila
            categoria_texto = categoria_numero.get(categoria, None)
            estado_texto = estado_numero.get(estado, None)
            self.tree.insert("", "end", values=(id_orden, categoria_texto, estado_texto))

     except Exception as e:         
            #Mostrar mensaje de error en caso de fallo y el fallo por consola
            messagebox.showinfo("Error", "Error al consultar los datos en la base de datos")
            print(e)

    def obtener_detalles_orden(self, id_orden):
        detalles_orden = {}
        try:
            #Establecer conexión a la base de datos MySQL
            db = sql.connect(host="localhost", user="root", passwd="", database="sistema_ordenes")
            cursor = db.cursor(dictionary=True)
            cursor.execute("SELECT detalle, fecha_emision, id_dep, run_emp, categoria, estado, run_tecnico FROM ordenes WHERE id_orden = %s", (id_orden,))
            detalles_orden = cursor.fetchone()
            cursor.close()
            db.close()
            detalles_orden['categoria'] = {1: "Hardware", 2: "Software", 3: "Red"}.get(detalles_orden['categoria'], "")
            detalles_orden['estado'] = {1: "Abierta", 2: "En Curso", 3: "Finalizado"}.get(detalles_orden['estado'], "")
            detalles_orden['id_dep'] = {1:"Jefatura",2:"TIC",3: "Tecnicos"}.get(detalles_orden['id_dep'], "")

        except Exception as e:         
            messagebox.showinfo("Error", "Error al consultar los datos en la base de datos")
            print(e)

        return detalles_orden
    
    def finalizar_orden(self, id_orden, ventana_detalles):
        try:
            
            db = sql.connect(host="localhost", user="root", passwd="", database="sistema_ordenes")
            cursor = db.cursor()
            fecha_termino = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cursor.execute("UPDATE ordenes SET estado=3, fecha_termino=%s WHERE id_orden=%s", (fecha_termino, id_orden))
            cursor.close()
            db.commit()
            db.close()

        # Mostrar mensaje de confirmación
            self.actualizar_tabla()
            messagebox.showinfo("Éxito", "La orden ha sido finalizada correctamente.")

        except Exception as e:         
            messagebox.showinfo("Error", "Error al consultar los datos en la base de datos")
            print(e)

        finally:
            #Cerrar la ventana de detalles de la orden
            if ventana_detalles and ventana_detalles.winfo_exists():
                ventana_detalles.destroy()

    def desistir_orden(self, id_orden, ventana_detalles):
        respuesta = messagebox.askyesno("Dejar orden", "¿Estás seguro de abrir la orden?")
        if respuesta:
            try:
                db = sql.connect(host="localhost", user="root", passwd="", database="sistema_ordenes")
                cursor = db.cursor()
                cursor.execute("UPDATE ordenes SET estado=1, run_tecnico=NULL, fecha_termino=NULL WHERE id_orden=%s", (id_orden,))
                cursor.close()
                db.commit()
                db.close()
            # Mostrar mensaje de confirmación
                self.actualizar_tabla()
                messagebox.showinfo("Éxito", "La orden se abrio denuevo")
                #Cerrar la ventana de detalles de la orden
                if ventana_detalles and ventana_detalles.winfo_exists():
                    ventana_detalles.destroy()

            except Exception as e:         
                messagebox.showinfo("Error", "Error al consultar los datos en la base de datos")
                print(e)

    def actualizar_orden(self, id_orden, run_tecnico, ventana_detalles, ventana_run_tecnico):
        if run_tecnico != "":
            try:
                db = sql.connect(host="localhost", user="root", passwd="", database="sistema_ordenes")
                cursor = db.cursor()
                cursor.execute("UPDATE ordenes SET run_tecnico=%s, estado=2 WHERE id_orden=%s", (run_tecnico, id_orden))
                cursor.close()
                db.commit()
                db.close() 

                #Acrualiza los datos y mustra un mensaje por pantalla
                self.actualizar_tabla()
                messagebox.showinfo("Éxito", "La orden ha sido tomada con éxito.")
                #Cerrar las ventanas
                ventana_detalles.destroy()
                ventana_run_tecnico.destroy()
                self.ventana.focus_set()

            except Exception as e:         
                    messagebox.showinfo("Error", "Error al consultar los datos en la base de datos")
                    print(e)
        else:
            messagebox.showinfo("Error", "Porfavor ingrese un run")

    def actualizar_tabla(self):
    # Limpiar el treeview
     for item in self.tree.get_children():
        self.tree.delete(item)
    #Mostrar datos
     self.obtener_datos()