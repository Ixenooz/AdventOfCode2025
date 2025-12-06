import time

def calculateColumn(column):
    total = int(column[0][0])
    taille = len(column) -1
    for i in range(1, taille):
        number = int(column[i][0])
        op = column[taille][0]
        if op == "*":
            total = total * number
        elif op == "+":
            total = total + number
    return total
        

if __name__ == "__main__":
    with open("day6/input.txt", "r") as file:
        input = file.read()
        lines = input.strip().split("\n")
        rowsNumber = [row.split() for row in lines[:-1]]
        operators = lines[-1].split()

        result = 0
        for columnIndex in range(len(operators)):
            column = [[row[columnIndex]] for row in rowsNumber]
            column.append([operators[columnIndex]])
            result += calculateColumn(column)

        print(result)






