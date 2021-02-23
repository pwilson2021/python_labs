a, b, c = 0, 1, 0

while c < 20:
    a, b =  b, a + b
    print(b)
    c += 1

print(c)