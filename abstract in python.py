import abc
from abc import ABC, abstractmethod

class shape(ABC):
    def area(self):
        pass

class rectangle(shape):
    def area(self):
        print("Rectangle area")


class triangle(shape):
    def area(self):
        print("Triangle area")

class square(shape):
    def area(self):
        print("Square area")

    r=rectangle()
    print(r.area())
    t=triangle()
    print (t.area())
    s=square()
    print(s.area())