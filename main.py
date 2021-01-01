#Object oriented programming


# get/set attribute of object: o.name
# call method: o.method()
# retrieve value from dictionary: o['my-key']
# not the same thing!
# What Can I Do With This Object?
# help(obj)
# Show help about object and methods
# dir(obj)
# List methods/attributes of object


#Classes
#Classes are like blueprints that you can use over and over
#dunder method = __init__ using double underscores has to be there
#whatever needs to be passed in goes in the ()as a paramaeter, sets up arguments but have to start with self
#first parameter will always be self = specific instance of that triangle
#self lets you set attributes, lie a = b, b = a
from math import sqrt  
##square root function, part of math module/ return sqrt line 17
from ranom import randint

class Triangle:
    "Right triangle."

    def __init__(self, a, b):
        "Create triangle from a and b sides."
        self.a = a
        self.b = b

    def get_hypotenuse(self):
        "Get hypotenuse (length of 3rd side)."
        return math.sqrt(self.a ** 2 + self.b ** 2)

    def get_area(self):
        "Get area of triangle."
        return (self.a * self.b) / 2

    def describe(self):
        return f"My area is {self.get_area()}"

#Class methods
#@classmethod decorator creating some instance like a factory method, like make a triangle for us. 
#make a random triangle, and group all the functionality together
@classmethod
def random(cls):
    print(cls

#Like in JS, classes can subclass other objects:
class ColoredTriangle(Triangle):
    """Triangle that has a color."""

    def __init__(self, a, b, color):
        # get parent class [`super()`], call its `__init__()`
        super().__init__(a, b)

        self.color = color

    def describe(self):
        msg = super().describe() + f" I am {self.color}"

  