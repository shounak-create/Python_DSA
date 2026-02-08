def even_numbers(arr):
    total = 0
    for  i in arr:
        if i%2==0:
            total +=1
    return total

print(even_numbers([3, 7, 2, 9, 4, 6]))