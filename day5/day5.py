# f = open("sample_input.txt", "r")
f = open("input.txt", "r")
inputs = [x for x in f.readlines()]
f.close()

# Find the row with the column numbers
idx_row = 0
for idx, row in enumerate(inputs[:20]):
    if row[1].isdigit():
        idx_row = idx
        break

# Use the column numbers to assemble stacks
stacks = []
for idx, character in enumerate(inputs[idx_row]):
    if character.isdigit():
        new_stack = []
        for row in range(idx_row - 1, -1, -1):
            if inputs[row][idx] != " ":
                new_stack.append(inputs[row][idx])
        stacks.append(new_stack)

instruct = [row.strip() for row in inputs[idx_row+2:]]
for inst in instruct:
    inst_breakdown = inst.split(" ")
    move_num = int(inst_breakdown[1])
    from_num = int(inst_breakdown[3]) - 1
    to_num = int(inst_breakdown[5]) - 1
    for x in range(move_num):
        stacks[to_num].append(stacks[from_num].pop())

output = "".join([stack[-1] for stack in stacks])
print(f"Part A: {output}")

stacks = []
for idx, character in enumerate(inputs[idx_row]):
    if character.isdigit():
        new_stack = []
        for row in range(idx_row - 1, -1, -1):
            if inputs[row][idx] != " ":
                new_stack.append(inputs[row][idx])
        stacks.append(new_stack)

instruct = [row.strip() for row in inputs[idx_row+2:]]
for inst in instruct:
    inst_breakdown = inst.split(" ")
    move_num = int(inst_breakdown[1])
    from_num = int(inst_breakdown[3]) - 1
    to_num = int(inst_breakdown[5]) - 1


    print(inst)
    vals = stacks[from_num][(move_num*-1):]
    print("Vals: ", vals)
    for idx, stack in enumerate(stacks):
        print(f"Stack {idx + 1}: ", stack)
    for val in vals:
        stacks[from_num].pop()
        stacks[to_num].append(val)

output = "".join([stack[-1] for stack in stacks])
print(f"Part B: {output}")
