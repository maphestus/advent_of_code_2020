
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
