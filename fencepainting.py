import sys

# Reading input
sys.stdin = open("paint.in", "r")
sys.stdout = open("paint.out", "w")

a, b = map(int, input().split())
c, d = map(int, input().split())

# Case 1: intervals are disjoint 

if (d < a) or (b < c):
  print((b - a) + (d - c))
else: # Case 2: intervals overlap
  print(max(d, b) - min(c, a))
