# Problem 86

import math

neighbors = [(1, 2), (3, 4), (7, 1), (5, 6)]
print("Neighbors:", neighbors)

#Accept neighbors (set of 2D coordinates) and a point, find nearest neighbor.

#By Loop
x = float(input("Enter x of point: "))
y = float(input("Enter y of point: "))

min_distance = None
nearest = None

for neighbor in neighbors:
    distance = math.sqrt((neighbor[0] - x)**2 + (neighbor[1] - y)**2)
    if min_distance is None or distance < min_distance:
        min_distance = distance
        nearest = neighbor

print("Nearest neighbor:", nearest)
print("Distance:", round(min_distance, 4))
