def isFresh(number, ranges):
    for r in ranges:
        low, high = map(int, r.split("-"))
        if low <= number <= high:
            return True
    return False

if __name__ == "__main__":
    with open("day5/input.txt", "r") as file:
        input = file.read()
        ranges = input.split("\n\n")[0].split("\n")
        numbers = input.split("\n\n")[1].split("\n")
        count = 0
        for number in numbers:
            if isFresh(int(number), ranges):
                count += 1
        print(count)