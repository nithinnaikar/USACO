# Source: https://usaco.guide/general/io

import sys
import string

sys.stdin = open("blocks.in", "r")
sys.stdout = open("blocks.out", "w")

n = int(input())

counts = dict(zip(list(string.ascii_lowercase), [0] * 26))

for _ in range(n):
    word1, word2 = input().split()
    for letter in list(string.ascii_lowercase):
        counts[letter] += max(word1.count(letter), word2.count(letter))

for value in counts.values():
    print(value)


