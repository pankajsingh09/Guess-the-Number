import random

print("Please Provide the Range ")
print("Enter the first value")
firstNo = input()
print("Enter the second value")
secondNo = input()

randNo = int(random.randint(10, 20))

print("Now Guess The no bw", firstNo, "and", secondNo)
count = 0
while True:
    userInput = int(input())
    if userInput == randNo:
        print("You have successfully guess the no in ", count+1, " Attempts")
        break

    if userInput < randNo:
        print("Your value is less than the actual no")
    else:
        print("Your value is greater than the actual no")

    count = count + 1