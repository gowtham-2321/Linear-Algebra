#question 1
lst= []
for i in range(1,6):
    a = int(input("enter no. "))
    lst.append(a)
print(lst)

#question 2
lst= []
for i in range(1,11):
    a = int(input("enter no. "))
    lst.append(a)
print(lst[::-1])

#question 3
lst = []
while(True):
    a = int(input("enter a number to append: "))
    if(a == -1):
        break
    lst.append(a)
print(lst)

#question 4
str = input("enter a comma sperated string of numbers: ")
lst = []
lst = str.split(",")
numlst = []
for i in lst:
    numlst.append(int(i))
print(numlst)

#question 5
lst = []
for i in range(1,21):
    lst.append(i)
print(lst)

#question 6
lst = []
for i in range(1,11):
    lst.append(i**2)
print(lst)

#question 7
lst = []
for i in range(2,22,2):
    lst.append(i)
print(lst)

#question 8
lst = []
for i in range(1,11):
    lst.append(int(input("enter values: ")))
evelst = []
for i in lst:
    if(i%2 == 0):
        continue
    evelst.append(i)
print(evelst)

#question 9 
lst = []
for i in range(10,55,5):
    lst.append(i)
print(lst)

#question 10
def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    return fib(n-1) + fib(n-2)

a = int(input("ENTER THE NUMBER OF TERMS YOU WANT IN FIB LIST: "))
lst = []
for i in range(1,a+1):
    lst.append(fib(i))
print(lst)

#question 11
def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)

lst = []
for i in range(0,10):
    lst.append(fact(i))
print(lst)

#question 12
lst = []
for i in range(2,51):
    lst.append(i)

for i in lst:
    for j in lst:
        if (i != j and j%i == 0):
            lst.remove(j)
print(lst)

#question 13
a = int(input("enter the length of the vector1: "))
lst1 = []
for i in range(a):
    lst1.append(int(input("enter the component of the vector1: ")))
b = int(input("enter the length of the vector2: "))
lst2 = []
for i in range(b):
    lst2.append(int(input("enter the component of the vector2: ")))
dot_prod = 0
for i in range(a):
    dot_prod = dot_prod + lst1[i]*lst2[i] 
print(dot_prod)

#question 14
a = int(input("enter the length of the vector1: "))
lst1 = []
for i in range(a):
    lst1.append(int(input("enter the component of the vector1: ")))
b = int(input("enter the length of the vector2: "))
if(a != b):
    print("cant add vectors of two different dimensions")
else:
    lst2 = []
    for i in range(b):
        lst2.append(int(input("enter the component of the vector2: ")))
    dot_prod = 0
    for i in range(a):
        dot_prod = dot_prod + lst1[i]*lst2[i] 
    print(dot_prod)

#question 15
a = 3
lst1 = []
for i in range(3):
    lst1.append(int(input("enter the component of the vector1: ")))
lst2 = []
for i in range(3):
    lst2.append(int(input("enter the component of the vector2: ")))
dot_prod = 0
for i in range(3):
    dot_prod = dot_prod + lst1[i]*lst2[i] 
print(dot_prod)