#Object oriented programming

#Classes
#Classes are like blueprints that you can use over and over
#dunder method = __init__ using double underscores has to be there
#whatever needs to be passed in goes in the ()as a paramaeter, sets up arguments but have to start with self
#first parameter will always be self = specific instance of that triangle
#self lets you set attributes, lie a = b, b = a
from math import sqrt  ##square root function, part of math module/ return sqrt line 17
from ranom import randint

class Triangle:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
    def get_hypotenuse(self):
        return sqrt(self.a ** 2 + self.b ** 2)

    def get_area(self):
        return = self.a * self.b / 2