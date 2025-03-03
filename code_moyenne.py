# Fonction pour calculer la moyenne pondérée
def calculer_moyenne_ponderee(notes, coefficients):
    return sum(n * c for n, c in zip(notes, coefficients)) / sum(coefficients) if coefficients else 0

# Fonction pour entrer les notes d'une matière
def entrer_notes(matiere):
    try:
        return [float(n) for n in input(f"Notes pour {matiere} (séparées par des espaces) : ").split() if 0 <= float(n) <= 20]
    except ValueError:
        print("Entrée invalide. Réessayez.")
        return entrer_notes(matiere)

# Matières et coefficients
matieres = {"Mathématiques": 12, "SISR": 12, "Technologie": 6}
notes, coefficients = [], []

# Saisie des notes
for matiere, coef in matieres.items():
    entrees = entrer_notes(matiere)
    notes.extend(entrees)
    coefficients.extend([coef] * len(entrees))

# Affichage de la moyenne
print(f"Moyenne pondérée : {calculer_moyenne_ponderee(notes, coefficients):.2f}" if notes else "Aucune note saisie.")
