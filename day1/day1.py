# f = open("sample_input.txt", "r")
f = open("input.txt", "r")
nums = [x.strip() for x in f.readlines()]
f.close()

elves = []
c_elves = []
for num in nums:
    if num != '':
        c_elves.append(int(num))
    else:
        elves.append(c_elves)
        c_elves = []
elves.append(c_elves)


elf_calories = []
max_calories = 0
for idx, elf in enumerate(elves):
    elf_calories.append(sum(elf))
    if sum(elf) > max_calories:
        max_calories = sum(elf)
        print(f"new max: {sum(elf)} at idx {idx}")

max_cals = max(elf_calories)
max_elf = elf_calories.index(max_cals)
print(f"Part 1: {max_elf+1}, Max Cals: {max_cals}")

sorted_cals = sorted(elf_calories)
print(f"Part 2: {sum(sorted_cals[-3:])}")
