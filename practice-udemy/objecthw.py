class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return((x2-x1)**2 + (y2-y1)**2)**0.5
    
    def slope(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return (y2-y1)/(x2-x1)

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1, coordinate2)

print(li.distance())
print(li.slope())


class Cylinder:
    
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        return 3.14 * ((self.radius)**2) * self.height
    
    def surface_area(self):
        return ((3.14 * 2) * (self.radius) * (self.height)) + ((3.14 * 2) * (self.radius **2))

c = Cylinder(2,3)

print(c.volume())
print(c.surface_area())

37.68