def sum(array: list):
    sum = 0
    for i in array:
        sum += i
    return sum

def moreThan(array: list, cond: int):
    counter = 0
    for i in array:
        if i > cond:
            counter += 1
    return counter

def contains(array: list, cond: int):
    for i in array:
        if i == cond:
            return True
    return False

def index(array: list, cond: int):
    indexes = []
    for i in range(0, len(array)):
        if array[i] == cond:
            indexes.append(i)
    return indexes

def min(array: list):
    min = array[0]
    for i in array:
        if min > i:
            min = i
    return min

def max(array: list):
    max = array[0]
    for i in array:
        if max < i:
            max = i
    return max

def split(array: list):
    arr1 = []
    arr2 = []
    for i in array:
        if i > 0:
            arr1.append(i)
            continue
        arr2.append(i)
    return arr1, arr2



array = [1,2,3,3,4,5,6,7,0,-1,-3]

print(sum(array))
print(moreThan(array, 3))
print(contains(array, 3))
print(index(array, 3))
print(min(array))
print(max(array))
print(split(array))