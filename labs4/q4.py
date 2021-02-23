with open('third.txt','r') as firstfile, open('fourth.txt','a') as secondfile: 
    test = firstfile.readlines()

    for line in reversed(test):
                
        secondfile.write(line)
