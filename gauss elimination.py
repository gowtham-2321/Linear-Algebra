#gauss elimination

print("matrix size - n X n")
n = int(input("enter the size of n in the matrix: "))
matrix =[]

#values for the matrix
for i in range(n):
    row = input("Enter the values of the row, seperated by a comma ({} values): ".format(n))
    lst = row.split(",")
    numlst =[]
    for i in lst:
        numlst.append(int(i))
    matrix.append(numlst) 

    

for i in range(n):
    num = matrix[0][0]
    if(i+1)== n:
        break
    mul = matrix[i+1][0]
    for j in range(n):
        matrix[0][j] = matrix[0][j]/num
        matrix[i+1][j] = matrix[i+1][j] - mul* matrix[0][j]
        print(matrix)
    print("end of first time fixing row")

for i in range(1,n):
    num = matrix[1][1]
    if(i+1)== n:
        break
    mul = matrix[i+1][1]
    for j in range(n):
        matrix[1][j] = matrix[1][j]/num
        matrix[i+1][j] = matrix[i+1][j] - mul* matrix[1][j]
        print(matrix)
    print("end of first time fixing row")
 
    
    

print(matrix)


