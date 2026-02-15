import tkinter as tk 
import sqlite3
from tkinter import ttk 


connexion=sqlite3.connect("Techniciens.db")

curseur=connexion.cursor()

curseur.execute("""
CREATE TABLE IF NOT EXISTS techniciens (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    prenom TEXT NOT NULL,
    age INTEGER,
    sexe TEXT CHECK(sexe IN ('HOMME','FEMME')) NOT NULL,
    specialite TEXT,
    niveau_etude TEXT,
    experience INTEGER,
    domaine TEXT,
    grade TEXT,
    telephone TEXT NOT NULL,
    email TEXT,
    ville TEXT
)
""")

connexion.commit()

connexion.close()

app=tk.Tk()
app.geometry("800x600")
app.title("Gestionnaire des techniciens")

frame1=tk.LabelFrame(app,text="Informations Techniciens",width=500,height=380,bg="white",fg="black",font="Anton 10")
frame1.place(x=10,y=15)

label1=tk.Label(frame1,text="Nom",font="Anton 11",bg="white")
label1.place(x=3,y=7)

zone1=tk.Entry(frame1,bg="white")
zone1.place(x=78,y=12)


label2=tk.Label(frame1,text="Prénom",font="Anton 11",bg="white")
label2.place(x=3,y=43)

#Prof ! Ceci je le note juste pour signaler certaines modifications au code, plus j'avance et je rentre parfois en arrière pour modifier certains détails comme la couleur, ou la position de la zone1 par exemple

zone2=tk.Entry(frame1,bg="white")
zone2.place(x=78,y=46)

label3=tk.Label(frame1,text="Age",font="Anton 11",bg="white")
label3.place(x=3,y=77)

zone3=tk.Entry(frame1,bg="white")
zone3.place(x=78,y=82)

label4=tk.Label(frame1,text="Sexe",font="Anton 11",bg="white")
label4.place(x=3,y=109)

combo=ttk.Combobox(frame1,values=["Homme","Femme"])
combo.set("Sélectionner")
combo.place(x=70,y=110)


label5=tk.Label(frame1,text="Spécialité",font="Anton 11",bg="white")
label5.place(x=3,y=148)

zone5=tk.Entry(frame1,bg="white")
zone5.place(x=78,y=151)

label6=tk.Label(frame1,text="Niveau d'étude",font="Anton 11",bg="white")
label6.place(x=3,y=182)

zone6=tk.Entry(frame1,bg="white")
zone6.place(x=120,y=184)


app.mainloop()