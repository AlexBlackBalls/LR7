import random 

def lst1(n):
    return list(range(n))

def lst2(n):
    return [random.randint(0, 10) for _ in range(n)]

def lst3(n):
    return n.split()



print(lst1(int(input())))
print(lst2(int(input())))
print(lst3(input()))


