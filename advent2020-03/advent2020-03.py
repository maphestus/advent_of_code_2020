
hillmap = open("advent2020-03-input.txt", "r")

print(hillmap)

hill = []
sled = [0, 0]
hill_height = -1
hill_width = 0
tot_trees = 0

for a in hillmap:
    line = a.rstrip()
    hill_width = len(line)
    hill.append(line)
    hill_height = hill_height + 1

print(hill_height, hill_width)

while sled[0] < hill_height:
    sled[1] = sled[1] + 3
    if sled[1] >= hill_width:
        sled[1] = sled[1] - hill_width
    sled[0] = sled[0] + 1
    y = sled[0]
    x = sled[1]
    if hill[y][x] == "#":
        tot_trees = tot_trees + 1
    print(sled)
    print("sled is on", hill[y][x])

print("Total trees encountered:", tot_trees)

# PART 2


def tree_collision(hill_map, height, width, travel_y, travel_x):
    total_trees = 0
    sled_pos = [0, 0]
    # print(hill_map)
    # print(height, width)
    # print(travel_y, travel_x)

    while sled_pos[0] < height and (sled_pos[0] + travel_y) <= height:
        sled_pos[1] = sled_pos[1] + travel_x
        if sled_pos[1] >= width:
            sled_pos[1] = sled_pos[1] - width
        sled_pos[0] = sled_pos[0] + travel_y
        pos_y = sled_pos[0]
        pos_x = sled_pos[1]
        if hill_map[pos_y][pos_x] == "#":
            total_trees = total_trees + 1
        # print(sled_pos)
        # print("sled is on", hill_map[pos_y][pos_x])
    print(total_trees)
    return total_trees


run1 = tree_collision(hill, hill_height, hill_width, 1, 1)
run2 = tree_collision(hill, hill_height, hill_width, 1, 3)
run3 = tree_collision(hill, hill_height, hill_width, 1, 5)
run4 = tree_collision(hill, hill_height, hill_width, 1, 7)
run5 = tree_collision(hill, hill_height, hill_width, 2, 1)

trees = run1 * run2 * run3 * run4 * run5

print("Total trees multiplied together: ", trees)
