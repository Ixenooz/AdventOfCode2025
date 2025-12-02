def count_invalid(min, max, count, invalidNumbers):
    for nombre in range(min, max + 1):
        if (len(str(nombre)) % 2) == 0:
            left = str(nombre)[:len(str(nombre))//2]
            right = str(nombre)[len(str(nombre))//2:]
            if left == right:
                count += 1
                invalidNumbers.append(nombre)
    return count, invalidNumbers
                

if __name__ == "__main__":
    with open("day2/input.txt", "r") as file:
        lignes = file.read()
        intervales = lignes.split(",")
        count = 0
        invalidNumbers = []
        for intervale in intervales:
            min_str, max_str = intervale.split('-')
            min, max = int(min_str), int(max_str)
            count, invalidNumbers = count_invalid(min, max, count, invalidNumbers)
        resultat = sum(invalidNumbers)
        print(resultat)
            