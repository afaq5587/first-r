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

key = Union [int , str]
value = Union [int , str, list, tuple, set, dict,]

data : dict[str , str] = {"fname" : "ali",
                          "name" : "danish",
                          "marks" : "hassan"
                          }
print(data["name"])

print(id("name"))



























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


# text = "air\tuniversity"
# center_text = text.expandtabs(10)
# print(center_text)
# print(text.translate)


# text = "hello\tworld"
# expanded_text = text.expandtabs(4)
# print(expanded_text)
# print(text)
                       
                       
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


