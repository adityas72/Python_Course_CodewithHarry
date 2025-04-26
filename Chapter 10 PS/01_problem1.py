class Programmer:
    company = "Google"  
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = Programmer("Harry", 100000, 1234)
print(p.name, p.salary, p.pin, p.company) 
