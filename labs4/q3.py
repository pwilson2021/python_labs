with open('first.txt','r') as firstfile, open('second.txt','r') as secondfile, open('third.txt', 'a') as thirdfile:

        for line in firstfile:
                for line2 in secondfile:
                        thirdfile.write(line)
                        thirdfile.write(line2)
