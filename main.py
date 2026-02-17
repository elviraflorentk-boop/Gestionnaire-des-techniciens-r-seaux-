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

frame1=tk.LabelFrame(app,text="Informations Techniciens",width=236,height=17,bg="white",font="Anton 11",fg="black")
frame1.place(x=7,y=3)

label1=tk.Label(app,text="Nom",font="Anton 11",bg="white")
label1.place(x=7,y=30)

zone1=tk.Entry(app,bg="white")
zone1.place(x=120,y=31)


label2=tk.Label(app,text="Prénom",font="Anton 11",bg="white")
label2.place(x=7,y=65)

#Prof ! Ceci je le note juste pour signaler certaines modifications au code, plus j'avance et je rentre parfois en arrière pour modifier certains détails comme la couleur, ou la position de la zone1 par exemple

zone2=tk.Entry(app,bg="white")
zone2.place(x=120,y=67)

label3=tk.Label(app,text="Age",font="Anton 11",bg="white")
label3.place(x=7,y=101)

zone3=tk.Entry(app,bg="white")
zone3.place(x=120,y=105)

label4=tk.Label(app,text="Sexe",font="Anton 11",bg="white")
label4.place(x=7,y=138)

combo=ttk.Combobox(app,values=["Homme","Femme"])
combo.set("Sélectionner")
combo.place(x=110,y=138)


label5=tk.Label(app,text="Spécialité",font="Anton 11",bg="white")
label5.place(x=7,y=174)

zone5=tk.Entry(app,bg="white")
zone5.place(x=120,y=175)

label6=tk.Label(app,text="Niveau d'étude",font="Anton 11",bg="white")
label6.place(x=7,y=210)

zone6=tk.Entry(app,bg="white")
zone6.place(x=120,y=212)

label7=tk.Label(app,text="Expérience",font="Anton 11",bg="white")
label7.place(x=7,y=247)

#Je fais ce commentaire juste pour dire que j'ai apporté des modifications pour raison de beauté

zone7=tk.Entry(app,bg="white")
zone7.place(x=120,y=250)

label8=tk.Label(app,text="Domaine",font="Anton 11",bg="white")
label8.place(x=7,y=285)

check_var1=tk.IntVar()
check_var2=tk.IntVar()
check_var3=tk.IntVar()
check_var4=tk.IntVar()

checkbutton=tk.Checkbutton(app,text="Entreprise",variable=check_var1)
checkbutton.place(x=97,y=285)

checkbutton=tk.Checkbutton(app,text="Banque",variable=check_var2)
checkbutton.place(x=200,y=285)

checkbutton=tk.Checkbutton(app,text="Télécom",variable=check_var3)
checkbutton.place(x=200,y=310)

checkbutton=tk.Checkbutton(app,text="Université",variable=check_var4)
checkbutton.place(x=97,y=310)

label9=tk.Label(app,text="Grade",font="Anton 11",bg="white")
label9.place(x=7,y=335)

zone9=tk.Entry(app,bg="white")
zone9.place(x=120,y=338)

label10=tk.Label(app,text="Téléphone",font="Anton 11",bg="white")
label10.place(x=7,y=372)

zone10=tk.Entry(app,bg="white")
zone10.place(x=120,y=375)

label11=tk.Label(app,text="Adresse mail",font="Anton 11",bg="white")
label11.place(x=7,y=410)

zone11=tk.Entry(app,bg="white")
zone11.place(x=120,y=413)

label12=tk.Label(app,text="Ville",font="Anton 11",bg="white")
label12.place(x=7,y=445)

combo=ttk.Combobox(app,values=["Kinshsa","Matadi","Boma","Moanda","Kanga","Bukavu","Kindu","Goma","Beni","Kisangani"])
combo.set("Sélectionner")
combo.place(x=110,y=445)

buton1=tk.Button(app,text="Ajouter",width=15)
buton1.place(x=7,y=490)

buton2=tk.Button(app,text="Modifier",width=15)
buton2.place(x=150,y=490)

app.mainloop()