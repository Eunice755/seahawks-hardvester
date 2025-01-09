import os
import subprocess
import requests
import json

def verifier_mise_a_jour():
    
    #Vérifie si une mise à jour est disponible sur la branche principale du dépôt GitHub.
    
    # Configuration
    github_repo = "https://github.com/Eunice755/seahawks-hardvester.git"
    branche = "main"

    try:
        # Requête à l'API GitHub pour récupérer la dernière version du dépôt
        response = requests.get(f"{github_repo}/branches/{branche}")
        response.raise_for_status()

        # Lire le dernier commit SHA
        remote_commit = response.json()["commit"]["sha"]

        # Lire le dernier commit SHA local
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        local_commit = result.stdout.strip()

        # Comparer les commits
        if remote_commit != local_commit:
            print("Une mise à jour est disponible.")
            return True
        else:
            print("L'application est déjà à jour.")
            return False

    except Exception as e:
        print(f"Erreur lors de la vérification de mise à jour : {e}")
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
