# Task
class Shapes:
    def __init__(self, name, side, type, size):
        self.name = name
        self.side = side
        self.type = type
        self.size = size

    def area(self):
        print("I am a " + self.name + "\n" +
              "I have " + self.side + "\n" +
              "I am a " + self.type + "\n" +
              "It is " + self.size)


objShapes = Shapes("shape", "4 sides", "polygon", "14cm")
objShapes.area()


class Circle(Shapes):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        result = 3.14 * self.radius * self.radius
        return result
    """ print(result) """


objCoin = Circle(5)
"""" objCoin.area() """
print(objCoin.area())


class Triangle(Shapes):
    def __init__(self, height, base):
        self.height = height
        self.base = base

    def area(self):
        areaTri = (1 / 2) * self.base * self.height
        return areaTri


objPyramid = Triangle(5, 10)
print(objPyramid.area())


class Rectangle(Shapes):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        areaRect = self.length * self.width
        return areaRect


objLaptop = Rectangle(7, 3)
print(objLaptop.area())


class Square(Shapes):
    def __init__(self, side):
        self.side = side

    def area(self):
        areaSqu = self.side * 4
        return areaSqu


objBox = Square(5)
print(objBox.area())