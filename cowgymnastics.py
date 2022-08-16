# Source: https://usaco.guide/general/io

import sys
import itertools

sys.stdin = open("gymnastics.in", "r")
sys.stdout = open("gymnastics.out", "w")

k, n = map(int, input().split())

rankings = []

for _ in range(k):
    rankings.append(list(map(int, input().split())))

two_sized_subsets = list(itertools.combinations(range(1, n + 1), 2))

consistent_pairs = 0

for pair in two_sized_subsets:

    # If a is initially ranked higher than b
    if rankings[0].index(pair[0]) < rankings[0].index(pair[1]):
        consistency = 0
        for session in rankings[1:]:
            if session.index(pair[0]) < session.index(pair[1]):
                consistency += 1
            else:
                break

    
    # If b is initially ranked higher than a

    else:
        consistency = 0
        for session in rankings[1:]:
            if session.index(pair[1]) < session.index(pair[0]):
                consistency += 1
            else:
                break

    if consistency == k - 1:
        consistent_pairs += 1

print(consistent_pairs)


        