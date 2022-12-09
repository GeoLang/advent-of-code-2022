import numpy as np

f = open("sample_input.txt", "r")
# f = open("sample_input2.txt", "r")
# f = open("input.txt", "r")
stream = np.array([[int(num.strip()) for num in row.strip()] for row in f.readlines()])
f.close()


def check_visible(x: int, y: int, grid: np.array):
    larger = False

    # print(grid[x, y])
    if x == 0 or x == (grid.shape[0] - 1) or y == 0 or y == (grid.shape[1] - 1):
        return 1

    else:
        if all(grid[x, :y] < grid[x,y]) or all(grid[x, y+1:] < grid[x,y]) or all(grid[:x, y] < grid[x,y]) or all(grid[x+1:, y] < grid[x,y]):
            return 1


    # print(grid[x])
    # print(grid[x, :y], grid[x, y], grid[x, y+1:], any(grid[x, y:] < grid[x,y]))
    # print(grid[x, y:], grid[x, y], grid[x, :y-1], all(grid[x, y:] >= grid[x,y]) and all(grid[x, :y-1] >= grid[x,y]))

    # print(grid[x,:y-1], grid[x, y], grid[x,y:], any(grid[x,:y-1] < grid[x,y]), ": ", x, y)
    if larger:
        return 1

    return 0

def check_scenery(y: int, x: int, grid: np.array):

    # If at edge, return 0
    # if x == 0 or x == (grid.shape[0] - 1) or y == 0 or y == (grid.shape[1] - 1):
    #     return 0

    score = []
    taller = grid >= grid[x,y]

    print(f"X: {x},\tY:{y},\tGrid: {grid[x,y]}")
    
    # Check top
    dist = 0
    top = taller[x, :y]

    # for x in range(y, 0, -1):

    # Check bottom
    dist = 0
    bottom = list(reversed(taller[x+1:, y]))
    for item in bottom:
        if item:
            score.append(dist+1)
            break
        dist += 1
    if len(score) != 1:
        if dist == 0:
            dist = 1

        score.append(dist)

    # Check top
    dist = 0
    top = taller[:x, y]
    for item in top:
        if item:
            if score == 0:
                score = 1
            score.append(dist+1)
            break
        dist += 1
    if len(score) != 2:
        if score == 0:
            score = 1
        score.append(dist)

    # Check right
    dist = 0
    right = taller[x, y+1:]
    for item in right:
        if item:
            if score == 0:
                score = 1
            score.append(dist+1)
            break
        dist += 1
    if len(score) != 3:
        if score == 0:
            score = 1
        score.append(dist)

    # Check left
    dist = 0
    left = list(reversed(taller[x, y+1:]))
    for item in left:
        if item:
            if score == 0:
                score = 1
            score.append(dist)
            break
        dist += 1
    if len(score) != 4:
        if score == 0:
            score = 1
        score.append(dist)

        
    print(score)

    return np.array(score).prod()


part_a = []
for x in range(stream.shape[0]):
    for y in range(stream.shape[1]):
        part_a.append(check_visible(x, y, stream))

print(f"Part A: {sum(part_a)}")

# part_b = np.zeros(stream.shape)
# for x in range(stream.shape[0]):
#     for y in range(stream.shape[1]):
#         part_b[x,y] = check_scenery(x, y, stream)

check_scenery(2,1,stream)
