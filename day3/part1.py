def max_joltage(batterie):
    maxs = [0, 0]
    maxsIndex = [0, 0]
    for i in range(len(batterie)-1):
        if int(batterie[i]) > maxs[0]:
            maxs[0] = int(batterie[i])
            maxsIndex[0] = i
    for j in range(len(batterie)-1, maxsIndex[0], -1):
        if int(batterie[j]) > maxs[1] and j != maxsIndex[0]:
            maxs[1] = int(batterie[j])
            maxsIndex[1] = j
    return maxs[0]*10 + maxs[1]

if __name__ == "__main__":
    with open("day3/input.txt", "r") as file:
        input = file.read()
        lines = input.split("\n")
        result = 0
        for line in lines:
            result += max_joltage(line)
        print(result)
        
