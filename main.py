import sqlite3
import tkinter  # import de tkinter
from tkinter import Entry

fenetre = tkinter.Tk()  # création de la fenêtre principale
fenetre.geometry("600x600")
# fenetre.iconbitmap("./home/jeanpi/Bureau/19122020/tatoum.ico")
fenetre.title("Ajout Parcelle")
fenetre['bg'] = 'white'  # couleur de fond
fenetre.resizable(width=False, height=False)


def tkquit():
    fenetre.destroy()


'''# Création de la requete  Uniquement 1 fois pour créer nom email tel ....ect conn = sqlite3.connect('iftdb') cur = 
conn.cursor() req = "CREATE TABLE fichier(id INTEGER PRIMARY KEY AUTOINCREMENT, Identité TEXT NOT NULL, Tel TEXT NOT 
NULL, Email TEXT NOT NULL)" # Exécution de la requete cur.execute(req)   # permet de communiquer avec la BDD # 
Envoyer la requete conn.commit() # Fermer la connexion conn.close '''


def sauvegarde():
    conn = sqlite3.connect('fichier.db')  # connection  à la bdd
    cur = conn.cursor()  # Créer un cursor
    global nom_prenom
    # Récupération des entrées et placement dans une variable
    contenu_nom = nom_prenom.get()
    contenu_tel = Tel.get()
    contenu_email = Email.get()
    # Insérer les données dans la BDD
    cur.execute("Insert into fichier (Identité,Tel,Email) values (?,?,?)",
                (contenu_nom, contenu_tel, contenu_email))  # Insérer les données dans la         BDD
    conn.commit()  # Engager l'opération
    conn.close()  # Fermer la connexion


# ...
zone_texte = tkinter.Label(fenetre, text="Votre Nom et Prenom")
# ...
zone_texte.pack(padx=0, pady=50)  # on ajoute la zone_texte à la fenêtre principale

nom_prenom = Entry(fenetre, width=50)
nom_prenom.pack()
nom_prenom.focus_force()  # placement du curseur dans la première entrée.
# ...
zone_texte = tkinter.Label(fenetre, text="Votre Numero de Tel")
# ...
zone_texte.pack()  # on ajoute la zone_texte à la fenêtre principale

Tel = Entry(fenetre, width=25)
Tel.pack(padx=5, pady=5)
# ...
zone_texte = tkinter.Label(text="Votre Email")
# ...
zone_texte.pack()  # on ajoute la zone_texte à la fenêtre principale

Email = Entry(fenetre, width=25)
Email.pack(padx=5, pady=5)

# Création du bouton de Sauvegarde
bouton = tkinter.Button(text="sauvegarder", command=sauvegarde)
bouton.pack()

bouton2 = tkinter.Button(fenetre, text="Quitter", command=tkquit)
bouton2.pack(padx=100, pady=100)
fenetre.mainloop()  # on affiche enfin la fenêtre principale et on attend
