import tkinter
from tkinter import *
from webbrowser import get
# ventana

ventana = tkinter.Tk()
ventana.geometry("700x300")
ventana.title("Controlador de honorarios regulados (Ley 27.423)")


# etiquetas

Capital = tkinter.Label(ventana,text="Capital de condena (En UMA)")
Capital.place(x=10,y=20)

Capital_ingresado = StringVar
Capital_ingresado = tkinter.Entry (ventana)
Capital_ingresado.place(x=170,y=20)



Honorarios = tkinter.Label(ventana,text="Honorarios regulados")
Honorarios.place(x=10,y=40)

Honorarios_regulados = tkinter.Entry(ventana)
Honorarios_regulados.place(x=170,y=40)


# funciones



# funcion máximo

def calcular():
        
    if float(Capital_ingresado.get()) <= 15:
        Honorario_maximo = round((float(Capital_ingresado.get())*0.33),2)
        Honorario_minimo = round((float(Capital_ingresado.get())*0.22),2)
        Etiqueta = tkinter.Label(ventana,text="El honorario no debe ser mayor a: "+str(Honorario_maximo)+ " , ni menor de "+str(Honorario_minimo))
        Etiqueta.place(x=10,y=120) 
        boton_control.config(state="disabled")
        if float(Honorarios_regulados.get()) > Honorario_maximo:
            Etiqueta = tkinter.Label(ventana,text="APELAR HONORARIOS POR ALTOS")
            Etiqueta.place(x=10,y=140)
            
     
    elif float(Capital_ingresado.get()) >= 16 and float(Capital_ingresado.get()) <= 45:
        Honorario_maximo = round(((float(Capital_ingresado.get())-15) * 0.26 + 15 * 0.33),2)
        Honorario_minimo = round(((float(Capital_ingresado.get())-15) * 0.20 + 15 * 0.33),2)
        Etiqueta = tkinter.Label(ventana,text="El honorario no debe ser mayor a: "+str(Honorario_maximo)+" , ni menor de "+str(Honorario_minimo))
        Etiqueta.place(x=10,y=120)
        boton_control.config(state="disabled")
        if float(Honorarios_regulados.get()) > Honorario_maximo:
            Etiqueta = tkinter.Label(ventana,text="APELAR HONORARIOS POR ALTOS")
            Etiqueta.place(x=10,y=140)
        
    elif float(Capital_ingresado.get()) >= 46 and float(Capital_ingresado.get()) <= 90:
        Honorario_maximo = round(((float(Capital_ingresado.get())-45) * 0.24 + 45 * 0.26),2)
        Honorario_minimo = round(((float(Capital_ingresado.get())-45) * 0.18 + 45 * 0.26),2)
        Etiqueta = tkinter.Label(ventana,text="El honorario no debe ser mayor a: "+str(Honorario_maximo)+ " , ni menor de "+str(Honorario_minimo))
        Etiqueta.place(x=10,y=120)
        boton_control.config(state="disabled")
        if float(Honorarios_regulados.get()) > Honorario_maximo:
            Etiqueta = tkinter.Label(ventana,text="APELAR HONORARIOS POR ALTOS")
            Etiqueta.place(x=10,y=140)
        
    elif float(Capital_ingresado.get()) >= 91 and float(Capital_ingresado.get()) <= 150:
        Honorario_maximo = round(((float(Capital_ingresado.get())-90) * 0.22 + 90 * 0.24),2)
        Honorario_minimo = round(((float(Capital_ingresado.get())-90) * 0.17 + 90 * 0.24),2)
        Etiqueta = tkinter.Label(ventana,text="El honorario no debe ser mayor a: "+str(Honorario_maximo)+ " , ni menor de "+str(Honorario_minimo))
        Etiqueta.place(x=10,y=120)
        boton_control.config(state="disabled")
        if float(Honorarios_regulados.get()) > Honorario_maximo:
            Etiqueta = tkinter.Label(ventana,text="APELAR HONORARIOS POR ALTOS")
            Etiqueta.place(x=10,y=140)
        
    elif float(Capital_ingresado.get()) >= 151 and float(Capital_ingresado.get()) <= 450:
        Honorario_maximo = round(((float(Capital_ingresado.get())-150) * 0.20 + 150 * 0.22),2)
        Honorario_minimo = round(((float(Capital_ingresado.get())-150) * 0.15 + 150 * 0.22),2)
        Etiqueta = tkinter.Label(ventana,text="El honorario no debe ser mayor a: "+str(Honorario_maximo)+ " , ni menor de "+str(Honorario_minimo))
        Etiqueta.place(x=10,y=120)
        boton_control.config(state="disabled")
        if float(Honorarios_regulados.get()) > Honorario_maximo:
            Etiqueta = tkinter.Label(ventana,text="APELAR HONORARIOS POR ALTOS")
            Etiqueta.place(x=10,y=140)
        
    elif float(Capital_ingresado.get()) >= 451 and float(Capital_ingresado.get()) <= 750:
        Honorario_maximo = round(((float(Capital_ingresado.get())-450) * 0.17 + 450 * 0.20),2)
        Honorario_minimo = round(((float(Capital_ingresado.get())-450) * 0.13 + 450 * 0.20),2)
        Etiqueta = tkinter.Label(ventana,text="El honorario no debe ser mayor a: "+str(Honorario_maximo)+ " , ni menor de "+str(Honorario_minimo))
        Etiqueta.place(x=10,y=120)
        boton_control.config(state="disabled")
        if float(Honorarios_regulados.get()) > Honorario_maximo:
            Etiqueta = tkinter.Label(ventana,text="APELAR HONORARIOS POR ALTOS")
            Etiqueta.place(x=10,y=140)
        
    else: 
        Honorario_maximo = round(((float(Capital_ingresado.get())-750) * 0.15 + 750 * 0.17),2)
        Honorario_minimo = round(((float(Capital_ingresado.get())-750) * 0.12 + 750 * 0.17),2)
        Etiqueta = tkinter.Label(ventana,text="El honorario no debe ser mayor a: "+str(Honorario_maximo)+ " , ni menor de "+str(Honorario_minimo))
        Etiqueta.place(x=10,y=120)
        boton_control.config(state="disabled")
        if float(Honorarios_regulados.get()) > Honorario_maximo:
            Etiqueta = tkinter.Label(ventana,text="APELAR HONORARIOS POR ALTOS")
            Etiqueta.place(x=10,y=140)
     
def borrar():
    boton_control.config(state="normal")
    Capital_ingresado.delete(0,1000)
    Honorarios_regulados.delete(0,1000)
    ventana.winfo_children()[6].destroy()
    ventana.winfo_children()[7].destroy()
     
       


# botones

boton_control = tkinter.Button(ventana,text="Controlar")
boton_control.configure(command=calcular)
boton_control.place(x=230,y=80)


boton_borrar = tkinter.Button(ventana,text="Borrar")
boton_borrar.configure(command=borrar)
boton_borrar.place(x=170,y=80)




ventana.mainloop()
