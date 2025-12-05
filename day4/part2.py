import time

def access_rolls(grid, accessedRolls=0):
    final_grid = grid.copy()
    hauteur = len(grid)
    largeur = len(grid[0])
    directions = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1)
    ]
    localAccessedRolls = 0
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
                    localAccessedRolls += 1
                    final_grid[line] = final_grid[line][:column] + 'x' + final_grid[line][column+1:]
    if localAccessedRolls == 0:
        return accessedRolls
    else:
        return access_rolls(final_grid, accessedRolls + localAccessedRolls)
                    
if __name__ == "__main__":
    with open("day4/input.txt", "r") as file:
        input = file.read()
        grid = input.split("\n")
        performance_start = time.perf_counter()
        print(access_rolls(grid))
        performance_end = time.perf_counter()
        print(f"Performance: {performance_end - performance_start} seconds")