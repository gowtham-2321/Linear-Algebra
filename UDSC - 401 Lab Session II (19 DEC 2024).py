#Generate two lists of random integers (manually coded logic) of length 5 and calculate their dot product
'''
lst = []
lst2 = []
print("Values for the first list: ")
for i in range(1,6):
    a = int(input("Enter value number {0}:".format(i)))
    lst.append(a)
print("Values for the second list: ")
for i in range(1,6):
    a = int(input("Enter value number {0}:".format(i)))
    lst2.append(a)
dot_prod = 0
for i, j in zip(lst,lst2):
   dot_prod = dot_prod +  i*j
print("the dot product of the given list is :", dot_prod)
'''

#Ask the user for two lists of integers and compute their dot product if both lists have the same number of elements
'''
lst = []
lst2 = []

len = int(input("Enter the len of the first list: "))
len2 = int(input("Enter the len of the second list: "))
if(len != len2):
    print("the vectors are of different dimensions, so dot product cant be found")
else:
    print("Values of the first list")
    for i in range(1,len+1):
        a = int(input("Enter value number {0}:".format(i)))
        lst.append(a)
    print("Values for the second list: ")
    for i in range(1,len2+1):
        a = int(input("Enter value number {0}:".format(i)))
        lst2.append(a)
    dot_prod = 0
    for i, j in zip(lst,lst2):
        dot_prod = dot_prod +  i*j
    print("the dot product of the given list is :", dot_prod)
'''

#Write a program to compute the dot product of two vectors stored in two separate lists, where one list is all zeros
'''
lst = []
lst2 = []

len = int(input("Enter the len of the list: "))
print("Values for the first list: ")
for i in range(1,len+1):
    a = int(input("Enter value number {0}:".format(i)))
    lst.append(a)
    lst2.append(0)
dot_prod = 0
for i, j in zip(lst,lst2):
    dot_prod = dot_prod +  i*j
print("the dot product of the given list is :", dot_prod)
'''
#Create a program that calculates the dot product of two vectors containing negative numbers.
'''
lst = []
lst2 = []

len = int(input("Enter the len of the first list: "))
len2 = int(input("Enter the len of the second list: "))
if(len != len2):
    print("the vectors are of different dimensions, so dot product cant be found")
else:
    print("Values of the first list")
    for i in range(1,len+1):
        a = int(input("Enter value number {0}:".format(i)))
        lst.append(a)
    print("Values for the second list: ")
    for i in range(1,len2+1):
        a = int(input("Enter value number {0}:".format(i)))
        lst2.append(a)
    dot_prod = 0
    for i, j in zip(lst,lst2):
        dot_prod = dot_prod +  i*j
    print("the dot product of the given list is :", dot_prod)
'''

#Write a program to verify if the two vectors are orthogonal
'''
lst = []
lst2 = []

len = int(input("Enter the len of the first list: "))
len2 = int(input("Enter the len of the second list: "))
if(len != len2):
    print("the vectors are of different dimensions, so they cant be added")
else:
    print("Values of the first list")
    for i in range(1,len+1):
        a = int(input("Enter value number {0}:".format(i)))
        lst.append(a)
    print("Values for the second list: ")
    for i in range(1,len2+1):
        a = int(input("Enter value number {0}:".format(i)))
        lst2.append(a)
    dot_prod = 0
    for i, j in zip(lst,lst2):
        dot_prod = dot_prod +  i*j
    print("the dot product of the given 2 vectors is :", dot_prod)
    if(dot_prod == 0):
        print("Therefore they are orthogonal")
    else:
        print("The given vectors are not orthogonal")
'''

# Write a program to input a 3x3 matrix (as a list of lists) and a vector of length 3, then compute their product

matrix = []
lst = []
vec = []
product_list = []
print("Enter the values of the first row: ")
for j in range(0,3):
    lst = []
    print("Values for row {}:".format(i+1))
    for i in range(0,3):
        a = int(input("Enter value {} : ".format(i+1)))
        lst.append(a)
    matrix.append(lst)
print("Enter the values of the vector: ")
for i in range(0,3):
    a = int(input("Enter value {}: ".format(i+1)))
    vec.append(a)

for i in matrix:
    dot_prod = 0
    for j, k in zip(i,vec):
       dot_prod = dot_prod +  j*k
    product_list.append(dot_prod)  

print(product_list)


#Modify Problem 6 to check if the matrix columns match the vector's length. Display an error message if not.

    
