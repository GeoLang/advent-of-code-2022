f = open("input.txt", "r")
commands = [com.strip().split(" ") for com in f.readlines()]
f.close()

class Computer():
    def __init__(self):
        self.register = {"x": 1}
        self.cycles = 0
        self.register_history = [self.register["x"]]

    def add(self, register, val):
        self.add_history()
        self.add_history()
        self.register[register] += int(val)
        self.cycles += 2

    def noop(self):
        self.add_history()
        self.cycles += 1

    def add_history(self):
        self.register_history.append(self.register["x"])

    def execute(self, instructions):
        for instr in instructions:
            if instr[0][0:3] == "add":
                self.add(instr[0][3], instr[1])
            if instr[0] == "noop":
                self.noop()

computer = Computer()
computer.execute(commands)
hist = computer.register_history
a_idx = [20, 60, 100, 140, 180, 220]
part_a = []
for idx in a_idx:
    part_a.append(hist[idx] * idx)

print(f"Part A: {sum(part_a)}")

output = [[],[],[],[],[],[]]
for x in range(240):
    bin_idx = int(x / 40)
    pix_idx = x % 40
    pixel_distance = abs(pix_idx - (hist[x + 1]))
    val = "#" if pixel_distance <= 1 else "."
    output[bin_idx].append(val)

out = ["".join(x) for x in output]
print("Part B:")
for row in out:
    print(row)
