total = 0
count = 0
while count < 1000:
    if count % 3 == 0 or count % 5 == 0:
        total = total + count
    count = count + 1
print(total)
