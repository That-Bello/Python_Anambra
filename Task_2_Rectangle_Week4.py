# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 00:41:37 2024

TASK 2

Write a class Rectangle with methods to calculate the area and perimeter.

@author: Mr Bello
"""

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth
    
    def perimeter(self):
        return (self.length * self.breadth) * 2

    def display(self):
        print(f"The length of the rectangle is: {self.length}")
        print(f"The breadth of the rectangle is: {self.breadth}")

R_len = int(input("Enter the length of the rectangle: "))
R_bre = int(input("Enter the breadth of the rectangle: "))

rectangle = Rectangle(R_len, R_bre)
rectangle.display()
print(f"The area of the rectangle is: {rectangle.area()}")
print(f"The perimeter of the rectangle is: {rectangle.perimeter()}")
