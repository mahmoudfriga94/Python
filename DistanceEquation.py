import math

def distance(p1,p2):
    d = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )
    return d

p1 = [5, 1]
p2 = [2, 7]
d = distance(p1,p2)
print(d)