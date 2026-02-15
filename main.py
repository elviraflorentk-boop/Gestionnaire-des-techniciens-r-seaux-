import tkinter as tk 
import sqlite3


connexion=sqlite3.connect("Techniciens.db")

curseur=connexion.cursor()

curseur.execute("""
CREATE TABLE IF NOT EXISTS techniciens (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    prenom TEXT NOT NULL,
    age INTEGER,
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

frame1=tk.LabelFrame(app,text="Informations Techniciens",width=500,height=380,bg="gray",fg="black",font="Anton 10")
frame1.place(x=10,y=15)

label1=tk.Label(frame1,text="Nom",font="Anton 18",bg="gray")
label1.place(x=3,y=7)

zone1=tk.Entry(frame1,bg="white")
zone1.place(x=110,y=14)


label2=tk.Label(frame1,text="Prénom",font="Anton 18",bg="gray")
label2.place(x=3,y=43)

#Prof ! Ceci je le note juste pour signaler certaines modifications au code, plus j'avance et je rentre parfois en arrière pour modifier certains détails comme la couleur, ou la position de la zone1 par exemple

app.mainloop()