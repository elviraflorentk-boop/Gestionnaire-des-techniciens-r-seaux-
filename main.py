import tkinter as tk 
import sqlite3
from tkinter import ttk 
from tkinter import messagebox

connexion = sqlite3.connect("techniciens.db")
curseur = connexion.cursor()

curseur.execute("""
CREATE TABLE IF NOT EXISTS techniciens (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    prenom TEXT NOT NULL,
    sexe TEXT CHECK(sexe IN ('H','F')) NOT NULL,
    age INTEGER,
    specialite TEXT,
    niveau_etude TEXT,
    experience INTEGER,
    domaine TEXT,
    grade TEXT,
    telephone TEXT NOT NULL,
    email TEXT,
    ville TEXT,
    date_enregistrement TEXT
)
""")

connexion.commit()
connexion.close()


app=tk.Tk()
app.geometry("800x600")
app.title("Gestionnaire des techniciens")

def ajouter_technicien():
    nom=zone1.get()
    prenom=zone2.get()
    if not zone1.get() or not zone2.get() :
        messagebox.showerror("Erreur", "Nom et Prénom obligatoires")
        return
        

frame1=tk.LabelFrame(app,text="Informations Techniciens",width=236,height=17,bg="white",font="Anton 11",fg="black")
frame1.place(x=7,y=3)

label1=tk.Label(app,text="Nom",font="Anton 11")
label1.place(x=7,y=30)

zone1=tk.Entry(app,bg="white")
zone1.place(x=120,y=31)


label2=tk.Label(app,text="Prénom",font="Anton 11")
label2.place(x=7,y=65)

#Prof ! Ceci je le note juste pour signaler certaines modifications au code, plus j'avance et je rentre parfois en arrière pour modifier certains détails comme la couleur, ou la position de la zone1 par exemple

zone2=tk.Entry(app,bg="white")
zone2.place(x=120,y=67)

label3=tk.Label(app,text="Âge",font="Anton 11")
label3.place(x=7,y=101)

zone3=tk.Entry(app,bg="white")
zone3.place(x=120,y=105)

label4=tk.Label(app,text="Sexe",font="Anton 11")
label4.place(x=7,y=138)

combo=ttk.Combobox(app,values=["Homme","Femme"])
combo.set("Sélectionner")
combo.place(x=110,y=138)


label5=tk.Label(app,text="Spécialité",font="Anton 11")
label5.place(x=7,y=174)

zone5=tk.Entry(app,bg="white")
zone5.place(x=120,y=175)

label6=tk.Label(app,text="Niveau d'étude",font="Anton 11")
label6.place(x=7,y=210)

zone6=tk.Entry(app,bg="white")
zone6.place(x=120,y=212)

label7=tk.Label(app,text="Expérience",font="Anton 11")
label7.place(x=7,y=247)

#Je fais ce commentaire juste pour dire que j'ai apporté des modifications pour raison de beauté

zone7=tk.Entry(app,bg="white")
zone7.place(x=120,y=250)

label8=tk.Label(app,text="Domaine",font="Anton 11")
label8.place(x=7,y=287)

zone8=tk.Entry(app,bg="white")
zone8.place(x=120,y=290)


label9=tk.Label(app,text="Grade",font="Anton 11")
label9.place(x=7,y=330)

check_var1=tk.IntVar()
check_var2=tk.IntVar()
check_var3=tk.IntVar()
check_var4=tk.IntVar()

checkbutton=tk.Checkbutton(app,text="Junior",variable=check_var1)
checkbutton.place(x=97,y=320)

checkbutton=tk.Checkbutton(app,text="Intermédiaire",variable=check_var2)
checkbutton.place(x=200,y=320)

checkbutton=tk.Checkbutton(app,text="Sénior",variable=check_var3)
checkbutton.place(x=200,y=340)

checkbutton=tk.Checkbutton(app,text="Chef d'équipe",variable=check_var4)
checkbutton.place(x=97,y=340)



label10=tk.Label(app,text="Téléphone",font="Anton 11")
label10.place(x=7,y=372)

zone10=tk.Entry(app,bg="white")
zone10.place(x=120,y=375)

label11=tk.Label(app,text="Adresse mail",font="Anton 11")
label11.place(x=7,y=410)

zone11=tk.Entry(app,bg="white")
zone11.place(x=120,y=413)

label12=tk.Label(app,text="Ville",font="Anton 11")
label12.place(x=7,y=445)

combo=ttk.Combobox(app,values=["Kinshsa","Matadi","Boma","Moanda","Kanga","Bukavu","Kindu","Goma","Beni","Kisangani"])
combo.set("Sélectionner")
combo.place(x=110,y=445)

buton1=tk.Button(app,text="Ajouter",width=15,command=ajouter_technicien)
buton1.place(x=7,y=490)

buton2=tk.Button(app,text="Modifier",width=15)
buton2.place(x=150,y=490)

buton3=tk.Button(app,text="Supprimer",width=15,)
buton3.place(x=7,y=530)

buton4=tk.Button(app,text="Afficher",width=15,)
buton4.place(x=150,y=530)

buton5=tk.Button(app,text="Rechercher",width=35)
buton5.place(x=7,y=576)

#frame2=tk.LabelFrame(app,bg="white",height=600,width=900)
#frame2.place(x=300,y=3)

colonnes=("ID","Nom","Prénom","Sexe","Âge","Spécialié","Niveau d'étude","Expérience","Domaine","Grade","Téléphone","Email","Ville")
liste=ttk.Treeview(app,columns=colonnes,show="headings",height=29)
for col in colonnes:
    liste.heading(col, text=col)
    liste.column(col, width=73)
liste.grid(row=0, column=3, rowspan=10, padx=300,pady=3)
liste.bind("<<TreeviewSelect>>")





app.mainloop()