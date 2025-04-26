marks = int(input("Enter your marks: "))

if(marks<=100 and marks>=90):
    print("You got A+ grade")
elif(marks<90 and marks>=80):
    print("You got A grade")
elif(marks<80 and marks>=70):
    print("You got B grade")
elif(marks<70 and marks>=60):
    print("You got C grade")
elif(marks<60 and marks>=50):
    print("You got D grade")
elif(marks<50):
    print("You got E grade")