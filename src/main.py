from gui.dashboard import afficher_tableau_de_bord
from network.scan import scan_reseau
from update.update import verifier_mise_a_jour

def main():
    # Vérification des mises à jour
    verifier_mise_a_jour()
    print("Mise à jour en cours...")

    # Effectuer un scan réseau
    resultat_scan = scan_reseau("192.168.1.0/24")

    # Afficher les résultats dans le tableau de bord
    afficher_tableau_de_bord(resultat_scan)  # Appel pour afficher l'interface graphique

if __name__ == "__main__":
    main()

    
    
