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


class point(object):
    def __init__(self,x,y):
        self.__x = float(x)
        self.__y = float(y)
    def getx(self):
        return self.__x
    def gety(self):
        return self.__y
    def answer(self):
        return self.__x , self.__y

class Line(object):
    def __init__(self,from_point, to_point):
        self.__from_point = from_point
        self.__to_point = to_point
    def tpfp (self):
        return self.__from_point - self.__to_point


def func(params):
    """Function documentation:
       - What does function do?
       - What is/are expected parameter value(s)?
       - What does function return, if anything
       - Example usage"""

    pass

if __name__ == '__main__':
    main()