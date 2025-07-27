class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  
  def __add__(self, point):
    x = self.x + point.x
    y = self.y + point.y
    return Point(x, y)

p1 = Point(3, 4)
p2 = Point(4, 3)

p3 = p1 + p2
print(f"p3 is ({p3.x}, {p3.y})")