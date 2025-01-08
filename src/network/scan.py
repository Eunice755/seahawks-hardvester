import nmap

def scan_reseau(ip_range="192.168.1.0/24"):
    
    #Effectue un scan réseau pour détecter les machines connectées et leurs ports ouverts.
    
    scan = nmap.PortScanner()
    scan.scan(hosts=ip_range, arguments="-sP")
    resultat = []
    for host in scan.all_hosts():
        resultat.append({
            "ip": host,
            "etat": scan[host].state(),
            "nom": scan[host].hostnames()[0]['name'] if scan[host].hostnames() else "Inconnu"
        })
    return resultat
