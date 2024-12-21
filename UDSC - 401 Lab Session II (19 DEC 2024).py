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
'''
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
'''

#Modify Problem 6 to check if the matrix columns match the vector's length. Display an error message if not.
'''
matrix = []
vec = []
lst=[]
numlst= []

for i in range(3):
    row = input("Enter the values of the row, seperated by a comma: ")
    lst = row.split(",")
    numlst =[]
    for i in lst:
        numlst.append(int(i))
    matrix.append(numlst)

for i in range(0,3):
    a = int(input("Enter value {}: ".format(i+1)))
    vec.append(a)

if len(vec) != len(numlst):
    print("cant multiply the matrix with the given vector!")
else:
    product_lst = []
    for i in matrix:
        dot_prod = 0
        for j, k in zip(i,vec):
            dot_prod = dot_prod +  j*k
        product_lst.append(dot_prod)  

    print(product_lst)
'''

#Write a program to multiply a 2x2 matrix by a 2-dimensional vector input by the user.
'''
matrix = []
vec = []
lst=[]
numlst= []

for i in range(2):
    row = input("Enter the values of the row, seperated by a comma: ")
    lst = row.split(",")
    numlst =[]
    for i in lst:
        numlst.append(int(i))
    matrix.append(numlst)

for i in range(2):
    a = int(input("Enter value {}: ".format(i+1)))
    vec.append(a)

if len(vec) != len(numlst):
    print("cant multiply the matrix with the given vector!")
else:
    product_lst = []
    for i in matrix:
        dot_prod = 0
        for j, k in zip(i,vec):
            dot_prod = dot_prod +  j*k
        product_lst.append(dot_prod)  

    print(product_lst)
'''

#Write a program to calculate the product of a 4x4 identity matrix and a 4-dimensional vector. Ensure the output is the same as the original vector.
'''
f_dim_matrix = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
vec =[]

for i in range(4):
    a = int(input("Enter value {}: ".format(i+1)))
    vec.append(a)

if len(vec) != len(f_dim_matrix):
    print("cant multiply the matrix with the given vector!")
else:
    product_lst = []
    for i in f_dim_matrix:
        dot_prod = 0
        for j, k in zip(i,vec):
            dot_prod = dot_prod +  j*k
        product_lst.append(dot_prod) 
    print(product_lst)
'''

#Create a program that multiplies a matrix of size `n x m` with a vector of size `m`. Prompt the user to input values for `n`, `m`, the matrix, and the vector. 
'''
m = int(input("enter the size of m in the matrix: "))
n = int(input("enter the size of n in the matrix: "))
matrix =[]

for i in range(n):
    row = input("Enter the values of the row, seperated by a comma ({} values): ".format(m))
    lst = row.split(",")
    numlst =[]
    for i in lst:
        numlst.append(int(i))
    matrix.append(numlst)

vec = []
for i in range(m):
    a = int(input("Enter value {}: ".format(i+1)))
    vec.append(a) 

for i in matrix:
    if len(i) != m:
        print("the given matrix is not in {} X {} form".format(n,m))
        str = "error"
        break

if str == "error":
    print("enter correct values:")
else:
    product_lst = []
    for i in matrix:
        dot_prod = 0
        for j, k in zip(i,vec):
            dot_prod = dot_prod +  j*k
        product_lst.append(dot_prod) 
    print(product_lst)
'''

#Write a program that calculates the matrix-vector product for a 2x3 matrix and a vector of size 3
'''
m = 3
n = 2
matrix =[]

for i in range(n):
    row = input("Enter the values of the row, seperated by a comma ({} values): ".format(m))
    lst = row.split(",")
    numlst =[]
    for i in lst:
        numlst.append(int(i))
    matrix.append(numlst)

vec = []
for i in range(m):
    a = int(input("Enter value {}: ".format(i+1)))
    vec.append(a) 

for i in matrix:
    if len(i) != m:
        print("the given matrix is not in {} X {} form".format(n,m))
        str = "error"
        break

if str == "error":
    print("enter correct values:")
else:
    product_lst = []
    for i in matrix:
        dot_prod = 0
        for j, k in zip(i,vec):
            dot_prod = dot_prod +  j*k
        product_lst.append(dot_prod) 
    print(product_lst)
'''

# Create a program to calculate the product of a diagonal matrix and a vector. Input the diagonal elements only
'''
print("matrix size - n X n")
n = int(input("enter the size of n in the matrix: "))
matrix =[]
dia= input("enter the values of the diagonals seperated by comma: ")
lst = dia.split(",")
if len(lst) != n:
    print("enter correct number of values!")
else: 
    numlst =[]
    for i in lst:
        numlst.append(int(i))
    
    for i in range(1,n+1):
        row = []
        for j in range(i-1):
            row.append(0)
        row.append(numlst[i-1])
        for k in range(i,n):
            row.append(0)
        matrix.append(row)

    print(matrix)

    vec = []
    for i in range(n):
        a = int(input("Enter value {}: ".format(i+1)))
        vec.append(a) 

    product_lst = []
    for i in matrix:
        dot_prod = 0
        for j, k in zip(i,vec):
            dot_prod = dot_prod +  j*k
        product_lst.append(dot_prod) 
    print(product_lst)
'''

#Write a Python program to multiply a sparse matrix represented as a list of lists with a vector.





#Create a program to multiply a 5x5 matrix (randomly populated) with a vector of length 5.
'''
matrix = []
vec = []
lst=[]
numlst= []

for i in range(5):
    row = input("Enter the values of the row, seperated by a comma: ")
    lst = row.split(",")
    numlst =[]
    for i in lst:
        numlst.append(int(i))
    matrix.append(numlst)

for i in range(5):
    a = int(input("Enter value {}: ".format(i+1)))
    vec.append(a)

if len(vec) != len(numlst):
    print("cant multiply the matrix with the given vector!")
else:
    product_lst = []
    for i in matrix:
        dot_prod = 0
        for j, k in zip(i,vec):
            dot_prod = dot_prod +  j*k
        product_lst.append(dot_prod)  

    print(product_lst)
'''

# Write a program to multiply a row vector with a column vector to produce a matrix
'''
lst = []
lst2 = []
print("Values for the first list: ")
for i in range(1,4):
    a = int(input("Enter value number {0}:".format(i)))
    lst.append(a)
print("Values for the second list: ")
for i in range(1,4):
    a = int(input("Enter value number {0}:".format(i)))
    lst2.append(a)
dot_prod = 0
for i, j in zip(lst,lst2):
   dot_prod = dot_prod +  i*j
print("the product of the given row vector and the column vector is :", dot_prod)
'''

#Generate a program to calculate the matrix-vector product of a singular matrix and a vector.


#Create a program that computes the product of a matrix containing all negative integers with a positive vector.
'''
m = int(input("enter the dimensions of m for a n X m matrix: "))
n = int(input("enter the dimensions of n for a n X m matrix: "))
matrix =[]

for i in range(n):
    row = input("Enter the values of the row(only negative numbers), seperated by a comma ({} values): ".format(m))
    lst = row.split(",")
    numlst =[]
    for i in lst:
        numlst.append(int(i))
    matrix.append(numlst)

vec = []
for i in range(m):
    a = int(input("Enter value {}: ".format(i+1)))
    vec.append(a) 

for i in matrix:
    if len(i) != m:
        print("the given matrix is not in {} X {} form".format(n,m))
        str = "error"
        break

if str == "error":
    print("enter correct values:")
else:
    product_lst = []
    for i in matrix:
        dot_prod = 0
        for j, k in zip(i,vec):
            dot_prod = dot_prod +  j*k
        product_lst.append(dot_prod) 
    print(product_lst)
'''

#Write a Python program to multiply a lower triangular matrix with a vector, both provided as input by the user.

print("matrix size - n X n")
n = int(input("enter the size of n in the matrix: "))
matrix =[]

for i in range(n):
    row = input("Enter the values of the row, seperated by a comma ({} values): ".format(n))
    lst = row.split(",")
    numlst =[]
    for i in lst:
        numlst.append(int(i))
    matrix.append(numlst)


