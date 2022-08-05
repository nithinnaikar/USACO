import sys 

sys.stdin = open("billboard.in", "r")
sys.stdout = open("billboard.out", "w")

b1_x1, b1_y1, b1_x2, b1_y2 = map(int, input().split())
b2_x1, b2_y1, b2_x2, b2_y2 = map(int, input().split())
t_x1, t_y1, t_x2, t_y2 = map(int, input().split())

def area(x1, y1, x2, y2):
  length = abs(x2 - x1)
  width = abs(y2 - y1)
  return length * width 

def intersect(rec1_x1, rec1_y1, rec1_x2, rec1_y2, rec2_x1, rec2_y1, rec2_x2, rec2_y2):
  x_overlap = max(0, min(rec1_x2, rec2_x2) - max(rec1_x1, rec2_x1))
  y_overlap = max(0, min(rec1_y2, rec2_y2) - max(rec1_y1, rec2_y1))
  return x_overlap * y_overlap

print((area(b1_x1, b1_y1, b1_x2, b1_y2) - intersect(b1_x1, b1_y1, b1_x2, b1_y2, t_x1, t_y1, t_x2, t_y2)) + (area(b2_x1, b2_y1, b2_x2, b2_y2) - intersect(b2_x1, b2_y1, b2_x2, b2_y2, t_x1, t_y1, t_x2, t_y2)))