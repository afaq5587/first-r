# def sum(a, b):
#     print(a + b)
# def multiply(a , b):
#     print(a * b)
# def divide(a , b):
#     print(a / b)
# def sub(a , b):
#     print(a - b)
# def modulo(a , b):
#     print(a % b)
# def exponential(a , b):
#     print(a ** b)

# def operator(operator):
#     a = int(input("Enter first value: "))
#     b = int(input("Enter second value: "))

#     if operator == "sum":
#          sum(a , b)
#     elif operator == "divide":
#         divide(a , b)
#     elif operator == "multiply":
#         multiply(a, b)
#     elif operator == "sub":
#         sub(a, b)
#     elif operator == "modulo":
#         modulo(a, b)
#     elif operator == "exponential":
#         exponential(a, b)

# operation = input("which operation did you want to operate 'sum, multiply, divide , modulo, exponential, sub':   ")


# operator(operation)      


# text = "hello"
# centered_text = text.center(10 , "*")
# print(centered_text)



# text = "hello"
# centered_text = text.center(25, "q")
# print(centered_text)

# text = "hello"
# a = text.count("l")
# print(a)

# text = "hello"
# encoded_text = text.encode("utf-8")
# print(encoded_text)  # Output: b'hello')


# from typing import Union
# pertype =Union[float,int]

# percentage :list[int] = [56, 78 ,89 , 98 ,12, 45]
# names :list = ["afaq", "hassan" , "danish" ,"ali" , "saad", "awais" ]

# grades :list[str] = []


# for percent in percentage:
#     garde : str = ""
    
#     if percent < 30:
#          grade = "fail"
#     elif 30 <= percent < 45:
#         grade = "E"
#     elif 45 <= percent < 55:
#         grade = "D"
#     elif 55 <= percent < 65:
#         grade = "C"
#     elif 65 <= percent < 75:
#         grade = "B"
#     elif 75 <= percent <= 100:
#         grade = "A"
#     else:
#         grade = "Invalid percentage"
    
#     grades.append(grade)
    
   
# new = list(zip(percentage,grades, names))   
# print(percentage)

# print(grades)    

# print(new)



# from typing import Union
# percenttype = Union[float , int]

# percentage : list[int] = [34, 56, 78, 98,45 ,12]
# names :list = ["afaq", "hassan" , "danish" ,"ali" , "saad", "awais" ]

# grades : list[str] = []

# for percent in percentage:
#     grade :str = ""

#     if percent < 30:
#         grade = "fail"
#     elif 30 <= percent < 45:
#         grade = "E"
#     elif 45 <= percent < 55:
#         grade = "D"
#     elif 55 <= percent < 65:
#         grade = "C"
#     elif 65 <= percent < 75:
#         grade = "B"
#     elif 75 <= percent <= 100:
#         grade = "A"
#     else:
#         grade = "Invalid percentage"
    
#     grades.append(grade)
    
# print("Students NAMES , PERCENTAGE and GRADES are here bellow:  ")
# function =(list(zip(names, percentage, grades)))
# print(function)

user_name : str = input("Enter your user name: ")
password : str = input("Enter your password:  ")


if user_name == "admin" and password == "admin":
    print("otp sent to you")
    otp : str = input("Enter otp:   ")
    
    if otp == "123" :
        print("welcome to our webside")
        
else:
    print("nvalid user_name or password")

























