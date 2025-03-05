# Fonction pour vérifier si un ingrédient est dans une pizza
def ingredient_dans_pizza(pizza, ingrediant):
    return ingrediant in pizza

#savoir a quel ingrediant appartient a quel pizza
#entrer un ingrédient
#regarder si l'ingredient donner est dans une pizza
def Pizzas_avec_Modif(tab_ingrediant, ingrediant):
    Nb_pizzas_valides = 0
    NumPizzas_valides = [99, 99, 99, 99, 99]
    for i in range(5):
        for j in range (4) :
            if (tab_ingrediant[i][j] == ingrediant) :
                NumPizzas_valides[Nb_pizzas_valides] = NumPizzas[i]
                Nb_pizzas_valides +1 
    return NumPizzas_valides

#-------------------------------------------------

NumPizzas = ["Regina", "Margherita", "Romaine", "Quatre fromages", "Calzone"]
ingrediant = [["tomate", "mozzarella", "jambon", "champignons"],
    ["tomate", "mozzarella", "basilic", "huile d'olive"],
    ["tomate", "anchois", "origan", "parmesan", "Selles-sur-cher"],
    ["mozzarella", "jambon", "tomate", "oeufs"],
    ["mozzarella", "jambon", "tomate", "oeuf"]]

ingrediant_input = input("Entrez l'ingrédient recherché: ")
liste_pizza = Pizzas_avec_Modif(ingrediant, ingrediant_input)
print(*[pizza for pizza in liste_pizza if pizza != 99])
