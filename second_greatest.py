#Problem: Find the greatest in the array
#Approach: Linear Scan
#time Complexity: 0(n)
#Space complexity: o(n)

def second_largest(arr):
    largest = arr[0]
    second = float('-inf')

    for i in arr:
        if i > largest:
            second = largest
            largest = i
        elif i > second and i != largest:
            second = i

    return second


print(second_largest([3, 7, 2, 9, 4]))
