print("hello world")
print("happy new year")

# sort a list
a = [1, 3, 2, 4, 5]
a.sort()
print(a)

print("hello world!!")
print("happy new year")

print("Merry Christmas")

# do a bubble sort in a list of 10 random numbers
import random
def random_list(n):
    a = []
    for i in range(n):
        a.append(random.randint(0,100))
    return a
def bubble(a):
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
    return a
ran=random_list(10)
print(ran)
print(bubble(ran))
print("Hello World!!")
# Path: test.py
# search a number from a list with 10 random numbers
import random
def random_list(n):
    a = []
    for i in range(n):
        a.append(random.randint(0,100))
    return a
def search(a, n):
    for i in range(len(a)):
        if a[i] == n:
            return i
    return -1
ran=random_list(10)
print(ran)
print(search(ran, 10))

print("Hello World!!")
# Path: test.py
# search a number from a list with 10 random numbers

print("sort and binary search")
# using sort and binary search
import random
def random_list(n):
    a = []
    for i in range(n):
        a.append(random.randint(0,100))
    return a
def search(a, n):
    a.sort()
    print(a)
    low = 0
    high = len(a)-1
    while low <= high:
        mid = (low + high) // 2
        if n == a[mid]:
            return mid
        elif n > a[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1
ran=random_list(10)
print(ran)
print(search(ran, 10))

# do a binary search
print("binary search")
import random
def random_list(n):
    a = []
    for i in range(n):
        a.append(random.randint(0,100))
    return a
def search(a, n):
    low = 0
    high = len(a)-1
    while low <= high:
        mid = (low + high) // 2
        if n == a[mid]:
            return mid
        elif n > a[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1
ran=random_list(10)
print(ran)
print(search(ran, 10))


# do a quick sort
print("quick sort")
import random
def random_list(n):
    a = []
    for i in range(n):
        a.append(random.randint(0,100))
    return a
def quick(a):
    if len(a) <= 1:
        return a
    pivot = a[len(a)//2]
    left = []
    right = []
    equal = []
    for i in a:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
        else:
            equal.append(i)
    return quick(left) + equal + quick(right)

ran=random_list(10)
print(ran)
print(quick(ran))
print("end of quick sort")
print("ending")






#




