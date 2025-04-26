class Employee:
    language = "Python" # This is a class attribute
    salary = 10000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod # decorator 
    def greet():
        print("Good Morning!")

Harry = Employee()
# Harry.language = "Javascript" # This is an instance attribute
# print(Harry.language, Harry.salary)
Harry.greet()
Harry.getInfo()
