import random # import de la bibliothéque random
continuer = True
ips_attribuees = [] # Liste pour stocker les IP
machines = {}

def generer_ip() :
        return f"192.168.1.{random.randint(1, 254)}" #géneré une IP aléatoire

def lister_ips(): 
     if not machines : 
          print("Aucune machine n'a d' IP aftribuée.")
 
     else : 
        print("Machine et leurs IP :") 
        for machine , ip in machines.items() :
            print(f"- {machine} : {ip}")



while continuer :
    
    print ("\n === Menu DHCP ===")
    print("\n 1. Générer une IP aléatoire") 
    print("\n 2. Lister les IP attribuées")
    print("\n 3. Quitter")
    choix = input("\n Votre choix : ")
    
    if choix == "1":
        nom_machine = input("\n Nom de la machine : ")
        ipa = generer_ip()
        machines[nom_machine] = ipa
        print(f"IP {ipa} attribuée à nom {nom_machine}. ")
    
    elif choix == "2":
        lister_ips()
    
    elif choix == "3":
        print("\n Au revoir !")
        continuer = False    
    
    else:
        print("\n Choix invalide, veuillez réessayer.")