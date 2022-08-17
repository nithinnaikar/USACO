# Source: https://usaco.guide/general/io

import sys

sys.stdin = open("cownomics.in", "r")
sys.stdout = open("cownomics.out", "w")

n, m = map(int, input().split())

spotty_genomes = []
plain_genomes = []

for _ in range(n):
    spotty_genomes.append(input())

for _ in range(n):
    plain_genomes.append(input())

possible_locations = 0

for genome_position in range(m):
    spotty_characters = set([spotty_genome[genome_position] for spotty_genome in spotty_genomes])
    plain_characters = set([plain_genome[genome_position] for plain_genome in plain_genomes])
    if spotty_characters.isdisjoint(plain_characters):
        possible_locations += 1

print(possible_locations)
