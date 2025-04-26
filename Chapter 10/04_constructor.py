class Employee:
    language = "Python" # This is a class attribute
    salary = 10000

    def __init__(self, name, salary, language): #dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod # decorator 
    def greet():
        print("Good Morning!")

Harry = Employee("Harry", 13000, "Javascript")
# Harry.name = "Harry" 
print(Harry.name, Harry.salary, Harry.language)

# Rohan = Employee()