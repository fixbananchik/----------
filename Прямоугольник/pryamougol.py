class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


from math import sqrt
def distance(point1, point2):
    return sqrt(( (point1.x - point2.x) ** 2 ) + ( (point1.y - point2.y) ** 2 ))


class Pryamougol:
    def __init__(self, point1, point2, point3, point4):
        self.A = point1
        self.B = point2
        self.C = point3
        self.D = point4

    def perimetr(self):
        return 2(distance(self.A, self.B) + distance(self.B, self.C))
    
    def kvadrat(self):
        if distance(self.A, self.B) == distance(self.B, self.C) == distance(self.C, self.D) == distance(self.D, self.A):
            return True
        else:
            return False 
        
        
    def ploch(self):
        return distance(self.A, self.B) * distance(self.B, self.C)

A = Point(0,0)
B = Point(0,1)
C = Point(1,0)
D = Point (1,1)
ABCD = Pryamougol(A,B,C,D)
print(ABCD.perimetr(), ABCD.ploch(), ABCD.kvadrat())