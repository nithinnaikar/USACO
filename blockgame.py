# Source: https://usaco.guide/general/io

import sys
import string
import itertools

sys.stdin = open("blocks.in", "r")
sys.stdout = open("blocks.out", "w")

n = int(input())

boards = []

for _ in range(n):
    word1, word2 = input().split()
    boards.append((word1, word2))

counts = dict(zip(list(string.ascii_lowercase), [0] * 26))

possible_sets = [p for p in itertools.product(*boards)]

for word in possible_sets[0]:
    for letter in word:
        counts[letter] += 1

def compute_differences(target_characters, available_characters):
    differences = []
    for target_character in set(target_characters):
        difference = target_characters.count(target_character) - available_characters[target_character]
        differences.append((target_character, difference))
    return differences

for possible_set in possible_sets[1:]:
    differences = compute_differences("".join(possible_set), counts)
    for difference in differences:
        counts[difference[0]] += max(0, difference[1])
   
for value in counts.values():
    print(value)
