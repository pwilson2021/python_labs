try:
    f = open('pythonfile.txt', 'r')
    userInput = ""
    while userInput != 'end':
        f.write(userInput + '\n')
        userInput = input("Add new Line ?")
except:
    print("An error occurred ")
