from tkinter import * #importar libreria tkinter
from tkinter import ttk

raiz=Tk()
raiz.geometry("600x450")

notebook=ttk.Notebook(raiz)
notebook.pack(expand=True, fill=BOTH)
style=ttk.Style()
style.theme_create("MyStyle",parent="alt", settings={
    "TNotebook.Tab":{
        "configure":{"background":"sky blue",
                    "foreground": "black" 
                    },
        "map":{"blackground":[("selected","white")]
            
        }
    }
})
style.theme_use("MyStyle")

tabla1=ttk.Frame(notebook)
tabla2=ttk.Frame(notebook)
tabla3=ttk.Frame(notebook)
tabla4=ttk.Frame(notebook)
tabla5=ttk.Frame(notebook)
tabla6=ttk.Frame(notebook)

filavacia=ttk.Frame(tabla1,padding="10 15 10 15", width=600, height=10, relief="groove")
filavacia.grid(column=0, row=1, sticky=(W,N,E,S))

tabs=ttk.Frame(tabla1,padding="10 15 10 15", width=600, height=10, relief="groove")
tabs.grid(column=0, row=2, sticky=(W,N,E,S))

card=ttk.Frame(tabla1,padding="10 15 10 15", width=600, height=10, relief="groove")
card.grid(column=0, row=3, sticky=(W,N,E,S))
room=ttk.Frame(tabla1,padding="10 15 10 15", width=600, height=10, relief="groove")
room.grid(column=0, row=4, sticky=(W,N,E,S))


ultimobotton=ttk.Frame(tabla1,padding="10 15 10 15", width=600, height=10, relief="groove")
ultimobotton.grid(column=0, row=5,sticky=(W,N,E,S))

notebook.add(tabla1,text="        Add                 ")
notebook.add(tabla2,text="               Delete                 ")
notebook.add(tabla3,text="             Search                       ")
notebook.add(tabla5,text="           Services               ")
notebook.add(tabla6, text="         Help             ")

ttk.Label(filavacia, text="")


nombreEntry=ttk.Entry(tabs)
nombreEntry.grid(column=1, row=0, columnspan=3, padx=10, pady=20)

apellidoEntry=ttk.Entry(tabs)
apellidoEntry.grid(column=5, row=0, columnspan=6, padx=10)

diaEntry=ttk.Entry(tabs, width=3)
diaEntry.grid(column=1,row=1, padx=4)

mesEntry=ttk.Entry(tabs, width=3)
mesEntry.grid(column=2, row=1, padx=4)

añoEntry=ttk.Entry(tabs, width=5)
añoEntry.grid(column=3,row=1, padx=4)

ciudadEntry=ttk.Entry(tabs)
ciudadEntry.grid(column=5,row=1,padx=10)

ttk.Label(tabs, text="First Name").grid(column=0, row=0, pady=7)
ttk.Label(tabs, text="Last Name").grid(column=4, row=0, pady=7)
ttk.Label(tabs, text="Birth Date").grid(column=0, row=1, pady=7)
ttk.Label(tabs, text="Country").grid(column=4, row=1, pady=7)

cardEntry=ttk.Entry(card)
cardEntry.grid(column=1, row=0, pady=15, sticky=(N))


ttk.Label(card, text="Credit card(if any)").grid(column=0, row=0)
ttk.Label(card, text="Credit card type(if any):").grid(column=0, row=1)

visa=ttk.Radiobutton(card, text="Visa")
visa.grid(column=1,row=1)

masterCard=ttk.Radiobutton(card, text="MasterCard")
masterCard.grid(column=2,row=1)

ttk.Label(room, text="Room type").grid(column=0,row=0)
ttk.Label(room,text="Total Staying Time (days)").grid(column=2, row=0, padx=20)

normal=Radiobutton(room,text="Normal")
normal.grid(column=1, row=0, padx=15)
familiar=ttk.Radiobutton(room, text="Familiar")
familiar.grid(column=1, row=1)
especial=ttk.Radiobutton(room,text="Especial")
especial.grid(column=1, row=2)

diaEntry=ttk.Entry(room, width=6)
diaEntry.grid(column=3,row=0)

boton= ttk.Button(ultimobotton, text="Submit").grid(column=0, row=0, padx=250)

raiz.mainloop()


