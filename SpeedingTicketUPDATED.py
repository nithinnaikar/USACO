# Source: https://usaco.guide/general/io

import sys

sys.stdin = open("speeding.in", "r")
sys.stdout = open("speeding.out", "w")

n, m = map(int, input().split())

speed_limits = []

for _ in range(n):
    length, speed_limit = map(int, input().split())
    for _ in range(length):
        speed_limits.append(speed_limit)

bessie_speeds = []

for _ in range(m):
    length, bessie_speed = map(int, input().split())
    for _ in range(length):
        bessie_speeds.append(bessie_speed)

speed_differences = []

for speed_limit, bessie_speed in zip(speed_limits, bessie_speeds):
    speed_difference = bessie_speed - speed_limit
    if speed_difference >= 0:
        speed_differences.append(speed_difference)

print(max(speed_differences))

