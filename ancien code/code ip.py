import random # import de la bibliothéque random
continuer = True
ips_attribuees = [] # Liste pour stocker les IP
def generer_ip() :
        return f"192.168.1.{random.randint(1, 254)}" #géneré une IP aléatoire

def lister_ips(): 
     if not ips_attribuees: 
          print("Aucune IP. aftribuee.")
 
     else : 
        print("IP attribuées :") 
        for ip in ips_attribuees:
            print(f"- {ip}")



while continuer :
    
    print ("=== Menu DHCP ===")
    print("1. Générer une IP aléatoire") 
    print("2. Lister les IP attribuées")
    print("3. Quitter")
    choix = input("Votre choix : ")
    if choix == "1":
        ip = generer_ip()
        ips_attribuees.append(ip)
        print(f"IP {ip} attribuée.")
    elif choix == "2":
    lister_ips()
    elif choix == "3":
    print("Au revoir !")
    continuer = False    
else:
        print("\n Choix invalide, veuillez réessayer.")