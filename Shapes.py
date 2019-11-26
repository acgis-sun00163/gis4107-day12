# -*- coding: UTF-8 -*-
# ------------------------------------------------------------------------------
# Name:        exercise_template.py
#
# Purpose:     Brief desciption of what module does
#
# Usage:       Module name and required/optional command-line parameters (if any)
#
# Author:      Your name(s)
#
# Created:     dd/mm/yyyy
# ------------------------------------------------------------------------------
def main():
    pass

import math

class Circle (object):
    def __str__ (self):
        return "Circle area with a radius of {} is {}".format(self.__radius,self.area)
    @property
    def area(self):
        return self.__radius**2*math.pi

    @property
    def radius(self):
        ''''''

    @radius.setter
    def radius(self,radius):
        self.__radius= radius


class Square (object):
    def __str__ (self):
        return "Square area with a side of {} is {}".format(self.__length,self.area)
    @property
    def length(self):
        ''''''

    @length.setter
    def length(self,length):
        self.__length= length

    @property
    def area(self):
        return self.__length**2


class Rectangle(object):
    def __str__ (self):
        return "Rectangle area with a width of {} and height of {} is {}".format(self.__width, self.__length,self.area)
    @property
    def length(self):
        ''''''

    @length.setter
    def length(self,length):
        self.__length= length

    @property
    def width(self):
        ''''''

    @width.setter
    def width(self,width):
        self.__width= width

    @property
    def area(self):
        return self.__length*self.__width











def func(params):
    """Function documentation:
       - What does function do?
       - What is/are expected parameter value(s)?
       - What does function return, if anything
       - Example usage"""

    pass

if __name__ == '__main__':
    main()
