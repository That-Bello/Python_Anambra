# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 00:41:37 2024

TASK 1

Create a class Person with attributes name and age. 
Add a method to display the person's details.

@author: Mr Bello
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myFunc(self):
        print(f"The person's name is {self.name}, at {self.age} years of age")

data1 = Person("Charles", 34)
data2 = Person("Aisha", 25)

data1.myFunc()
data2.myFunc()