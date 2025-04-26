class Employee:
    a = 1

    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

   
e = Employee()
e.a = 45

e.name = "Harry khan"
print(e.name)

e.show() # Prints the instance value of a