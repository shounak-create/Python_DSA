#Time Complexity: O(n)
#Space Complexity: O(1)
def array_sum(arr):
    sum = 0
    for i in arr:
        sum +=i
    print(sum)

Input=[3, 7, 2, 9, 4]
array_sum(Input)