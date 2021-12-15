from abc import abstractmethod


class Shape:

    def get_area(self):
        pass
        return

    def get_perimeter(self):
        pass
        return

    def __str__(self):
        pass
        return


    @classmethod
    def check_if_args_not_below_zero(cls,*args):
        for arg in args:
            if arg < 0:
                raise ValueError
        return True        

    @classmethod
    def get_area_formula(cls):
        return

    @classmethod
    def get_perimeter_formula(cls):
        return  


class Circle(Shape):

    def __init__(self, r):
        self.check_if_args_not_below_zero(r)
        self.r = r


    @abstractmethod
    def get_area(self):
        return int(self.r) * int(self.r) * 3.14;

    @abstractmethod
    def get_perimeter(self):
        return  2 * int(self.r) * 3.14;

    @abstractmethod
    def __str__(self):
        return 'circle r is' , self.r




class Triangle(Shape):
    def __init__(self, a, b, c):
        self.check_if_args_not_below_zero(a)
        self.check_if_args_not_below_zero(b)
        self.check_if_args_not_below_zero(c)
        self.a = a
        self.b = b
        self.c = c


    @abstractmethod
    def get_area(self):
        s = (self.a + self.b + self.c) / 2
        return pow(s * (s - self.a) * (s - self.b) * (s - self.c), 0.5);

    @abstractmethod
    def get_perimeter(self):
        return  self.a + self.b + self.c

    @abstractmethod
    def __str__(self):
        return 'circle sides is' , self.a , self.b, self.c

class Rectangle(Shape):
    def __init__(self, a, b):
        self.check_if_args_not_below_zero(a)
        self.check_if_args_not_below_zero(b)
        self.a = a
        self.b = b

    @abstractmethod
    def get_area(self):
        return self.a * self.b;

    @abstractmethod
    def get_perimeter(self):
        return 2 * (self.a + self.b);

    @abstractmethod
    def __str__(self):
        return 'circle sides is' , self.a , self.b;
class Square(Rectangle):
    def __init__(self, a):
        self.check_if_args_not_below_zero(a)
        self.a = a
        self.b = a

    # ? dont need implement abstract method
class RegularPantagon(Shape):
    def __init__(self, a):
        self.check_if_args_not_below_zero(a)
        self.a = a
        self.b = a
        self.c = a

    @abstractmethod
    def get_area(self):
        return 0.25 * pow(5 * (5 + 2 * pow(5, 0.5)), 0.5) * self.a * self.a;

    @abstractmethod
    def get_perimeter(self):
        return  self.a * 5

    @abstractmethod
    def __str__(self):
        return 'circle side is' , self.a

class EquilateralTriangle(Triangle):
    def __init__(self, a):
        self.check_if_args_not_below_zero(a)
        self.a = a
        self.b = a
        self.c = a
    # ? dont need implement abstract method

class ShapeList():
        
    def add_shape(self, shape):
        self.Shape.append(shape);
    def get_shapes_table(self):
        return self.shape;
    def get_largest_shape_by_perimeter(self):
        return 
    def get_largest_shape_by_area(self):

        return