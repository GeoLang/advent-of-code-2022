f = open("input.txt", "r")
stream = [x.strip() for x in f.readlines()]
f.close()

class Dir:
    def __init__(self, parent=None, name=""):
        self.parent = parent
        self.name = name
        self.files = []
        self.dirs = {}
        self._size = 0

    @property
    def size(self):
        out = sum(self.files)

        if len(self.dirs) != 0:
            for key in self.dirs.keys():
                out += self.dirs[key].size

        return out

    def get_sizes(self):
        sizes = [self.size]

        for directory in self.dirs.values():
            sizes += directory.get_sizes()

        return sizes

    def print_dir(self, depth=0, max_depth=99):
        print(" "*(depth*2), "- ", self.name, " size: ", self.size, sep="")
        for _file in self.files:
            print(" "*((depth*2) + 2), "- ", _file, sep="")
        if depth < max_depth:
            for key in self.dirs.keys():
                self.dirs[key].print_dir(depth=depth+1)

root = Dir(None, "/")
cdir = root

for command in stream:
    split = command.split()

    if split[1] == "cd":
        match split[2]:
            case "/":
                cdir = root
            case "..":
                cdir = cdir.parent
            case _:
                cdir = cdir.dirs[split[2]]

    elif split[1] != "ls":
        if split[0] == "dir":
            cdir.dirs[split[1]] = Dir(cdir, split[1])
        else:
            cdir.files.append(int(split[0]))

root.print_dir()

def parta(root):
    global total
    total = 0

    def dive(folder):
        if folder.size <= 100000:
            global total
            total += folder.size
        if len(folder.dirs) != 0:
            for key in folder.dirs.keys():
                dive(folder.dirs[key])

    dive(root)
    print(f"Part A: {total}")

def partb(root):
    total_size = 70000000 - root.size
    print(f"Total size: {total_size}")

    global total
    total = []

    def dive2(folder):
        return_arr = []

        return_arr.append(folder.size)
        if len(folder.dirs) != 0:
            for key in folder.dirs.keys():
                vals = dive2(folder.dirs[key])
                if vals != None:
                    for val in vals:
                        return_arr.append(val)
        return return_arr

    total = dive2(root)
    print(sorted(total))
    print(f"Part B: {sorted(total)[0]}")
    val = (root.size - sorted(total)[0]) < 40000000
    print(val)
    return total

parta(root)
partb(root)

sizes = root.get_sizes()
print(f"Part 2: {next(size for size in sorted(sizes) if size >= sizes[0] - 40000000)}")
