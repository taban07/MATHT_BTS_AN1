#savoir a quel ingrediant appartient a quel pizza
#entrer un ingrédient
#regarder si l'ingredient donner est dans une pizza
def Pizzas_avec_Modif(tab_ingrediant, ingrediant ) :
    Nb_pizzas_valides = int() 
    Nb_pizzas_valides = 0
    NumPizzas = [99,99,99,99,99,99]                 
    for i in range (5) :
        for j in range (4) :
            if (tab_ingrediant[i][j] == ingrediant) :
                NumPizzas[Nb_pizzas_valides] = i
                Nb_pizzas_valides  = Nb_pizzas_valides+1
    return NumPizzas

#-------------------------------------------------

NumPizzas = ["Regina","Margherita","Romaine","Quatre fromages","Calzone"] 
ingrediant =  [["tomate","mozzarella","jambon","champignons"],
                ["tomate","mozzarella","basilic","huile d'olive"],
                ["tomate","anchois","origan","parmesan","Selles-sur-cher"],
                ["mozzarella","jambon","tomate","oeufs"],
                ["mozzarella","jambon","tomate","oeuf"]]


ingrediant_input = input ("Entrez l'ingrédient recherché: ")
liste_pizza = Pizzas_avec_Modif(ingrediant, ingrediant_input)
print (liste_pizza)
