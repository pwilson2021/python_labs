import math

print("Enter your age ?")
age = int(input())
i = 0
ans = 0

while i <= age:
    ans += i
    i += 1

months = math.ceil( ans / 12)
days =  365 * ans
hours = days * 24

print("Calculated number of years, months, days and hours")
print(ans)
print(months)
print(days)
print(hours)

