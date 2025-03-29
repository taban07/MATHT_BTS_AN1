# Fonction pour afficher une image en remplaçant 1 par "■" et 0 par "□" 
def AfficheImage(image):
    for ligne in image:  # On parcourt chaque ligne
        for pixel in ligne:  # On parcourt chaque pixel de la ligne
            if pixel == 1:
                print("■", end="")
            else:
                print("□", end="")
        print() 

# Fonction pour vérifier si l'image est symétrique verticalement
def VerifSymetrieVert(image):
    for ligne in image: 
        if ligne != ligne[::-1]:
            return False
    return True  

# Fonction pour créer le négatif d'une image (inverser 0 et 1)
def Negatif(image):
    nouveau = [] 
    for ligne in image
        nouvelle_ligne = []
        for pixel in ligne:
            if pixel == 1:
                nouvelle_ligne.append(0)  
            else:
                nouvelle_ligne.append(1)
        nouveau.append(nouvelle_ligne)
    return nouveau

# Fonction pour superposer deux images (fait un "OU")
def Superpose(image1, image2):
    nouveau = []
    for i in range(len(image1)):
        nouvelle_ligne = []
        for j in range(len(image1[0])):
            if image1[i][j] == 1 or image2[i][j] == 1:
                nouvelle_ligne.append(1)
            else:
                nouvelle_ligne.append(0)
        nouveau.append(nouvelle_ligne)  
    return nouveau

# Définition d'une image en noir et blanc
image = [
    [1,0,0,0,0,0,0,0,0,1],
    [0,1,1,1,1,1,1,1,1,0],
    [0,1,0,1,1,1,1,0,1,0],
    [0,1,0,1,1,1,1,0,1,0],
    [0,1,1,1,1,1,1,1,1,0],
    [0,1,0,1,1,1,1,0,1,0],
    [0,1,0,0,0,0,0,0,1,0],
    [0,1,1,1,1,1,1,1,1,0],
    [1,0,0,0,0,0,0,0,0,1]
]

print("Image originale :")
AfficheImage(image)

# Vérification de la symétrie verticale
if VerifSymetrieVert(image)
    print("\nL'image est symétrique verticalement.")
else:
    print("\nL'image n'est pas symétrique verticalement.")

# Affichage du négatif de l'image
print("\nNégatif de l'image :")
image_negatif = Negatif(image)
AfficheImage(image_negatif)

# Exemple d'une deuxième image pour la superposition
image2 = [
    [0,1,1,1,1,1,1,1,1,0],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,1,1,1,0,1],
    [1,0,1,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,1,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [0,1,1,1,1,1,1,1,1,0]
]

# Affichage de la superposition des deux images
print("\nSuperposition des deux images :")
image_superposee = Superpose(image, image2)
AfficheImage()
