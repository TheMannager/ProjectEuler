

largest = 0
for num1 in range(100, 1000):
    for num2 in range(100, 1000):
        num3 = num1 * num2
        if str(num3) == str(num3)[::-1] and num3 > largest:
            largest = num3

print(largest)
