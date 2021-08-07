from typing import Counter


class Book:
    #attributes, size, pages, colour, thickness ect
    #methods, turning a page, closing, opening ect

    def __init__(self, title, author, pages, current_page):
        #assingment to object attributes
        self.title = title
        self.author = author
        self.page = pages
        self.current_page = current_page
        self.bookmark = 1 #assign by default

#Q1.1
    def bookmark_page(self):
        self.bookmark = self.current_page

    # def turn_page(self):
    #     return f"Title:{self.title}, Author:{self.author}, Pages:{self.pages}"

    def turn_page(self):
            if self.current_page == self.pages -1:
                self.current_page == 1
            else: 
                self.current_page += 1

#string representation
    def __str__(self):
        return f"Title:{self.title}, Author:{self.author}"

    def __len__(self):
        return self.pages

#create a method to turn back the page
    def turn_back(self):
        self.current_page -=1

#Q1.2
    def specific_page(self):
        self.bookmark = 100
        return self.bookmark

#Q1.3
    def back_to_start(self):
        if self.current_page >= self.pages:
            self.current_page == 1
        

                 
# my_book = Book("A great book", "me", 350, 5)
# print(my_book)
# # print(my_book.bookmark) #attr
# # my_book.turn_page() #method
# my_book.bookmark_page()
# print(my_book.bookmark)
# my_book.turn_back()
# print(my_book.bookmark)
# print(my_book.specific_page())


# class Employee:
#     #attr - name, role, pay_level
#     #method - work, get_name, get_role

#     def __init__(self, name, salary, phone_number, start_date):
#         self.name = name
#         self.salary = salary
#         self.phone_number = phone_number
#         self.start_date = start_date

#     def get_employment_details(self):
#         return (self.name, self.salary, self.start_date)

#     def get_contact_details(self):
#         return(self.name, self.phone_number)

#lets create and onject of this class Employee

# employee_1 = Employee("Fran", 78000, "0401826779", "1st June 2020")
# print(employee_1.get_employment_details())
# print(employee_1.get_contact_details())

#Q2

import math
class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def calculate_area(self):
        area = self.width * self.height
        return f"The area is:{area}cm"

    def calculate_perimeter(self):
        perimeter = (self.width * 2) + (self.height * 2)
        return perimeter

    def calculate_diagonal(self):
        diagonal = math.sqrt(self.height**2 + (self.width**2)
        return diagonal

    def is_it_square(self):
        if self.width == self.height:
            return f"This is square"

my_rectangle = Rectangle(2,4)
print(my_rectangle.calculate_area())
print(my_rectangle.calculate_perimeter())
print(my_rectangle.calculate_diagonal())
