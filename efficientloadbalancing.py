# Source: https://usaco.guide/general/io

import sys

sys.stdin = open("balancing.in", "r")
sys.stdout = open("balancing.out", "w")

N, B = map(int, input().split())

cow_coordinates = []

for _ in range(N):
    x, y = map(int, input().split())
    cow_coordinates.append((x, y))

ans = N

for x in range(N):
    for y in range(N):
        fence_x = cow_coordinates[x][0] + 1
        fence_y = cow_coordinates[y][1] + 1

        quadrant_1_cows, quadrant_2_cows, quadrant_3_cows, quadrant_4_cows = 0, 0, 0, 0
        for cow in cow_coordinates:
            if cow[0] > fence_x and cow[1] > fence_y:
                quadrant_1_cows += 1
            elif cow[0] < fence_x and cow[1] > fence_y:
                quadrant_2_cows += 1
            elif cow[0] < fence_x and cow[1] < fence_y:
                quadrant_3_cows += 1
            else:
                quadrant_4_cows += 1

        m = max(quadrant_1_cows, quadrant_2_cows, quadrant_3_cows, quadrant_4_cows)
        if m < ans:
            ans = m
        

print(ans)
