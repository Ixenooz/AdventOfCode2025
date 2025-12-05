import time

def mergeRanges(ranges):
    ranges = sorted(ranges, key=lambda r: r[0])
    merged = [ranges[0]]

    for start, end in ranges[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end + 1:
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))
    return merged

def countFresh(ranges):
    count = 0
    for low, high in ranges:
        count += (high - low + 1)
    return count

if __name__ == "__main__":
    with open("day5/input.txt", "r") as file:
        input = file.read()
        lines = input.split("\n\n")[0].split("\n")
        ranges = []
        perf_start = time.perf_counter()
        for line in lines:
            low, high = map(int, line.split("-"))
            ranges.append((low, high))
        print(countFresh(mergeRanges(ranges)))
        perf_end = time.perf_counter()
        print(f"Performance: {perf_end - perf_start} seconds")