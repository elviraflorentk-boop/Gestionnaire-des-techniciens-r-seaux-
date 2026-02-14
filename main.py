import tkinter as tk 
import sqlite3


connexion=sqlite3.connect("Techniciens.db")






app=tk.Tk()
app.geometry("800x600")
app.title("Gestionnaire des techniciens")

app.mainloop()