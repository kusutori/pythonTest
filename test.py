import math


class shape:
    def __init__(self) -> None:
        pass

    def area(self):
        return "这只是一个形状"


class Circle(shape):
    def __init__(self, x, y, radius) -> None:
        super().__init__()
        self.x = x
        self.y = y
        self.radius = radius
        print("Circle 对象已构建")

    def area(self):
        return math.pi*self.radius*self.radius


class Rectangle(shape):
    def __init__(self, width, length) -> None:
        super().__init__()
        self.width = width
        self.length = length
        print("Rectangle 对象已构建")

    def area(self):
        return self.width*self.length


c1 = Circle(0, 0, 2)
print(c1.area())
r1 = Rectangle(1, 4)
print(r1.area())
