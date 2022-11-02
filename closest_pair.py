import math
import sys

# Finds the two closest points from the set of points
# Using Bruteforce approach
def closestPair(p):
	dmin = sys.maxsize
	index1 = index2 = -1

	for i in range(len(p)):
		for j in range(i+1, len(p)):
			# Using formula of Euclidean distance to find closest points
			d = math.sqrt((p[i][0] - p[i][1])**2 + (p[j][0] - p[j][1])**2)
			if d < dmin:
				dmin = d
				index1, index2 = i, j

	return index1, index2

# let we have these set of points
points = [(1,1),(2,2),(1,3),(3,6),(9,15),(8,12),(4,7),(9,7),(4,4),(5,4),(3,3),(6,7),(8,9),(9,2)]
p1, p2 = closestPair(points)
print(p1, p2)