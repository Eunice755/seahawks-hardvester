from gui.dashboard import afficher_tableau_de_bord
from network.scan import scan_reseau
from update.update import mettre_a_jour_application

def main():
    # Vérifier les mises à jour
    mettre_a_jour_application()
    
    # Effectuer un scan réseau
    resultat_scan = scan_reseau("192.168.1.0/24")
    
    # Afficher les résultats dans le tableau de bord
    afficher_tableau_de_bord(resultat_scan)

if __name__ == "__main__":
    main()
