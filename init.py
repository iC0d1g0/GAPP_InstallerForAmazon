import tkinter
from tkinter import *
from tkinter import ttk

class Interfaz(object):
    def __init__(self) -> None:
        #Creacion de la ventana
        self.ventana=Tk()
        self.ventana.title('GAPP Installer |v0.01')
        self.ventana.geometry('400x600')
        self.ventana.configure(background='#B2E351')
        self.ventana.resizable(False, False)

        #Cargamos imagen y logo de google_play
        self.googleplay ='google_play.png'
        self.test3 = PhotoImage(file=self.googleplay)
        self.logoamazon=Label(self.ventana, image=self.test3,background='#B2E351')
        self.logoamazon.place(x='240', y='15')


        #imagen y logo de amazon
        self.amazonlogo ='amazon_.png'
        self.test2 = PhotoImage(file=self.amazonlogo)
        self.logoamazon=Label(self.ventana, image=self.test2,background='#B2E351')
        self.logoamazon.place(x='140', y='15')
        
        #Logo de wahtasapp
        whatsappimg ='whatsapp_.png'
        whatsapp_ = PhotoImage(file=whatsappimg)
        self.whatsapplabel=Label(self.ventana, image=whatsapp_, background='#B2E351')
        self.whatsapplabel.place(x='230', y='520')

         #Logo de telegram
        self.telegram ='telegram.png'
        self.telegram_ = PhotoImage(file=self.telegram)
        self.telegramlabel=Label(self.ventana, image=self.telegram_, background='#B2E351')
        self.telegramlabel.place(x='280', y='520')

         #Logo de twitter
        self.twitter_ ='twitter.png'
        self.twitter = PhotoImage(file=self.twitter_)
        self.twitterlabel=Label(self.ventana, image=self.twitter, background='#B2E351')
        self.twitterlabel.place(x='330', y='510')

      
        
        #logo de Android
        #ADDERLIS AGREGANDO ALGO 
        self.image1 ='andoird.png'
        self.test = PhotoImage(file=self.image1)
        self.logoamazon=Label(self.ventana, image=self.test, background='#B2E351')
        self.logoamazon.place(x='70', y='15')

        #Label del registro arriba
        self.registrotexto=Label(self.ventana, text='Registro', font=['Arial',8], background='#B2E351')
        self.registrotexto.place(x='10', y='60')

        #USUARIOS DIFERENTES

        #Logo al pie de pagina creador de este codigo
        self.icodigotexto=Label(self.ventana, text='by iCodigo Unlocker RD', font=['Arial',11], background='#B2E351', fg='black')
        self.icodigotexto.place(x='230', y='570')
        

        
        #Consola de salida para el usuario.........
        self.cabzera=Frame(self.ventana, background='black')
        self.consola = Text(self.cabzera, height='30', width='29', bd=5, background='#8A8A8A', font=['Arial',8],fg='white' , cursor='watch').grid(column=0, row=0, padx='5',pady='5')
        self.cabzera.place(x='10', y='80')

        #boton de usuario simple
        self.botonesframe= Frame(self.ventana, background='#B2E351')
        self.gapp = Label(self.botonesframe, text='Google PlayServices OneClick', background='#B2E351').grid(column=0, row=0, pady='10', padx='10')
        self.gapp = Button(self.botonesframe, text='GAPPs', bd=7, background='yellow', cursor='arrow').grid(column=0, row=1)
        self.botonesframe.place(x='210', y='80')
        

        #set de botones AVANZADOS no defindos 
        self.botonesframe= Frame(self.ventana, background='#B2E351')
        self.gapp = Label(self.botonesframe, text='AVANZADO', background='#B2E351').grid(column=0, row=0)
        self.Info = Button(self.botonesframe, text='Info',width='7',bd=7, background='yellow', cursor='arrow').grid(column=0, row=1,pady='2')
        self.Instalar = Button(self.botonesframe, text='Instalar', bd=7, background='yellow', cursor='arrow',width='7').grid(column=0, row=2,pady='2')
        self.ApksInstaladas = Button(self.botonesframe, text='instalados',bd=7, background='yellow', cursor='arrow').grid(column=0, row=3, pady='2')
        self.Desintalar = Button(self.botonesframe, text='Desintalar', bd=7, background='yellow', cursor='arrow').grid(column=0, row=4, pady='2')
        self.botonesframe.place(x='263', y='250')





        #Progressbar 
        self.progress =ttk.Progressbar(self.ventana, orient='horizontal',
                        mode='determinate',
                        length=198, cursor='watch')
        self.progress.place(x='10', y='525')
        value_label = Label(self.ventana, text=self.update_progress_label(), background='#B2E351')
        value_label.place(x='50', y='550')



        self.ventana.mainloop()
    def update_progress_label(self):
        return f"progreso.... {self.progress['value']}%"




if __name__=='__main__':
    Interfaz()