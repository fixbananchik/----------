class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


from math import sqrt
def distance(point1, point2):
    return sqrt(( (point1.x - point2.x) ** 2 ) + ( (point1.y - point2.y) ** 2 ))


class Triangle:
    def __init__(self, point1, point2, point3):
        self.A = point1
        self.B = point2
        self.C = point3

    def perimetr(self):
        return distance(self.A, self.B) + distance(self.B, self.C) + distance(self.C, self.A)
    
    def ravnostoron(self):
        if distance(self.A, self.B) == distance(self.C, self.A) == distance(self.B, self.C):
            return True
        else:
            return False 
        
    def ravnobedr(self):
        if (distance(self.A, self.B) == distance(self.B, self.C) or distance(self.A, self.B) == distance(self.C, self.A) or distance(self.B, self.C) == distance(self.C, self.A)) and self.ravnostoron():
            return True
        else:
            return False
        
    def ploch(self):
        return sqrt(self.perimetr() * ((self.perimetr()) - distance(self.A, self.B)) * ((self.perimetr()) - distance(self.B, self.C)) * ((self.perimetr()) - distance(self.B, self.C))) 



J = Point(0,0)
O = Point(0,1)
P = Point(1,0)

JOP = Triangle(J, O, P)
print(JOP.perimetr(), JOP.ploch(), JOP.ravnobedr(), JOP.ravnostoron())
