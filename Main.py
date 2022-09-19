#Librerias utilizadas
from tkinter import *
from tkinter.ttk import Notebook
from PIL import Image, ImageTk 
from tkinter.filedialog import askopenfile, askopenfilename
from Funcion_Alg_Genetico import *

#================================================================
#===================    Aplicacion Main  ========================
#================================================================
class App(Tk):
    #Inicializamos los parametros - constructores
    def __init__(self):
        #CREAMOS LA VENTANA
        super().__init__()
        self.title("PruebaPrueba")    #PONGO TITULO
        self.geometry("1000x800+310+30") #TAMAÑO
        self.create_widgets()            #FUNCION CREA TODO LO QUE ESTA DENTRO
        self.overrideredirect(True)      #SIN CONTORNO DE BARRA 
        self.ruta="" #RUTA DE INPUT
        self.valor=1 #VALOR ES PARA PONER SI ES MAÑANA O TARDE, ...
        self.personalizado=False
        self.CreditosMinimos=IntVar()
        self.CreditosMaximos=IntVar()
        self.EntryCreditosMin=None
        self.EntryCreditosMax=None
    def create_widgets(self):

        #FUNCION QUE ACTUALIZA LOS RADIO BUTTOM
        def actualizar(value):   
            self.valor=int(value)
        
        #CREAMOS LOS PANELES - FRAMES
        self.Marco_Frame=Frame(self,bg="#5e1725")
        self.Marco_Frame.pack(side="top",fill="both",ipady=5)

        # Primer Frame
        self.Primer_Frame=Frame(self,bg='#5e1725',border=0)
        self.Primer_Frame.pack(side="top",fill="both")

        self.Marco_Frame2=Frame(self,bg="#5e1725")
        self.Marco_Frame2.pack(side="top",fill="both",ipady=5)

        self.Marco_Frame3=Frame(self,bg="white")
        self.Marco_Frame3.pack(side="top",fill="both",ipady=1)
        
        # Segundo Frame
        self.Segundo_Frame=Frame(self,bg='#5e1725')
        self.Segundo_Frame.pack(side="top",fill="both",expand=True)


        

        #Boton Salir
        self.btnGenerar=Button(self.Primer_Frame,
                                text="SALIR",
                                padx=10,pady=50,
                                border=2,
                                bg='#5e1725',
                                fg="white",
                                command=exit).pack(side="right")
        
        #Boton Generar Horarios
        self.btnGenerar=Button(self.Primer_Frame,
                                text="GENERAR HORARIOS",
                                padx=10,pady=50,
                                border=2,
                                bg='#5e1725',
                                fg="white",
                                command=self.GenerarHorario).pack(side="right")

        #Boton Input
        self.btnInput=Button(self.Primer_Frame,
                                text="INPUT",   
                                padx=10,
                                pady=50,
                                border=2,
                                bg='#5e1725',
                                fg="white",
                                command=self.AbrirArchivo).pack(side="right")
        
        #Label imagen
        self.LogoUnsaac=ImageTk.PhotoImage(Image.open("unsaac.png").resize((100,128)))
        lbl_LogoUnsaac=Label(self.Primer_Frame,image=self.LogoUnsaac)
        lbl_LogoUnsaac.config(border=0)
        lbl_LogoUnsaac.pack(side="left")

        Label(self.Primer_Frame,text="GENERADOR \nDE HORARIOS",
                font=('Arial',30),
                bg="#5e1725",
                fg="white").pack(padx=10,pady=10,side="left")
        
        # Frame Radio
        self.opcion=IntVar()
        self.opcion.set(value=1)
        self.FrameRadio=Frame(self.Primer_Frame).pack(side="left",fill=BOTH)
        Radiobutton(self.Primer_Frame,
                    text="TURNO MAÑANA",
                    value=1,border=1,
                    variable=self.opcion,
                    command=lambda: actualizar(self.opcion.get()),
                    bg="#5e1725",
                    fg="red").pack(side="top",fill=BOTH,ipadx=2,ipady=4)
        Radiobutton(self.Primer_Frame,
                    text="TURNO TARDE     ",
                    value=2,border=1,
                    variable=self.opcion,
                    command=lambda: actualizar(self.opcion.get()),
                    bg="#5e1725",
                    fg="red").pack(side="top",fill=BOTH,ipadx=2,ipady=4)
        Radiobutton(self.Primer_Frame,
                    text="TURNO CASUAL  ",
                    value=3,border=0,
                    variable=self.opcion,
                    command=lambda: actualizar(self.opcion.get()),
                    bg="#5e1725",
                    fg="red").pack(side="top",fill=BOTH,ipadx=2,ipady=4)
        Button(self.Primer_Frame,
                    text="TURNO PERSONALIZADO",
                    border=0,
                    command=self.createNewWindow,
                    bg="#5e1725",
                    fg="white",
                    ).pack(side="top",fill=BOTH,ipadx=2,ipady=4)


        #Label Unsaac Centro
        self.lblVerificacion=Label(self.FrameRadio,
                    text="Subido \nCorrectamente",
                    font=("Arial",15),
                    bg='#5e1725',
                    fg="white")
        self.limpiar=Button(self.FrameRadio,
                    border=0,
                    bg='#5e1725',
                    fg="white",
                    text="LIMPIAR",
                    font=('Arial',15),
                    command=self.clearFrame)

    #Nueva ventana para elegir los creditos
    def createNewWindow(self):
        self.CreditosMaximos=IntVar()
        def Guardar():
            self.personalizado=True
            self.CreditosMinimos=int(self.CreditosMinimos.get())
            self.CreditosMaximos=int(self.CreditosMaximos.get())
            print("Minimos:",self.CreditosMinimos)
            print("Maximo: ",self.CreditosMaximos)
            ventanaNew.destroy()

        def Salir():
            ventanaNew.destroy()
        ventanaNew = Toplevel(app)
        ventanaNew.geometry("300x250+650+120")
        ventanaNew.overrideredirect(True)
        
        #Titulo
        Label(ventanaNew,
                    text="PERSONALIZAR",
                    font=("Arial",15)).pack(ipadx=8,ipady=8)

        # CREDITOS MAXIMOS
        Label(ventanaNew,
                    text="Minimos Creditos",
                    font=("Arial",12)).pack(ipadx=5,ipady=5)
        self.EntryCreditosMin=Entry(ventanaNew,
                                border=0,
                                font=("Arial",18),
                                bg='#5e1725',
                                fg="white",
                                textvariable=self.CreditosMinimos).pack()

        # CREDITOS MINIMOS
        Label(ventanaNew,
                    text="Maximos Creditos",
                    font=("Arial",12)).pack(ipady=2)
        self.EntryCreditosMax=Entry(ventanaNew,
                                border=0,
                                bg='#5e1725',
                                fg="white",
                                font=("Arial",18),
                                textvariable=self.CreditosMaximos).pack()
        
        #Bottom para salir
        Button(ventanaNew,
                text="Salir",
                border=0,
                bg='#5e1725',
                fg="white",
                font=('Arial',12),
                command=Salir,padx=5,pady=5).pack(expand=True,side="right")

        #Buttom para Guardar
        Button(ventanaNew,
                text="Guardar",
                border=0,
                bg='#5e1725',
                fg="white",
                font=('Arial',12),
                command=Guardar,padx=5,pady=5).pack(expand=True,side="right")
    #LIMPIA LA PARTE DEL
    def clearFrame(self):
    # destroy all widgets from frame
        for widget in self.Segundo_Frame.winfo_children():
            widget.destroy()
    
    #Abrir el csv
    def AbrirArchivo(self):
        try:
            self.ruta=askopenfilename(title="Abrir CSV")
            self.lblVerificacion.pack(padx=2,pady=2,side="right",expand=True)
            self.limpiar.pack(padx=2,pady=2,side="right",expand=True)
        except:
            self.lblVerificacion.config(text="ERROR\nVUELVE A INTENTAR")
    
    #Aplicacion del algoritmo genetico
    def GenerarHorario(self):
        try:
            
            #CAMBIAR LABEL
            self.lblVerificacion.config(text="GENERADO\nEXITOSAMENTE",font=('Arial',10))

            #GENERAMOS EL HORARIO, ANTES IMPORTAMOS EL INPUT
            if(self.personalizado):
                HorarioGenerado=AlgoritmoGenetico(InputCsv(self.ruta),self.valor,self.CreditosMaximos,self.CreditosMinimos)
            else:
                HorarioGenerado=AlgoritmoGenetico(InputCsv(self.ruta),self.valor)
            #---------- Creamos una area -----------------------
            tablayout=Notebook(self.Segundo_Frame)
            #tabla2
            tab1=Frame(tablayout) # Agrego
            tab1.pack(fill="both") # Determino su dimension

            for rows in range(15):
                for columns in range(6):
                    if(rows==0): 
                        label=Label(tab1,text=HorarioGenerado[rows][columns],bg="white",fg="black",padx=9,pady=9)
                        label.config(font=('Arial',12))
                        label.grid(row=rows,column=columns,sticky="nsew",padx=0,pady=0)
                        tab1.grid_columnconfigure(columns,weight=1)
                    else:
                        label=Label(tab1,text=HorarioGenerado[rows][columns],bg="#BEDBED",fg="black",padx=8,pady=8)
                        label.grid(row=rows,column=columns,sticky="nsew",padx=1,pady=1)
                        tab1.grid_columnconfigure(columns,weight=1)
            tablayout.add(tab1,text="Tab 1")
            tablayout.pack(fill="both")
            self.Primer_Frame.config(bg="#5e1725")
        except:
            self.lblVerificacion.config(text="NO SE PUDO\nGENERAR HORARIO",font=('Arial',10))

# ---------- PROGRAMA PRINCIPAL -----------
if __name__=="__main__":
    app=App()
    app.mainloop() #EJECUTAR
