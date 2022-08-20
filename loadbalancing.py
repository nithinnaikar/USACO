# Source: https://usaco.guide/general/io

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
        quadrant_1_cows = [cow for cow in cow_coordinates if cow[0] > a and cow[1] > b]
        quadrant_2_cows = [cow for cow in cow_coordinates if cow[0] < a and cow[1] > b]
        quadrant_3_cows = [cow for cow in cow_coordinates if cow[0] < a and cow[1] < b]
        quadrant_4_cows = [cow for cow in cow_coordinates if cow[0] > a and cow[1] < b]
        m = max(len(quadrant_1_cows), len(quadrant_2_cows), len(quadrant_3_cows), len(quadrant_4_cows))
        ms.append(m)

print(min(ms))
