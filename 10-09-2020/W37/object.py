class Point:
    static_field = 0
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f'Point(x={self.x}, y={self.y})'
        
#    def __add__(self, other):
#        return Point(self.x + other.x, self.y + other.y)
    

    def __call__(self):
        print("You can't call a point")
        
        
class Aviator:
    def fly(this):
        print(f"{this} can fly!")
        
class ClassPrinter:
    @classmethod
    def __repr__(cls):
        return f"{cls.__name__}"
    
class Bird(Aviator, ClassPrinter):
    pass

class EarthBound:
    def fly(this):
        print(f"{this} can't fly!")

class Penguin(Bird, EarthBound):
    pass

class PointFactory:
    
    @staticmethod
    def makePoint(x, y):
        return Point(x, y)
    
    

class ListKeeper:
    
    def __init__(self, x):
        self.x = x
    
    @property
    def x(self):
        return list(self._x)

    @x.setter
    def x(self, x):
        print(x)
        self._x = x
        
        
class XPoint:
    
    def __init__(self, x):
        self._x = x
        
    @property
    def x(self):
        return self._x

