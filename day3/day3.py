# f = open("sample_input.txt", "r")
f = open("input.txt", "r")
bags = [x.strip().split(' ')[0] for x in f.readlines()]
f.close()

def get_priority(character):
    char_val = ord(character)
    if char_val >  96:
        char_val = char_val - 96
    else:
        char_val = char_val - 38
    return char_val

def parta(bag):
    _len = int(len(bag)/2)
    a = bag[:_len]
    b = bag[_len:]
    dup = set(a) & set(b)
    dup_val = get_priority(dup.pop())
    return dup_val

def partb(bags):
    bags_split = []
    for idx in range(0, len(bags), 3):
        bags_split.append(bags[idx:idx+3])

    badges = []
    for trip in bags_split:
        a = set(trip[0])
        b = set(trip[1])
        c = set(trip[2])
        in_all = a & b & c
        badges.append(get_priority(in_all.pop()))
    return sum(badges)

part_a = [parta(bag) for bag in bags]
print(f"Part A: {sum(part_a)}")

print(f"Part B: {partb(bags)}")
