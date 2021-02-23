numberList = []

print("We need 10 numbers between 1 and 8")

while len(numberList) < 10:
    userInput = int(input("Please enter a number between 1 and 8:  "))

    if userInput >= 1 and userInput <= 8:
        numberList.append(userInput)
    else:
        print("Enter a number between  1 and 8") 

print(numberList.count(5))