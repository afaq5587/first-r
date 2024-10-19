# a = int ("67")
# b = 87
# print(type(b))
# print(a+b)

# name = input("Enter your name;")
# print("Welcome" , name)
# name = input("enter name")
# age = input("enter your age")
# study = input("enter your study")

# print("name =" , name)
# print("age" , age)
# print("study" , study)
# name = input("enter name;  ")
# age = input("enter your age;  ")
# study = input("enter your study;  ")

# print("name =", name)
# print("age", age)
# print("study", study)

# num1 = int(input("enter two numbers; "))
# num = int(input("enter second number; "))
# print("sum =" ,num1 + num)

# side = int(input("enter the square side;  "))
# print("square =" , side ** 2)

# a = float(input("enter a number; "))
# b = float(input("enter second number; "))
# print ("avg = ", a+b/2)

# IF AND ELIF AND ELSE STATEMENTS

# play = str(input("lets play game choose number which is not greater than first number; "))
# a = int(input("enter a number; "))
# b = int(input("enter second number; "))
# print(a >= b)
# if(a >= b):
#   print("well done")
# # 
# #   SPACE after if and before print called indentation
# elif(a<=b):
#     print("try again")


# a =str ("afaq")
# b = str("latif")
# final = (a +" " + b)
# print(final)
# print(len(final))


# indexing
# name = str("afaq latif")
# a = name[4] , name[6], name[3]
# print(a)

# slicing
# name = str("afaq latif")
# c = name[2 :5]
# b = name[:6]
# a = name[1 : len(name)]
# print(a)
# print(b)

# STRING FUCTIONS
# str.endswith()
# name = str("my name is afaq")
# print(name.endswith("aq"))
# print(name.endswith("na"))

# name = str("my name is afaq")
# print(name.capitalize())

# name = str("my name is afaq")
# print(name.replace("a" , 'b'))

# name = str("my name is afaq")
# print(name.find("m"))

# name = str("my name is afaq")
# print(name.count("a"))

# practice
# name = str(input("enter your first name;  "))
# print(name)
# print(len(name))

# LISTS
# marks = [23, 44, 45, 5, 2, 5,]
# print(marks)
# print(len(marks))
# print(type(marks))
# print(marks[4])

# SLICING
# marks = [23, 44, 45, 5, 2, 5,]
# new = marks[1 : 4]
# print(new)

# marks = [23, 44, 45, 5, 2, 5,]
# result = marks[  : 5]
# print(result)

# LIST METHODS
# APPEND METHOD
# marks = [23, 44, 45, 5, 2, 5,]
# marks.append(5)
# print (marks)
# sorting    change in to assending order
# marks = [23, 44, 45, 5, 2, 5,]
# marks.sort()
# print(marks)

# desending sorting
# marks = [23, 44, 45, 5, 2, 5,]
# marks.sort(reverse = True)
# print(marks)

# reverse
# marks = [23, 44, 45, 5, 2, 5,]
# marks.reverse()
# print(marks)

# insert
# marks = [23, 44, 45, 5, 2, 5,]
# marks.insert(1 , 6)
# print(marks)
# marks = [23, 44, 45, 5, 2, 5,]
# marks.insert(4 , 76)
# print(marks)

# remove
# marks = [23, 44, 45, 5, 2, 5,]
# marks.remove(44)
# print(marks)

# pop
# marks = [23, 44, 45, 5, 2, 5,]
# marks.pop(3)
# print(marks)

# TUPLES
# tup =(2 ,4, 6, 7 , 8 , 4)
# print(tup.index(4))
# print(tup.count(4))
# ...................................
# FUNCTION IN PYTHON



# I/O FUCTIONS
# f = open("python.py", "r")
# data = f.read()
# print(data)
# f.close
    
# ............................................................................
# OOPS IN PYTHON

# class Student:
#     name = "danish"

# s1 = Student()
# print(s1.name)

# s2 = Student()
# print (s2.name)

# -------------==========------====================================================

# DICTIONAY  

# key = Union [int , str]
# value = Union [int , str, list, tuple, set, dict,]

# data : dict[str , str] = {"fname" : "ali",
#                           "name" : "danish",
#                           "marks" : "hassan"
#                           }
# print(data["name"])

# print(id("name"))



























# class Student:
    
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#         print("adding new value in database")


# s1 = Student("daninsh", 73)
# print(s1.name,s1.marks)

# s2 = Student("ali", 67)
# print(s2.name, s2.marks)



# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks =marks

#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("hi ", self.name, "your avg score is:", sum/3)

# s1 = Student("afaq latif ", [45, 65, 12] )
# s1.get_avg()

# @staticmethod

# -============================================ =================================================

# a = int (34)
# b = int (23)
# sum = a + b
# divide = a / b
# subtraction = a - b
# multiply = a * b
# modulo = a % b
# exponential = a ** b

# print(sum)
# print(divide)
# print(subtraction)
# print(multiply)
# print(exponential)
# print(modulo)




# def sum(num1, num2):
#     print(num1 + num2)
    
# def sub(num1, num2):
#     print(num1 - num2)
    
# def multiply(num1, num2):
#     print(num1 * num2)
    
# def divide(num1, num2):
#     print(num1 / num2)

# def operator(operator):
#     num1: int = int(input("Enter first value: "))
#     num2: int = int(input("Enter second value: "))
    
#     if operator == "sum":
#         sum(num1, num2)
#     elif operator == "sub":
#         sub(num1, num2)
#     elif operator == "multiply":
#         multiply(num1, num2)
#     elif operator == "divide":
#         divide(num1, num2)

# operation = input("Which operation you want to do 'sum, sub, multiply, divide': ")

# operator(operation)
# ================================================================================================================  

# text = "air\tuniversity"
# center_text = text.expandtabs(10)
# print(center_text)
# print(text.translate)


# text = "hello\tworld"
# expanded_text = text.expandtabs(4)
# print(expanded_text)
# print(text)
 
# ================================================================================================================                       
# name : str = input("Enter your name : ")
# percent = int(input("Enter your marks percentage : "))


# if percent < 30:
#     grade = "fail"
# elif 30 <= percent < 45:
#     grade = "E"
# elif 45 <= percent < 55:
#     grade = "D"
# elif 55 <= percent < 65:
#     grade = "C"
# elif 65 <= percent < 75:
#     grade = "B"
# elif 75 <= percent <= 100:
#     grade = "A"
# else:
#     grade = "Invalid percentage"
                     
                             
# print(f"Dear {name} your grade is {grade} keep it up : ")

#---------------------------- ___________________________________________________________________________________________________________---


# a : int = 45
# b : int = 23

# a , b = b , a
# print(a , b)





# numbers :list[str] = ["45", "23" , "67" , "89", "12"]
# print(numbers[0:4:3])

# no :list[str] = [1,2,3,4,5,6,7,8,9,10], [3,5,7,9,11,13,15,17,19,21]
# print(no[::-1])

# students : list[str] = [[[["ali", "danish"], [ "abnd", "dfj"]],["12","56"],["ddfggh","por"]],["ip","eyiu"]]
# print(students[0][2])




# ==================================================================================================================
# list 
# marks :list[int] = [23, 44, 45, 5, 2, 5,]
# print(max(marks))
# print(min(marks))
# print(sum(marks))
# for mark in marks:
#     print(mark)

# numbers = list(range(1,8))
# print(numbers)
# for i in range(23, 98):
#     print(i)
# ==================================================================================================================
# LIST COMPREHENSION...
# a = [i ** 3 for i in range (1 , 10)]
# print(f"cube of value from 1 to 10 is : {a}")
# a = 2 ** 3
# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
# for requested_topping in requested_toppings:
#     print(f"Adding {requested_topping}.")
# print("\nFinished making your pizza!")


# user_0 = {
#     'username': 'efermi',
#     'first': 'enrico',
#     'last': 'fermi',
#     }
# user_1 = user_0.get('fname' , 'unknown')
# print(user_0)
# for key,value in user_0.items():
#     print(key, value)

# =======================================================================
# l1 :list[str] = [1,2,3,4,5,6]

# for l in l1:
#     print(l)

# l2 : str = "pakistan"
# for l3 in l2:
#     print(f"characters : {l3}")
# import sys
# a : dict[str, str] = {"name" : "afaq" , "school" : "high public"}
# for k in a:
#     print(f"keys are {k} and values are {a[k]}")

# ======================================================================================
# INPUT FUNCTION (SYS.ARGV)
# import sys

# print("abnsndhddh")
# print("jakakak")

# print(sys.argv)

# ask : str = input("Did you want to eat pizza:  ")

# index : int = 0
# while index <= 5:
#     if ask == "yes":
#         print(f"your pizza is getting ready plz pay for it")
#     index += 1
#     if index <= 5:
#         break
        














# squares : list[int] = [x**2 for x in range(1,50)]
# print(squares)

# msg :list = ["ali", "danish", "aslam", "evi"]

# for message in msg:
#     print(f"hi {message.title()} , you're invited in our party!.")
    


# coordinates : tuple[int,int] = (10, 20, 15)
# print(coordinates)  # Output: (10, 20)

# n:int = int(input("Enter a number: "))

# for i in range(1, 11):
#     for n in range(1, 11):
#         print(f"{i} x {n} = {i * n}")
    
    
    # print(f"{n} x {i} = {i * n}")



# for i in range(2, 11):
#     for n in range(1, 11):
#         print(f"{i} x {n} = {i * n}")
#     print("next table")

# data : dict = {
#     'name' : 'saad',
#     'age' : '19',
#     'city' : 'kahuta'
    
# }
# for i in data:
#     print(f"His {i} is {data[i]}")
    
# for key,value in data.items():
#     # print(f"{key}: {value}")
#     print(key)
#     print(value)

 # Make 30 green aliens.
# aliens = []
# for alien_number in range (30):
#    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#    aliens.append(new_alien)
# for alien in aliens[:3]:
#    if alien['color'] == 'green':
#        alien['color'] = 'yellow'
#        alien['speed'] = 'medium'
#        alien['points'] = 10
#  # Show the first 5 aliens.
# for alien in aliens[:5]:
#    print(alien)
# print("...")


# prompt = "\nDid you want to order pizza:"
# prompt += "\nEnter 'stop' if there is enough pizzas for you. "
# message : int | str = ""
# while message != 'stop':
#    message = input(prompt)
#    print(message)
# FUNCTIONS


# def myfunction(num1: int , num2 : int):
#     return (num1 , num2)   
# print(myfunction(67 , 78))

# LAMBDA AND MAP AND FILTER

# data : list[int] = [1,2,3,4,5,6,7,8,9]
# data = list(filter(lambda x:x%2==0 ,data))

# print(data)

# def addition(first_number:int, second_number:int)->int:
#     result : int = first_number + second_number
#     return result


# print(addition(5, 8)) # Output: 13
# # Can also do like this
# get_sum : int = addition(5,8)
# print(get_sum) 

# 

# def factorial(n):
#     if n < 0:
#         return None
#     if n < 2:
#         return 1
#     else:
#         result = 1
#         for i in range(2,n+1):
#             result *= i
#         return result
# print(factorial(5))

students_data = [
    {
        'name': 'John Doe',
        'marks': {
            'Math': 85,
            'English': 90,
            'Science': 78
        }
    },
    {
        'name': 'Jane Smith',
        'marks': {
            'Math': 75,
            'English': 82,
            'Science': 89
        }
    },
    {
        'name': 'Emily Davis',
        'marks': {
            'Math': 93,
            'English': 87,
            'Science': 85
        }
    },
    {
        'name': 'Michael Brown',
        'marks': {
            'Math': 65,
            'English': 70,
            'Science': 60
        }
    },
    {
        'name': 'Chris Johnson',
        'marks': {
            'Math': 88,
            'English': 85,
            'Science': 90
        }
    }
]

def grades(total):
    if total < 30:
        return "fail"
    elif 30 <= total < 45:
        return "E"
    elif 45 <= total < 55:
        return "D"
    elif 55 <= total < 65:
        return "C"
    elif 65 <= total < 75:
        return "B"
    elif 75 <= total <= 100:
        return "A"
    else:
        return "Invalid"

for student in students_data:
    sum = student["marks"]["Math"] + student["marks"]["English"] + student["marks"]["Science"]
    name = student["name"]
    total = sum * 100 / 300
    grade = grades(total)
   
    print(f"Dear {name}, your total marks are {sum} and your grade is {grade}. Keep it up!")
