#fonction pour comparer deux chaines de caractères
def Comparer2Chaine(chaine1, chaine2):
    return chaine1 == chaine2

#fonction pour vérifier si une chaine contient exactement 4 caracteres
def Verfier4Caracteres(chaine):
    return len(chaine) == 4

#fonction pour vérifier si une chaine contient uniquement des chiffres
def VerifierUniquementChiffres(chaine):
    return chaine.isdigit()

#fonction principale pour verifier un code PIN
def VerifierCodePin(code_ref):
    while True : #boucle infinie jusqu'à un code valide
        code_pin = input("entrez votre code PIN :")
        if Verfier4Caracteres(code_pin) and VerifierUniquementChiffres(code_pin):
            if Comparer2Chaine(code_pin, code_ref):
                print("code PIN correct")
                break # Sort de la boucle si le code est correct
            else : 
                print ("Code PIN incorrect. Veuillez réessayer.")
        else :
            print("Code PIN invalide. assurez-vous qu'il contient exactement 4 chiffres")

#Example d'utilisation
code_reference = "1234"
VerifierCodePin(code_reference)