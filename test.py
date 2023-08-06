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

# test










