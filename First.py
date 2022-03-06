# print("Hello")
# firstname = "Tony "
# lastname = " Stark "
# fullname = firstname + lastname
# print(fullname)

# age = 47

# genius = True

# print(age)
# print(genius)

# name = input("What is your Age")
# myname = int(name) + 2
# print(myname)

# first = input("Enter Your First No")
# second = input("Enter second No")
# total = int(first) + int(second)
# print(" the sum of no is" + str(total))

from ast import Num, operator
from importlib.util import find_spec
from tokenize import String
from unicodedata import name

#String
name = "Muhammad Ahsan"
# print(name.upper())
# print(name.find('A'))

# # it colud not change original string
# print(name.replace("Ahsan", "Ehsan"))

# print(name)
# print("Ahsan" in name)
# print("Ali" in name)

# #Oprators
# print(5**2)
# print(2 + 2 * 3 / 2)

#Comments

# Comments start  in Python with # tag

# Comaprison Oprator

# print(3 < 4)
# print(2 < 1)
# print(2 != 2)

# Logical Oprator Or  (Both False then False otherwise True) , And (Both true then true ) Operator , not  opertor

# print(3 > 4 or 4 > 5)

# print(3 < 4 and 4 < 5)

# print(not 3 > 2)

# If Else Statements

# age = int(input("Enter Your Age"))
# if age >= 18:
#     print("you are adult")
#     print("You can Vote")
# elif age < 20 and age > 5:
#     print("you are in school")
# else:
#     print("You are Child")

# Design a Calculator using Pyhton

# first = input("Enter First No : ")
# operator = input("Enter Operator (+ , - , / , %) : ")
# second = input("Enter second No : ")

# first = int(first)
# second = int(second)

# if operator == "+":
#     print(first + second)

# elif operator == "-":
#     print(first - second)

# elif operator == "*":
#     print(first * second)

# elif operator == "/":
#     print(first / second)

# elif operator == "%":
#     print(first % second)
# else:
#     print("Enter Valid Value")

# Range

# print(range(5))

# loops in python

# i = 1
# while i <= 10:
#     print(i * "*")
#     i = i + 1

# i = 5
# while i >= 0:
#     print(i * "*")
#     i = i - 1

#For loop

# for item in range(5):
#     print(item +2)

# data Types in Python

# marks = [
#     1,
#     4.2,
#     "Ali",
#     False,
# ]

# print(marks[1:3])
# for list in marks:
#     print(list)

# marks = [
#     1,
#     4.2,
#     "Ali",
#     False,
# ]
# marks.append("Muhamad")
# print(marks)

# marks.insert(3, 100)
# print(marks)

# print(100 in marks)
# print(len(marks))

# List i=using While Loop

# i = 0
# while i < len(marks):
#     print(marks[i])
#     i = i + 1

# marks.clear()
# print(marks)

# students = ["muhammad", "Ahsan", "Ali", "raza"]
# for item in students:
#     if item == "Ali":
#         continue
#     print(item)

# Tuple: inmutable

# std = ("muhammad", "Ahsan", "Ali", 12, 13, 12)
# print(std)
# # std[0]=43
# # print(std)
# print(std.count(12))

#set

# unique values store in set

# std = {"muhammad", "Ahsan", "Ali", 12, 13, 12}
# # print(std)
# for score in std:
#     print(score)

#Dictionary

# std = {"muhammad": 50, "Ahsan": 43, "Ali": 122}
# print(std)
# std["math"]=100;
# print(std)

# Functions in Python
# inbuild , Module, User-Defined,
# import math

# print(dir(math))

from math import sqrt
print(sqrt(16))
 