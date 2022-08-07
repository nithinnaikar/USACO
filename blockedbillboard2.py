# 9/10 test cases
import sys

sys.stdin = open("billboard.in", "r")
sys.stdout = open("billboard.out", "w")

lawn_bl_x, lawn_bl_y, lawn_tr_x, lawn_tr_y = map(int, input().split())
feed_bl_x, feed_bl_y, feed_tr_x, feed_tr_y = map(int, input().split())

def area(x1, y1, x2, y2):
  length = abs(x2 - x1)
  width = abs(y2 - y1)
  return length * width 

def intersect(rec1_x1, rec1_y1, rec1_x2, rec1_y2, rec2_x1, rec2_y1, rec2_x2, rec2_y2):
  x_overlap = max(0, min(rec1_x2, rec2_x2) - max(rec1_x1, rec2_x1))
  y_overlap = max(0, min(rec1_y2, rec2_y2) - max(rec1_y1, rec2_y1))
  return x_overlap, y_overlap

x_overlap, y_overlap = intersect(lawn_bl_x, lawn_bl_y, lawn_tr_x, lawn_tr_y, feed_bl_x, feed_bl_y, feed_tr_x, feed_tr_y)

intersection_area = x_overlap * y_overlap

lawn_area = area(lawn_bl_x, lawn_bl_y, lawn_tr_x, lawn_tr_y)

if intersection_area <= 0:
  print(lawn_area)
else:
  if (x_overlap == (lawn_tr_x - lawn_bl_x)) or (y_overlap == (lawn_tr_y - lawn_bl_y)):
    print(lawn_area - intersection_area)
  else: 
    print(lawn_area)
