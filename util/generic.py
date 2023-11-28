from PIL import ImageTk, Image

#Funcion para cargar imagenes y ajustarlas
def leer_imagen( path, size): 
        return ImageTk.PhotoImage(Image.open(path).resize(size, Image.LANCZOS))  

#Funcion para centrar ventana y darle tamaño en pixeles
def centrar_ventana(ventana,aplicacion_ancho,aplicacion_largo):    
    pantall_ancho = ventana.winfo_screenwidth()
    pantall_largo = ventana.winfo_screenheight()
    x = int((pantall_ancho/2) - (aplicacion_ancho/2))
    y = int((pantall_largo/2) - (aplicacion_largo/2))
    return ventana.geometry(f"{aplicacion_ancho}x{aplicacion_largo}+{x}+{y}")