def checkArray(len, arr):
    array = [int(x) for x in arr.split(' ')]
    for i in range (1, int(len)):
        left = sum(array[0:i])
        right = sum(array[i+1:])
        
        if (left == right):
            return "YES"
    return "NO"

len = input()
arr = input()
print(checkArray(len, arr))