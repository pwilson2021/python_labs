testList = [1, 4, 9, 16, 25] 
list2 = []

[list2.append(e) for e in testList if e % 2 != 0]

print(list2)