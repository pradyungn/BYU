import math

class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return('<' + self.__class__.__name__ + ' x = ' + str(self.x) + ' y = ' + str(self.y)+'>')

class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def __repr__(self):
        return('<'+self.__class__.__name__ + ' x = ' + str(self.x) + ' y = ' +str(self.y)+' radius = '+str(self.radius)+'>')

    def  circumference(self):
        diameter = self.radius * 2
        return(math.pi*diameter)

    def area(self):
        c = self.radius^2
        return(math.pi*self.radius)

class Rectangle(Shape):
    def __init__(self, x, y, height, width):
        super().__init__(x, y)
        self.height = height
        self.width = width
    def __repr__(self):
        return('<' + self.__class__.__name__ + ' x = ' + str(self.x) + ' y = ' + str(self.y) + ' height = ' + str(self.height) + ' width = ' + str(self.width) + '>')

    def area(self):
        return(self.height*self.width)

    def circumference(self):
        return(2*self.height+2*self.width)

class Square(Rectangle):
    def __init__(self, x, y, height, width):
        super().__init__(x, y, height, width)
        self.width = self.height
        
    def __repr__(self):
        return('<' + self.__class__.__name__ + ' x = ' + str(self.x) + ' y = ' + str(self.y) + ' height = ' + str(self.height) + ' width = ' + str(self.width) + '>')
    
class RightTriangle(Shape):
    def __init__(self, x, y, height, width):
        super().__init__(x, y)
        self.height = height
        self.width = width

    def __repr__(self):
        return('<' + self.__class__.__name__ + ' x = ' + str(self.x) + ' y = ' + str(self.y) + ' height = ' + str(self.height) + ' width = ' + str(self.width) + '>')

    def area(self):
        initial = self.height*self.width
        return(initial/2)

    def circumference(self):
        a = self.height^2
        b = self.width^2
        c = math.sqrt(a+b)
        return(self.width + self.height + c)

MyRectangle = Rectangle(33, 77, 12, 15)
MyRightTriangle = RightTriangle(99, 128, 2, 2)
MyCircle = Circle(12, 12, 6)
MySquare = Square(12, 45, 12, 12)

print('The Area of my Circle is '+str(MyCircle.area()))
print('The Area of my Rectangle is '+str(MyRectangle.area()))
print('The Area of my Triangle is ' + str(MyRightTriangle.area()))
print('The Area of my Square is' + str(MySquare.area()))

print('The circumference of my Circle is '+str(MyCircle.circumference()))
print('The perimeter of my Rectangle is '+str(MyRectangle.circumference()))
print('The perimeter of my Triangle is ' + str(MyRightTriangle.circumference()))
print('The perimeter of my Square is ' + str(MySquare.circumference()))

#Polymorphism displayed by square and rectangle



    
        
