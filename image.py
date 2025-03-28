#fonction pour afficher l'image et remplacer le 1 et 0 par X ou 0
def AfficheImage (image) :
    for ligne in image :#parcour ligne dans l'image
        for pixel in ligne :#parcour des pixel de chaque ligne
            if pixel == 1 :
                print ("■",end = "")
            elif pixel == 0 :
                print ("□" , end = "")
        print()
image = [[1,0,0,0,0,0,0,0,0,1],
        [0,1,1,1,1,1,1,1,1,0],
        [0,1,0,1,1,1,1,0,1,0],
        [0,1,0,1,1,1,1,0,1,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,1,0,1,1,1,1,0,1,0],
        [0,1,0,0,0,0,0,0,1,0],
        [0,1,1,1,1,1,1,1,1,0],
        [1,0,0,0,0,0,0,0,0,1],]

AfficheImage(image)# appel de la fontion

def VerifSymetrieVert ()
