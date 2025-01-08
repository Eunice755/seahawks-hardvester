import tkinter as tk
from tkinter import ttk

def afficher_tableau_de_bord(data):
    
    #Affiche les résultats du scan réseau dans un tableau de bord.
    
    fenetre = tk.Tk()
    fenetre.title("Tableau de bord Seahawks Harvester")
    
    # Titre
    label_titre = tk.Label(fenetre, text="Résultats du Scan Réseau", font=("Arial", 16))
    label_titre.pack(pady=10)

    # Tableau
    colonnes = ("Adresse IP", "Nom", "État")
    tableau = ttk.Treeview(fenetre, columns=colonnes, show="headings")
    tableau.heading("Adresse IP", text="Adresse IP")
    tableau.heading("Nom", text="Nom")
    tableau.heading("État", text="État")
    tableau.pack()

    # Ajouter des données
    for machine in data:
        tableau.insert("", "end", values=(machine["ip"], machine["nom"], machine["etat"]))

    # Bouton Quitter
    bouton_quitter = tk.Button(fenetre, text="Quitter", command=fenetre.destroy)
    bouton_quitter.pack(pady=10)

    fenetre.mainloop()
