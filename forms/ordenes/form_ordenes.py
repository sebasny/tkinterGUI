from forms.ordenes.form_ordenes_designer import OrdenesDesigner
import mysql.connector as sql
from datetime import datetime

class Ordenes(OrdenesDesigner):
    
    def __init__(self):
        super().__init__()
 
    #funcion para limitar los caracteres en los entry
    def limitar_caracteres(self, event, variable, max_caracteres):
        if len(variable.get()) > max_caracteres:
            variable.set(variable.get()[:max_caracteres])
            
    def cerrar_ventana(self):
        #Cerrar la ventana actual y abrir la ventana de login
        self.ventana.destroy()
        from forms.login.form_login import FormLogin
        FormLogin()

    def subir_datos(self):
        #Obtener los valores de la orden
        categoria = self.categoria_var.get()
        detalle = self.detalle_var.get()
        fecha_emision = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        departamento = self.departamento_var.get() 
        run_emp = self.run_emp_var.get()
        estado = "1"
        #Cambiar las categorias y departamentos a sus respectivos id en la base de datos
        categoria_numero = {"Hardware": 1, "Software": 2, "Red": 3}.get(categoria, None)
        departamento_numero = {"Jefatura": 1, "TIC": 2, "Tecnicos": 3}.get(departamento, None)

        #Comprobar que ningun campo este vacio
        if categoria_numero is not None and departamento_numero is not None and detalle != "" and run_emp != "":
            try:
                #Conectar a la base de datos almacenado en db
                db = sql.connect(host="localhost", user="root", passwd="", database="sistema_ordenes")
                #crear el gestor de consulta
                cursor = db.cursor()
                #Generar consulta
                query = "INSERT INTO ordenes (categoria, detalle, fecha_emision, id_dep, run_emp, estado) VALUES (%s, %s, %s, %s, %s, %s)"
                values = (categoria_numero, detalle, fecha_emision, departamento_numero, run_emp, estado)
                #Ejecutar consulta
                cursor.execute(query, values)
                #Confirmar y cerrar la conexión
                cursor.close()
                db.commit()
                db.close()
                #limpiar los entry
                self.categoria_var.set("")
                self.detalle_var.set("")
                self.departamento_var.set("")
                self.run_emp_var.set("")
                #Actualizar el mensaje para verificar si se subio la orden
                self.mesage['foreground'] = 'green'
                self.mesage['text'] = 'ORDEN ENVIADA'
            except Exception as e:
                #Mostrar mensaje de error en caso de fallo y el fallo por consola
                self.mesage['foreground'] = 'red'
                self.mesage['text'] = 'ERROR'
                print(e)
        else:
            #Mostrar advertencia si no se llenan todos los campos
            self.mesage['foreground'] = 'red'
            self.mesage['text'] = 'LLENE TODOS LOS CAMPOS'