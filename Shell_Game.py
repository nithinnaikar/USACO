# Source: https://usaco.guide/general/io

import sys

sys.stdin = open("shell.in", "r")
sys.stdout = open("shell.out", "w")

num_swaps = int(input())

case_1 = [1, 0, 0]
case_2 = [0, 1, 0]
case_3 = [0, 0, 1]

correct_guesses_1 = 0
correct_guesses_2 = 0
correct_guesses_3 = 0

for swap in range(num_swaps):
    a, b, g = map(int, input().split())

    # Case 1: Pebble is initially under shell 1

    case_1_copy = case_1[:]
    case_1[a - 1] = max(0, case_1_copy[b - 1])
    case_1[b - 1] = max(0, case_1_copy[a - 1])
    if g == case_1.index(1) + 1:
        correct_guesses_1 += 1
        
    
    # Case 2: Pebble is initially under shell 2

    case_2_copy = case_2[:]
    case_2[a - 1] = max(0, case_2_copy[b - 1])
    case_2[b - 1] = max(0, case_2_copy[a - 1])
    if g == case_2.index(1) + 1:
        correct_guesses_2 += 1


    # Case 3: Pebble is initially under shell 3

    case_3_copy = case_3[:]
    case_3[a - 1] = max(0, case_3_copy[b - 1])
    case_3[b - 1] = max(0, case_3_copy[a - 1])
    if g == case_3.index(1) + 1:
        correct_guesses_3 += 1

    
print(max(correct_guesses_1, correct_guesses_2, correct_guesses_3))

