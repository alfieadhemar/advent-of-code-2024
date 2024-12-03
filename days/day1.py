#%%
import sys

sys.path.append("../")
from utils.file_reader import DataFile

def where(value, array2):
    result = []

    for a in array2:
        result.append(True if value == a else False)

    return result

def part1(data):
    dist = 0

    left = []
    right = []

    for line in data.lines:
        left.append(line[0])
        right.append(line[1])

    left = sorted(left)
    right = sorted(right)

    for i in range(len(data.lines)):
        dist += abs(left[i] - right[i])

    return dist

def part2(data):
    total = []

    left = []
    right = []

    for line in data.lines:
        left.append(line[0])
        right.append(line[1])

    left = sorted(left)
    right = sorted(right)

    for l in left:
        numMatches = [x for x in where(l, right) if x == True]
        if len(numMatches):
            total.append(numMatches*l)
        print(total)

    return sum(total)
        # if len(right[numMatches]) != 0:
        #     total.append(len(right[numMatches])*value)

def main():
    data = DataFile(1)
    print(f"Part 1: {part1(data)}\n")
    print(f"Part 2: {part2(data)}\n")

if __name__ == "__main__":
    main()
# %%
