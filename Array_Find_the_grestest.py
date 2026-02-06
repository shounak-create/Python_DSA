input = [3, 7, 2, 9, 4]
greatest = input[0]
for i in input:
    if i > greatest:
        greatest = i
    else:
        continue

print(greatest)