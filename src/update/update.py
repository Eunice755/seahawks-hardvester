import os
import subprocess
import requests
import json

def verifier_mise_a_jour():
    
    #Vérifie si une mise à jour est disponible sur la branche principale du dépôt GitHub.
    
    # Configuration
    url = "https://github.com/Eunice755/seahawks-hardvester/tree/main"
    
    

    try:
        # Requête à l'API GitHub pour vérifier les mise à jouur
        response = requests.get(url)
        response.raise_for_status() #Declenche une ereur pour les codes HTTP 4xx/5xx
        print("Mise à jour vérifiée avec succès !")


    except requests.exceptions.HTTPError as err:
        print(f"Erreur lors de la vérification de mise à jour : {err}")
        return False


def appliquer_mise_a_jour():
    
    #Applique les changements depuis le dépôt GitHub.
    
    try:
        print("Téléchargement des mises à jour...")
        subprocess.run(["git", "pull"], check=True)
        print("Mise à jour appliquée avec succès.")
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'application de la mise à jour : {e}")


if __name__ == "__main__":
    # Vérifier s'il y a une mise à jour
    if verifier_mise_a_jour():
        appliquer_mise_a_jour()
