import numpy as np

f = open("input.txt", "r")
stream = [num.strip() for num in f.readlines()]
f.close()

class Rope():
    def __init__(self):
        self._head = [0,0]
        self._tail = [0,0]
        self.trail = {(0, 0)}

        self.sub_ropes = []

    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, loc):
        prev_head = self._head
        self._head = loc
        if check_distance():
            self._tail = prev_head

    def set_head(self, loc):
        prev_head = self._head
        self._head = loc
        move = [a - b for a, b in zip(self.head, self._tail)]

        if abs(move[0]) <= 1 and abs(move[1]) <= 1:
            return
        elif abs(move[0]) == 2 and abs(move[1]) == 2:
            self._tail[0] += move[0] / 2
            self._tail[1] += move[1] / 2
        elif abs(move[0]) == 2:
            self._tail[0] += move[0] / 2
            self._tail[1] = self.head[1]
        elif abs(move[1]) == 2:
            self._tail[1] += move[1] / 2
            self._tail[0] = self.head[0]

        if self.check_distance():
            self._tail = prev_head

        self.trail.add(tuple(self._tail))


    def move_head(self, _dir, val):
        for idx in range(int(val)):
            match _dir:
                case "R":
                    self.set_head([self.head[0] + 1, self.head[1]])
                case "L":
                    self.set_head([self.head[0] - 1, self.head[1]])
                case "U":
                    self.set_head([self.head[0], self.head[1] + 1])
                case "D":
                    self.set_head([self.head[0], self.head[1] - 1])
                case _:
                    print(f"Error: Invalid command: {_dir.lower()}")
            for idx, rope in enumerate(self.sub_ropes):
                if idx == 0:
                    rope.set_head(self._tail)
                else:
                    rope.set_head(self.sub_ropes[idx-1]._tail)

    def check_distance(self):
        """
        Return the distance between the head and the tail. Returns True if the
        distance is greater than 1 in any direction.
        """
        h = np.array(self.head)
        t = np.array(self._tail)
        dist = h - t
        if any(dist > 1):
            return True

        return False

rope = Rope()
for command in stream:
    rope.move_head(*command.split(" "))
print(f"Part A: {len(rope.trail)}")

rope = Rope()
ropes = [Rope() for x in range(9)]
rope.sub_ropes = ropes
for command in stream:
    rope.move_head(*command.split(" "))

print(f"Part B: {len(ropes[7].trail)}")
