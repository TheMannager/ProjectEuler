num1 = 1
num2 = 2
num3
total = 0
while num1+num2 < 10:
    num3 = num1 + num2
    if num3 % 2 == 0:
        total = total + num3
    num1 = num2
    num2 = num3
    num3 = 0
print(total)
