import tkinter as tk
from tkinter import ttk
import util.generic as utl
from tkinter.font import BOLD

class OrdenesDesigner:

    def limitar_caracteres(self):
        pass

    def cerrar_ventana(self):
        pass

    def subir_datos(self):
        pass
    
    def __init__(self):
        #Diseño de la ventana
        self.ventana = tk.Tk()
        self.ventana.title('ORDENES')
        self.ventana.config(bg='#808080')
        self.ventana.resizable(width=False, height=False)
        #Comando para centrar y dar tamaño a la ventana
        utl.centrar_ventana(self.ventana,550,260)
        #comando para cargar el icono de la ventana
        icono = utl.leer_imagen("./images/icon.png", (200, 200))
        self.ventana.iconphoto(True, icono)
        #accion para enlazar el enter
        self.ventana.bind("<Return>", (lambda event: self.subir_datos()))
       #Acción al cerrar la ventana
        self.ventana.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)

        #Variables para almacenar los valores de la orden
        self.categoria_var = tk.StringVar(self.ventana)
        self.detalle_var = tk.StringVar(self.ventana)
        self.departamento_var = tk.StringVar(self.ventana)
        self.run_emp_var = tk.StringVar(self.ventana)

        #Marco principal
        orden_frame = ttk.Frame(self.ventana, padding=20, style="My.TFrame")
        orden_frame.grid(row=4, column=1,sticky=tk.W)

        #Eliminar bordes grises alrededor del frame
        style = ttk.Style()
        style.configure("My.TFrame", background='#808080')

        #mensajes
        self.mesage = ttk.Label(orden_frame, text = '', foreground= 'red',background="#808080",font=("Arial",12,BOLD))
        self.mesage.grid(row=4, column=1, pady=(10, 0), padx=(0, 10), sticky=tk.W)

        #Labels y Entrys
        ttk.Label(orden_frame, text="Categoría:", font=("Arial", 12), background='#808080').grid(row=0, column=0, pady=(0, 5), padx=(10, 0), sticky=tk.W)
        categoria_menu = ttk.Combobox(orden_frame, textvariable=self.categoria_var, values=["Hardware", "Software", "Red"], state="readonly", width=20, font=("Arial", 12))
        categoria_menu.grid(row=0, column=1, pady=5, padx=(0, 10), sticky=tk.W)

        ttk.Label(orden_frame, text="Detalle:", font=("Arial", 12), background='#808080').grid(row=1, column=0, pady=(10, 5), padx=(10, 0), sticky=tk.W)
        detalle_text = tk.Entry(orden_frame, textvariable=self.detalle_var, width=40, font=("Arial", 12))
        detalle_text.grid(row=1, column=1, pady=5, padx=(0, 10), sticky=tk.W)
        detalle_text.bind('<Key>', lambda event: self.limitar_caracteres(event, self.detalle_var, 399))

        ttk.Label(orden_frame, text="Departamento:", font=("Arial", 12), background='#808080').grid(row=2, column=0, pady=(10, 5), padx=(10, 0), sticky=tk.W)
        departamento_menu = ttk.Combobox(orden_frame, textvariable=self.departamento_var, values=["Jefatura", "TIC", "Tecnicos"], state="readonly", width=20, font=("Arial", 12))
        departamento_menu.grid(row=2, column=1, pady=5, padx=(0, 10), sticky=tk.W)

        ttk.Label(orden_frame, text="RUT del Empleado:", font=("Arial", 12), background='#808080').grid(row=3, column=0, pady=(10, 5), padx=(10, 0), sticky=tk.W)
        run_emp_entry = ttk.Entry(orden_frame, textvariable=self.run_emp_var, width=20, font=("Arial", 12))
        run_emp_entry.grid(row=3, column=1, pady=5, padx=(0, 10), sticky=tk.W)
        run_emp_entry.bind('<Key>', lambda event: self.limitar_caracteres(event, self.run_emp_var, 12))

        #Boton de enviar
        style = ttk.Style()
        style.configure("My.TButton", font=("Arial", 14, BOLD))
        ttk.Button(orden_frame, text="Enviar", command=self.subir_datos, width=20, style="My.TButton").grid(row=5, column=1, pady=(10, 0), padx=(0, 10), sticky=tk.W,ipady=7)

       #Iniciador de la ventana
        self.ventana.mainloop()
