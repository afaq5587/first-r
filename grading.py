data : list = [
    {
        "name" : "ali",
        "marks" : "45"
    },
    {
        "name" : "aslam",
        "marks" : "88"
    },
    {
        "name" : "hassan",
        "marks" : "97"
    },
    {
        "name" : "danish",
        "marks" : "29"
    }
]

def grades(marks):
    
    marks = int(marks)

    if marks < 30:
        return "fail"
    elif 30 <= marks < 45:
        return "E"
    elif 45 <= marks < 55:
        return "D"
    elif 55 <= marks < 65:
        return "C"
    elif 65 <= marks < 75:
        return "B"
    elif 75 <= marks <= 100:
        return "A"
    else:
        return "Invalid"
for students in data:
    name : str = students["name"]
    marks : int = students["marks"]    
    grade = grades(marks)
    
    print(f"Dear {name} your marks are {marks} and you grade is {grade}.")