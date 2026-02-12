def recursion(num):
    if  num > 5:
        return
    print(num)
    return recursion(num + 1)

# recursion(1)

def palindrome(string):
    length = len(string)
    for i in range(length // 2):
        if string[i] != string[length - 1 - i]:
            return False
    return True
