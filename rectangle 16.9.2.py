class Rectangle:
    def __init__(self, x,y):
        self.x = x
        self.y = y
    def area(self):
        return f'Rectangle: {self.x * self.y}.'
rect_1 = Rectangle(10,15)
print(rect_1.area())
