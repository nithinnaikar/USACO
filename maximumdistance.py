# Source: https://usaco.guide/general/io
import math


n = int(input())

x_coords = list(map(int, input().split()))
y_coords = list(map(int, input().split()))
points = [(x_coord, y_coord) for x_coord, y_coord in zip(x_coords, y_coords)]

def euclidean_distance(point_1, point_2):
    return math.sqrt((point_2[0] - point_1[0])**2  + (point_2[1] - point_1[1])**2)

high = 0

# This nested loop will perform more checks than necessary but that is fine for this problem

for point_1 in points: 
    for point_2 in points: 
        squared_euclidean_distance = euclidean_distance(point_1, point_2)**2
        if squared_euclidean_distance > high:
            high = squared_euclidean_distance 
        else:
            pass


print(round(high))

