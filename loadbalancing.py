# Source: https://usaco.guide/general/io
# Program only passes 5/10 test cases due to TLE. Can make program more efficient by limiting search space to only coordinates that are close to the average coordinate
# all cows. 
import sys

sys.stdin = open("balancing.in", "r")
sys.stdout = open("balancing.out", "w")

N, B = map(int, input().split())

cow_coordinates = []

for _ in range(N):
    x, y = map(int, input().split())
    cow_coordinates.append((x, y))

ms = []

for a in range(0, B + 2, 2):
    for b in range(0, B + 2, 2):
        quadrant_1_cows, quadrant_2_cows, quadrant_3_cows, quadrant_4_cows = 0, 0, 0, 0
        for cow in cow_coordinates:
            if cow[0] > a and cow[1] > b:
                quadrant_1_cows += 1
            elif cow[0] < a and cow[1] > b:
                quadrant_2_cows += 1
            elif cow[0] < a and cow[1] < b:
                quadrant_3_cows += 1
            else:
                quadrant_4_cows += 1

        m = max(quadrant_1_cows, quadrant_2_cows, quadrant_3_cows, quadrant_4_cows)
        ms.append(m)

print(min(ms))

