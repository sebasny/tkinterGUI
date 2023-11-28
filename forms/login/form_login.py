from tkinter import messagebox
import mysql.connector as sql
from forms.master_panel.form_master import MasterPanel
from forms.ordenes.form_ordenes import Ordenes
from forms.login.form_login_designer import FormLoginDesigner
from forms.ordenes_tecnicos.form_tecnicos import Tecnicos


class FormLogin(FormLoginDesigner):

    def consulta(self,usuario,password):
        #Conectar a la base de datos almacenado en db
        db = sql.connect(host="localhost",user="root",passwd="",database="sistema_ordenes")
        #crear el gestor de consulta
        cursor = db.cursor()
        #Generar consulta
        consulta = "SELECT id_rol FROM usuarios WHERE correo = %s AND password = %s"
        datos = (usuario, password)
        #Ejecutar consulta
        cursor.execute(consulta,datos)
        #Almacenar consulta
        resultado = cursor.fetchone()
        #Cerrar conexion
        cursor.close
        db.close
        return resultado
    
#funcion para redireccionar a ventanas    
    def redireccion(self,id_rol):
        if id_rol == 1:
            self.ventana.destroy()
            MasterPanel()
        if id_rol == 2:
            self.ventana.destroy()
            Ordenes()
        if id_rol == 3:
            self.ventana.destroy()
            Tecnicos()
            
#funcion para verificar datos de la consulta          
    def verificar(self):
        usuario = self.usuario.get()
        contraseña = self.password.get()
        id_rol = self.consulta(usuario,contraseña)
        if id_rol:
            id_rol = id_rol[0]
            self.redireccion(id_rol)
        else:
            messagebox.showerror(
                message="El usuario no existe", title="ADVERTENCIA",parent=self.ventana)