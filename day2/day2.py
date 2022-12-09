# f = open("sample_input2.txt", "r")
f = open("input.txt", "r")
nums = [x.strip().split(' ') for x in f.readlines()]
f.close()

def rps(vals):
    elf_choices = {
        "A": 1,
        "B": 2,
        "C": 3
    }
    player_choices = {
        "X": 1,
        "Y": 2,
        "Z": 3
    }

    elf = elf_choices[vals[0]]
    player = player_choices[vals[1]]
    score = 0

    if elf == player:
        score += (player + 3)
    elif elf == 1:
        if player == 2:
            score += 8
        if player == 3:
            score += 3
    elif elf == 2:
        if player == 1:
            score += 1
        if player == 3:
            score += 9
    elif elf == 3:
        if player == 1:
            score += 7
        if player == 2:
            score += 2

    return score

total_score = 0
for num in nums:
    total_score += rps(num)
print(f"Part A: {total_score}")


def part_b(vals):
    choice = ""
    elf = vals[0]
    player = vals[1]
    if elf == "A":
        if player == "X":
            choice = "Z"
        if player == "Y":
            choice = "X"
        if player == "Z":
            choice = "Y"

    elif elf == "B":
        if player == "X":
            choice = "X"
        if player == "Y":
            choice = "Y"
        if player == "Z":
            choice = "Z"

    elif elf == "C":
        if player == "X":
            choice = "Y"
        if player == "Y":
            choice = "Z"
        if player == "Z":
            choice = "X"

    return [vals[0], choice]


partB_score = 0
numsB = [part_b(num) for num in nums]
for num in numsB:
    partB_score += rps(num)
print(f"Part B: {partB_score}")
