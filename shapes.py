
class Circle:
    def __init__(self,r):
        self.r=r

    def area(self):
        PI = 3.14
        A = PI * (self.r*self.r)
        return A

    def circumference(self):
        PI = 3.14
        c=2*PI*self.radius
        return c
class Square:
    def __init__(self,a):
        self.a=a

    def area(self):
        A = self.a*self.a
        return A

    def parimeter(self):
        P = 4*self.a
        return P

class Rectangle:
    def __init__(self,w,l):
        self.w=w
        self.l=l
        
        
    def my_area(self):
        A=self.w*self.l
        return A

    def my_perimeter(self):
        P=2*self.w+self.l
        return P


class Sphere:
    def __init__(self,r):
        self.r=r
        
        
    def surface_area(self):
        PI = 3.14
        A=4*PI*(self.r*self.r)
        return A

    def volume(self):
        PI = 3.14
        V=4/3*(PI*(self.r+self.r))
        return V



    