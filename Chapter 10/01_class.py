class Employee:
    language = "Python" # class attribute
    salary = 10000

Harry = Employee()
Harry.name = "Harry" # instance attribute
print(Harry.name, Harry.language, Harry.salary)

Rohan = Employee()
Rohan.name = "Rohan"
print(Rohan.name, Rohan.language, Rohan.salary)

# Here name is instance attribute and salary and language are class attributes as they directly belong to the class 
