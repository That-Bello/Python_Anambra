# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 00:41:37 2024

PROJECT

Library Management System: 
Create a library management system where users can add books, borrow books, 
and return books. Each book should have a title, author, and availability status. 
Use classes to represent books and the library.

@author: Mr Bello
"""

import sys

class LMS:
    def __init__(self, booklist, name):
        self.booklist = booklist
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"Available Books in Our Library 👆🏼: {self.name}")
        print("===============")
        for book in self.booklist:
            print(book)

    def lendBook(self, user, book):
        if book not in self.lendDict:
            self.lendDict[book] = user
            print("Lender Book Database has been updated. The book is avaiable now.")
        else:
            print(f"The book is still in use by {self.lendDict[book]}")

    def addBook(self, book):
        self.booklist.append(book)
        print(f"The book(s) '{book}' has been added to the library.")

    def returnBook(self, book):
        if book in self.lendDict:
            del self.lendDict[book]
            print(f"The book '{book}' has been returned.")
        else:
            print(f"The book '{book}' was not borrowed.")

if __name__ == "__main__":
    Private_LMS = LMS(["The Monsters", "Euphoria", 
                       "Station Eleven", "Wonderland",
                       "Big Ben", "World of Diamond"], "Private")
    while True:
        print(f"Welcome to {Private_LMS.name} Library.")
        print("===============| Main Menu |==============")
        print("1. Display Books List")
        print("2. Lend Book(s)")
        print("3. Add Book(s) to List")
        print("4. Return Book(s) to Library")
        print("")
        print("Enter your choice below 👇🏼 ===============")
        
        user_choice = input()
        if user_choice not in ["1", "2", "3", "4"]:
            print("Not a valid option!")
            continue
        else:
            user_choice = int(user_choice)
        
        if user_choice == 1:
            Private_LMS.displayBooks()
        elif user_choice == 2:
            book = input("Enter the title of the book to lend: ")
            user = input("Enter your name: ")
            Private_LMS.lendBook(user, book)
        elif user_choice == 3:
            book = input("Enter the title of the book to add: ")
            Private_LMS.addBook(book)
        elif user_choice == 4:
            book = input("Enter the title of the book to return: ")
            Private_LMS.returnBook(book)
        
        print("Press 'q' to Quit or 'c' to Continue!")
        
        user_choice2 = ""
        while user_choice2 not in ["c", "q"]:
            user_choice2 = input()
            if user_choice2 == "q":
                print("Thank you, bye 🙋🏼‍! ")
                sys.exit()
            if user_choice2 == "c":
                continue








