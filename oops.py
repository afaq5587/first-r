# class Teacher():
#     def __init__(self, teacher_id: str , teacher_name: str)->None:
#         self.teacher_id = teacher_id
#         self.teacher_name = teacher_name
#         self.organization_name = "piaic"
        
#     def teaching(self, subject: str)->str:
#         print(f"{self.teacher_name} is teaching {subject}....")
        
# obj1 : Teacher = Teacher(1,"sir zia")
# obj2 : Teacher = Teacher(2,"qasim")

# print(obj1.teaching("genrative Ai"))

# class Student():
#     teacher : str = "sir qasim"
#     def __init__ (self, student_name, student_marks)-> None:
#         self.student_name = student_name
#         self.student_marks = student_marks
        
#     def subject(self, subject:str)-> None:
#         print(f"{self.student_name} contain marks in {subject} ")
        
#     def detail(self)-> None:
#         info = (f"""
# teacher name is {Student.teacher} and student name is {self.student_name}""")
#         print(info)
# student1 :Student = Student("ali", 89)

# print(student1.subject("AI"))

# print(Student.teacher)
# print(student1.detail())



# class Mother:
#     def __init__ (self, name :str)-> None:
#         self.name : str = name
#         self.eyecolor : str = "blue"
        
#     def speak (self, speaking: str)-> None:
#         return(f"Mother speaking function : {speaking}")

# class Father:
#     def __init__ (self, name: str)-> None:
#         self.name : str = name
#         self.height  = "6 feet"
#     def speak (self, speaking: str)-> None:
#         return(f"FAther speaking function : {speaking}")   
# class Child(Mother, Father ):

#     def __init__ (self, mother_name: str, father_name: str, child_name: str ):
#         Mother.__init__ (self, mother_name)
#         Father.__init__(self, father_name)
#         self.child_name : str = child_name
        
# afaq : Child = Child("heba noor", "m.latif", "m.afaq")

# print(f"afaq height is {afaq.height}")
# print(f" afaq eye color is {afaq.eyecolor}")
# print(afaq.speak("pakistan zinda bad"))



# class Complex:
#     def __init__ (self, real , img)->None:
#         self.real = real
#         self.img = img
    
#     def shownum (self):
#         print(self.real, "i -" , self.img , "j")
        
#     def __sub__ (self, num2):
#         newreal = self.real - num2.real
#         newimg = self.img - num2.img
#         return Complex(newreal, newimg)
    
# num1 : Complex = Complex(1, 3)
# num1.shownum()
    
# num2 = Complex(2, 4)
# num2.shownum()
    
# num3 = num1 - num2
# num3.shownum()
    

        
# class Complex:
#     def __init__ (self, real , img)->None:
#         self.real = real
#         self.img = img
    
#     def shownum (self):
#         print(self.real, "i +" , self.img , "j")
        
#     def __add__ (self, num2):
#         newreal = self.real + num2.real
#         newimg = self.img + num2.img
#         return Complex(newreal, newimg)
    
# num1 : Complex = Complex(1, 3)
# num1.shownum()
    
# num2 = Complex(2, 4)
# num2.shownum()
    
# num3 = num1 + num2
# num3.shownum()




# NUMPY

import numpy as np

from nptyping import NDArray
   
state_bank : NDArray[Shape["4"], Any] = np.array([1,2,3,43,])
new = state_bank % 2 ==0
print(new)


# import json

# # a Python object (dict):
# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }

# # convert into JSON:
# y = json.dumps(x)

# # the result is a JSON string:
# print(y)


























