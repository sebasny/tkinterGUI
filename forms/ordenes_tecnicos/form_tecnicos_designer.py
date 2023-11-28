import tkinter as tk
from tkinter import ttk
import util.generic as utl

class TecnicosDesigner():
   def cerrar_ventana(self):
       pass

   def obtener_datos(self):
       pass
   
   def obtener_detalles_orden(self):
       pass

   def actualizar_orden(self):
       pass

   def finalizar_orden(self):
       pass
   
   def desistir_orden(self):
       pass
   
   def limitar_caracteres(self):
       pass

   def __init__(self):
        #Diseño de la ventana
        self.ventana = tk.Tk()
        self.ventana.title('ORDENES')
        self.ventana.config(bg='#808080')
        self.ventana.resizable(width=False, height=False)
        #Comando para centrar y dar tamaño a la ventana
        utl.centrar_ventana(self.ventana,800,600)
        #comando para cargar el icono de la ventana
        icono = utl.leer_imagen("./images/icon.png", (200, 200))
        self.ventana.iconphoto(True, icono)

        #Crear tabla
        self.tree = ttk.Treeview(self.ventana, columns=("ID Orden", "Categoría", "Estado"), show="headings")
        self.tree.heading("ID Orden", text="ID Orden")
        self.tree.heading("Categoría", text="Categoría")
        self.tree.heading("Estado", text="Estado")
        #Seleccion dentro de la tabla para mostrar detalles
        self.tree.bind("<ButtonRelease-1>", self.mostrar_detalles)

        #Realizar la conexión a la db
        self.obtener_datos()

        # Empaquetar el TreeView
        self.tree.pack(expand=True, fill="both")

        #Acción al cerrar la ventana
        self.ventana.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)

        #Iniciador de la ventana
        self.ventana.mainloop()

   def mostrar_detalles(self, event):
        #Obtener la fila seleccionada
         item = self.tree.selection()[0]

        #Obtener los datos de la fila seleccionada
         datos_fila = self.tree.item(item, 'values')

        #Crear ventana de detalles
         ventana_detalles = tk.Toplevel(self.ventana)
         ventana_detalles.title("Detalles")  
         ventana_detalles.resizable(width=False, height=False)

         #Obtener más detalles de la db
         detalles_orden = self.obtener_detalles_orden(datos_fila[0])

         #Crear etiquetas y mostrar datos
         tk.Label(ventana_detalles, text="ID Orden:").grid(row=0, column=0, sticky='w', padx=5, pady=5)
         tk.Label(ventana_detalles, text=datos_fila[0]).grid(row=0, column=1, sticky='w', padx=5, pady=5)

         tk.Label(ventana_detalles, text="Categoría:").grid(row=1, column=0, sticky='w', padx=5, pady=5)
         tk.Label(ventana_detalles, text=detalles_orden['categoria']).grid(row=1, column=1, sticky='w', padx=5, pady=5)

         tk.Label(ventana_detalles, text="Estado:").grid(row=2, column=0, sticky='w', padx=5, pady=5)
         tk.Label(ventana_detalles, text=detalles_orden['estado']).grid(row=2, column=1, sticky='w', padx=5, pady=5)

         tk.Label(ventana_detalles, text="Detalle:").grid(row=3, column=0, sticky='w', padx=5, pady=5)
         detalle_texto = tk.Text(ventana_detalles, wrap=tk.WORD, width=40, height=5)
         detalle_texto.grid(row=3, column=1, padx=5, pady=5)
         detalle_texto.insert(tk.END, detalles_orden['detalle'])
         detalle_texto.config(state=tk.DISABLED)

         tk.Label(ventana_detalles, text="Fecha Emisión:").grid(row=4, column=0, sticky='w', padx=5, pady=5)
         tk.Label(ventana_detalles, text=detalles_orden['fecha_emision']).grid(row=4, column=1, sticky='w', padx=5, pady=5)

         tk.Label(ventana_detalles, text="Departamento:").grid(row=5, column=0, sticky='w', padx=5, pady=5)
         tk.Label(ventana_detalles, text=detalles_orden['id_dep']).grid(row=5, column=1, sticky='w', padx=5, pady=5)

         tk.Label(ventana_detalles, text="Run Emp:").grid(row=6, column=0, sticky='w', padx=5, pady=5)
         tk.Label(ventana_detalles, text=detalles_orden['run_emp']).grid(row=6, column=1, sticky='w', padx=5, pady=5)

         tk.Label(ventana_detalles, text="RUN Técnico:").grid(row=8, column=0, sticky='w', padx=5, pady=5)
         tk.Label(ventana_detalles, text=detalles_orden.get('run_tecnico', 'No asignado')).grid(row=8, column=1, sticky='w', padx=5, pady=5)

         #Crear botones dependiendo si la orden esta abierta o En Curso
         if detalles_orden['estado'] == "Abierta":
            boton = tk.Button(ventana_detalles, text="Tomar Orden", command=lambda: self.tomar_orden(datos_fila[0], ventana_detalles))
            boton.grid(row=9, column=0, columnspan=2, pady=10)
         elif detalles_orden['estado'] == "En Curso":
            boton_finalizar = tk.Button(ventana_detalles, text="Finalizar Orden", command=lambda: self.finalizar_orden(datos_fila[0], ventana_detalles))
            boton_desistir = tk.Button(ventana_detalles, text="Desistir Orden", command=lambda: self.desistir_orden(datos_fila[0], ventana_detalles))

            boton_finalizar.grid(row=9, column=1, pady=10)
            boton_desistir.grid(row=9, column=0, pady=10)
   
   def tomar_orden(self, id_orden, ventana_detalles):
         #Crear una ventana para ingresar el RUN del técnico
         ventana_run_tecnico = tk.Toplevel(self.ventana)
         ventana_run_tecnico.title("Ingreso")
         ventana_run_tecnico.resizable(width=False, height=False)

         #Label y Entry para ingresar el RUN
         tk.Label(ventana_run_tecnico, text="Ingrese su RUN:").grid(row=0, column=0, padx=5, pady=5)
         run_tecnico_var = tk.StringVar()
         run_tecnico_entry = tk.Entry(ventana_run_tecnico, width=15, textvariable=run_tecnico_var)
         run_tecnico_entry.grid(row=0, column=1, padx=5, pady=5)
         run_tecnico_entry.bind('<Key>', lambda event: self.limitar_caracteres(event, run_tecnico_var, 13))

         # Botón para tomar la orden con el RUN ingresado
         boton_tomar_orden = tk.Button(ventana_run_tecnico, text="Tomar Orden", command=lambda: self.actualizar_orden(id_orden, run_tecnico_entry.get(), ventana_detalles, ventana_run_tecnico))
         boton_tomar_orden.grid(row=1, column=0, columnspan=2, pady=10)