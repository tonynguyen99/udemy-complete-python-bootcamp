# Problem 1

class Line:
  
  def __init__(self, coor1, coor2):
    self.coor1 = coor1
    self.coor2 = coor2
    
  def distance(self):
    self.xDiff = self.coor1[0] - self.coor2[0]
    self.yDiff = self.coor1[1] - self.coor2[1]
    
    return (self.xDiff ** 2 + self.yDiff ** 2)**0.5

  def slope(self):
    return self.yDiff/self.xDiff
  
coordinate1 = (3, 2)
coordinate2 = (8, 10)

points = Line(coordinate1, coordinate2)

print(points.distance())
print(points.slope())

# Problem 2

class Cylinder():
  
  pi = 3.14
  
  def __init__(self, height=1, radius=1):
    self.height = height
    self.radius = radius

  def volume(self):
    return Cylinder.pi * (self.radius ** 2) * self.height
  
  def surfaceArea(self):
    return 2 * Cylinder.pi * self.radius * self.height + 2 * Cylinder.pi * (self.radius ** 2)
  
can = Cylinder(2, 3)

print(can.volume())
print(can.surfaceArea())