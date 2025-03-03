# Fonction pour vérifier si un code PIN est valide (4 chiffres)
def verifier_code_pin(code):
    return len(code) == 4 and code.isdigit()

# Fonction pour comparer deux codes PIN
def comparer_code(pin1, pin2):
    return pin1 == pin2

# Fonction pour chiffrer un code PIN avec César (+2)
def chiffrer_cesar(code):
    code_crypte = ""
    for chiffre in code:
        nouveau_chiffre = (int(chiffre) + 2) % 10  # Décalage de 3
        code_crypte += str(nouveau_chiffre)
    return code_crypte

# Fonction pour déchiffrer un code PIN avec César (-2)
def dechiffrer_cesar(code):
    code_decrypte = ""
    for chiffre in code:
        nouveau_chiffre = (int(chiffre) - 2) % 10  # Décalage inverse
        code_decrypte += str(nouveau_chiffre)
    return code_decrypte

# Fonction du menu principal
def menu():
    code_reference = "1234"  # Code PIN par défaut
    code_crypte = ""  # Variable pour stocker le code chiffré

    while True:
        print("\n=== MENU ===")
        print("1. Saisir un code PIN")
        print("2. Vérifier le code PIN")
        print("3. Chiffrer le code PIN")
        print("4. Déchiffrer le code PIN")
        print("5. Quitter")

        choix = input("Choisissez une option : ")

        if choix == "1":  # Saisie du code PIN
            nouveau_code = input("Entrez un code PIN (4 chiffres) : ")
            if verifier_code_pin(nouveau_code):
                code_reference = nouveau_code
                print("✅ Code PIN enregistré.")
            else:
                print("❌ Code invalide. Il doit contenir exactement 4 chiffres.")

        elif choix == "2":  # Vérification du code PIN
            code_saisi = input("Entrez votre code PIN : ")
            if comparer_code(code_saisi, code_reference):
                print("✅ Code PIN correct.")
            else:
                print("❌ Code PIN incorrect.")

        elif choix == "3":  # Chiffrement du code PIN
            if code_reference:
                code_crypte = chiffrer_cesar(code_reference)
                print(f"🔒 Code PIN crypté : {code_crypte}")
            else:
                print("❌ Aucun code PIN à crypter.")

        elif choix == "4":  # Déchiffrement du code PIN
            if code_crypte:
                code_decrypte = dechiffrer_cesar(code_crypte)
                print(f"🔓 Code PIN déchiffré : {code_decrypte}")
            else:
                print("❌ Aucun code PIN crypté à déchiffrer.")

        elif choix == "5":  # Quitter
            print("👋 Au revoir !")
            break

        else:
            print("❌ Option invalide. Veuillez choisir une option entre 1 et 5.")

# Lancer le menu
menu()
