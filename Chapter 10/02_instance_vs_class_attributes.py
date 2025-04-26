class Employee:
    language = "Python" # This is a class attribute
    salary = 10000

Harry = Employee()
Harry.language = "Javascript" # This is an instance attribute
print(Harry.language, Harry.salary)
