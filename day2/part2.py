def motif_repete(number):
    nb_str = str(number) # Correspond au nombre sous forme de chaîne de caractères
    taille = len(nb_str) # Longueur de cette chaîne

    for motif_len in range(1, taille + 1):
        if taille % motif_len == 0: # Le motif doit pouvoir se répéter un nombre entier de fois
            motif = nb_str[:motif_len] # On extrait le motif
            repetitions = taille // motif_len # Nombre de répétitions nécessaires 
            construit = motif * repetitions # On reconstruit le nombre à partir du motif
            if construit == nb_str and repetitions >= 2: # Correspond et au moins 2 répétitions
                return True
    return False

def check_invalid(min, max, invalidNumbers):
    for nombre in range(min, max + 1):
        if motif_repete(nombre) == True:
            invalidNumbers.append(nombre)
            print(f"{min}-{max} : Nombres invalide trouvé = {nombre}")
    return invalidNumbers

if __name__ == "__main__":
    with open("day2/input.txt", "r") as file:
        lignes = file.read()
        intervales = lignes.split(",")
        count = 0
        invalidNumbers = []

        for intervale in intervales:
            min_str, max_str = intervale.split('-')
            min, max = int(min_str), int(max_str)
            invalidNumbers = check_invalid(min, max, invalidNumbers)
        print(sum(invalidNumbers))