total =0
count = 0
while (count < 1000):
    if count % 5 == 0 or count % 3 == 0:
        total += count
    count = count + 1

print( total )
