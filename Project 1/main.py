'''
1 for snake 
-1 for water
0 for gun
'''
import random

computer = random.choice([-1, 0, 1]) 
youstr = input("Enter your choice: ")
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

you = youDict[youstr]

print(f"You chose: {reverseDict[you]}\nComputer choice: {reverseDict[computer]}")

if you == computer:
    print("Draw")
else:
    if(computer == -1 and you == 1):
        print("You win")
    elif(computer == -1 and you == 0):
        print("You lose")

    elif(computer == 1 and you == -1):
        print("You lose")
    elif(computer == 1 and you == 0):
        print("You win")

    elif(computer == 0 and you == -1):
        print("You lose")
    elif(computer == 0 and you == 1):
        print("You win")
    else:
        print("Invalid input")
# The above code is a simple game where the user can choose between snake, water, or gun.