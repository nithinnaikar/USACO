# Source: https://usaco.guide/general/io

import sys
import string

#sys.stdin = open("blocks.in", "r")
#sys.stdout = open("blocks.out", "w")

# Note: initial algorithm exceeded time limit on some test cases since it was a naive exponential
# time solution. Efficient algorithm reasoning is as follows: maintain a dictionary map that has the 
# counts for each letter that will eventually be returned as final solution. Then, iterate through
# each of the n boards. For each board, determine the frequency of each of the characters in the 
# first word and the second word. Then, for each letter in the alphabet, add the maximum of the
# frequency of the letter in the first word and the frequency of the letter in the second word to 
# the value of the corresponding letter key in the dictionary. So do this for each board. Remember,
# this works on a board by board basis. So you need to have enough characters to spell out each board
# However, if you have enough characters for the maximum of the two frequencies for a certain character,
# then you cover both words in a board. You need to keep adding to this value when you encounter new boards
# so that you have enough characters to cover the entire front facing set. 

n = int(input())

counts = dict(zip(list(string.ascii_lowercase), [0] * 26))

for _ in range(n):
    word1, word2 = input().split()
    for letter in list(string.ascii_lowercase):
        counts[letter] += max(word1.count(letter), word2.count(letter))

for value in counts.values():
    print(value)


