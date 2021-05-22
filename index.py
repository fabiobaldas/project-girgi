from tkinter import *
import os
from tkinter import messagebox

c=os.path.dirname(__file__)
nomeArquivo=c+"\\nomes.txt"

def gravarDados():
    arquivo=open(nomeArquivo,"a")
    arquivo.write("\nNome: %s" % lnome.get())
    arquivo.write("\nTelefone: %s" % ltelefone.get())
    arquivo.write("\nEmail: %s" % lemail.get())
    arquivo.write("\n")
    messagebox.showinfo("CEU Engenharia", "Finalizado!")
    
app=Tk()
app.title("CEU Engenharia")
app.geometry("500x300")
app.configure(background="#dde")

nome=Label(app,text="Nome", background="#dde",foreground="#009",anchor=W).place(x=10,y=10,width=100,height=20)
lnome=Entry(app)
lnome.place(x=10,y=30,width=200,height=20)

telefone=Label(app,text="Telefone", background="#dde",foreground="#009",anchor=W).place(x=10,y=60,width=100,height=20)
ltelefone=Entry(app)
ltelefone.place(x=10,y=80,width=100,height=20)

email=Label(app,text="Email", background="#dde",foreground="#009",anchor=W).place(x=10,y=110,width=300,height=20)
lemail=Entry(app)
lemail.place(x=10,y=130,width=200,height=20)

btn_enviar=Button(app, text="Enviar",command=gravarDados)
btn_enviar.place(x=10, y=270, width=100, height=20)


app.mainloop()