f = open("input.txt", "r")
nums = [x.strip().split(",") for x in f.readlines()]
f.close()

def solution(num, part="a"):
    tmp = num[0].split("-")
    a = list(range(int(tmp[0]), int(tmp[1])+1))
    tmp = num[1].split("-")
    b = list(range(int(tmp[0]), int(tmp[1])+1))

    comb_set = set(a) & set(b)

    if part == "a":
        if len(comb_set) == len(a) or len(comb_set) == len(b):
            return 1
        else:
            return 0
    else:
        if len(comb_set) != 0:
            return 1
        else:
            return 0

print(f"Part A: {sum([solution(num) for num in nums])}")
print(f"Part B: {sum([solution(num, part='b') for num in nums])}")
