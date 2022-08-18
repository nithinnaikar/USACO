# Source: https://usaco.guide/general/io

import sys
import itertools
import string

sys.stdin = open("circlecross.in", "r")
sys.stdout = open("circlecross.out", "w")

crossing_points = list(input())


possible_cow_pairs = list(itertools.combinations(set(string.ascii_uppercase), 2))

crossing_pairs = 0

for possible_cow_pair in possible_cow_pairs:
    cow_1_appearances = [i for i, x in enumerate(crossing_points) if x == possible_cow_pair[0]]
    cow_2_appearances = [i for i, x in enumerate(crossing_points) if x == possible_cow_pair[1]]
    if cow_1_appearances[0] < cow_2_appearances[0] < cow_1_appearances[1]:
        if cow_2_appearances[1] > cow_1_appearances[1]:
            crossing_pairs += 1
    elif cow_1_appearances[0] < cow_2_appearances[1] < cow_1_appearances[1]:
        if cow_2_appearances[0] < cow_1_appearances[0]:
            crossing_pairs += 1

print(crossing_pairs)
