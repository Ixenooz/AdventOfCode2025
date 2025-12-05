def access_rolls(grid):
    final_grid = grid.copy()
    hauteur = len(grid)
    largeur = len(grid[0])
    directions = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1)
    ]
    accessedRolls = 0
    for line in range(hauteur):
        for column in range(largeur):
            if grid[line][column] == '@':
                count = 0
                for dirRow, dirCol in directions:
                    nr, nc = line + dirRow, column + dirCol
                    if 0 <= nr < hauteur and 0 <= nc < largeur:
                        if grid[nr][nc] == '@':
                            count += 1
                if (count < 4):
                    accessedRolls += 1
                    final_grid[line] = final_grid[line][:column] + 'x' + final_grid[line][column+1:]
    return accessedRolls
                    
if __name__ == "__main__":
    with open("day4/input.txt", "r") as file:
        input = file.read()
        grid = input.split("\n")
        print(access_rolls(grid))