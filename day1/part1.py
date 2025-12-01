# Lecture du fichier d'entrée
def lire_fichier(chemin):
    with open(chemin, "r") as fichier:
        contenu = fichier.read()
    return contenu

# Diviser le contenu en lignes
def liste_lignes(input):
    return input.splitlines()

# Extraire la direction (Droite ou Gauche)
def extraire_direction(ligne):
    return ligne[0]

# Extraire la distance (nombre de clicks) en tant qu'entier
def extraire_distance(ligne):
    return int(ligne[1:])

# Tourner le cadran vers la gauche
def tourner_gauche(cadran_valeur, valeur):
    for i in range(valeur):
        cadran_valeur -= 1
        if cadran_valeur < 0:
            cadran_valeur = 99
    return cadran_valeur

# Tourner le cadran vers la droite
def tourner_droite(cadran_valeur, valeur):
    for i in range(valeur):
        cadran_valeur += 1
        if cadran_valeur > 99:
            cadran_valeur = 0
    return cadran_valeur
        
# Calculer la nouvelle position du cadran
def calculer_position(cadran_valeur, ligne):
    direction = extraire_direction(ligne) # "L" ou "R"
    distance = extraire_distance(ligne) # entier correspondant au nombre de clicks
    
    if direction == "L":
        cadran_valeur = tourner_gauche(cadran_valeur, distance)
    elif direction == "R":
        cadran_valeur = tourner_droite(cadran_valeur, distance)
    return cadran_valeur


if "__main__" == __name__:
    chemin_fichier = "day1/input.txt"
    input = lire_fichier(chemin_fichier)
    lignes = liste_lignes(input)

    cadran_valeur = 50
    compteur = 0

    for ligne in lignes:
        cadran_valeur = calculer_position(cadran_valeur, ligne)
        if (cadran_valeur == 0):
            compteur += 1

    print("Compteur :", compteur)