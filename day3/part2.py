def max_joltage(batterie):
    result = []
    start = 0
    digits = list(batterie)
    for i in range(12):
        max = '0'
        max_index = start
        for j in range(start, len(digits) - (12 - i - 1)):
            if digits[j] > max:
                max = digits[j]
                max_index = j
        result.append(max)
        start = max_index + 1
    return int("".join(result))

if __name__ == "__main__":
    with open("day3/input.txt", "r") as file:
        input = file.read()
        lines = input.split("\n")
        result = 0
        for line in lines:
            result += max_joltage(line)
        print(result)