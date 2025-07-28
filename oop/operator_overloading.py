class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  
  def __add__(self, point):
    x = self.x + point.x
    y = self.y + point.y
    return Point(x, y)
  
  def __str__(self):
    return f"Point({self.x}, {self.y})"

p1 = Point(3, 4)
p2 = Point(4, 3)
print(p1)
print(p2)

p3 = p1 + p2
print(f"p3 is {p3}")