import tkinter as tk
from tkinter import ttk
from tkinter.font import BOLD
import util.generic as utl

class FormLoginDesigner:
    
    def verificar(self):
        pass
    
    def __init__(self):
        #Diseño de la ventana
        self.ventana = tk.Tk()
        self.ventana.title('INACAP')
        self.ventana.config(bg='#FFFFFF')
        self.ventana.resizable(width=False, height=False)
        #Comando para definir tamaño y centrar la ventana
        utl.centrar_ventana(self.ventana,800,450)
        #Comando para cargar logo inacao y icono de la ventana
        icono =utl.leer_imagen("./images/icon.png", (200,200))
        logo =utl.leer_imagen("./images/logo.png", (200,200))
        self.ventana.iconphoto(True, icono)

        #Marco del logo de inacap
        frame_logo = tk.Frame(self.ventana, bd=0, width=250, relief=tk.SOLID, padx=10,pady=10, bg='#ffffff' )
        frame_logo.pack(side='left',expand=tk.NO,fill=tk.BOTH)
        label = tk.Label(frame_logo, image=logo,bg='#ffffff')
        label.place(x=0,y=0,relwidth=1, relheight=1)
        
        #Marco principal
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg='#808080')
        frame_form.pack(side='right',expand=tk.YES,fill=tk.BOTH)
        
        #Marco superior "Iniciar sesion"
        frame_form_top =  tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.pack(side="top",fill=tk.X)
        title = tk.Label(frame_form_top, text=' Inicio de sesion',font=('Arial black', 30), fg="#000", bg='#808080',pady=50)
        title.pack(expand=tk.YES,fill=tk.BOTH)
        
        #Marco de formulario
        frame_form_fill = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg='#808080')
        frame_form_fill.pack(side='bottom', expand=tk.YES,fill=tk.BOTH)
        
        #Labels y Entrys
        etiqueta_usuario = tk.Label(frame_form_fill, text="Usuario",font=('Arial black', 14), fg="#000", bg='#808080',anchor="w")
        etiqueta_usuario.pack(fill=tk.X, padx=20, pady=5)
        self.usuario = ttk.Entry(frame_form_fill, font=('Arial black', 14))
        self.usuario.pack(fill=tk.X, padx=20,pady=10)
        
        etiqueta_password = tk.Label(frame_form_fill, text="Contraseña",font=('Arial black', 14), fg="#000", bg='#808080',anchor="w")
        etiqueta_password.pack(fill=tk.X, padx=20, pady=5)
        self.password= ttk.Entry(frame_form_fill, font=('Arial black', 14))
        self.password.pack(fill=tk.X, padx=20,pady=10)
        self.password.config(show='*')
        
        inicio = tk.Button(frame_form_fill,text="Iniciar sesion",font=("Arial black", 15, BOLD),bg=('#666666'),bd=0, fg="#fff",command=self.verificar)
        inicio.pack(fill=tk.X, padx=20, pady=20)
        self.ventana.bind("<Return>", (lambda event: self.verificar()))
        
        #Iniciador de la ventana
        self.ventana.mainloop()
