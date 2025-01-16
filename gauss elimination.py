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
    num = matrix[i][i]
    if(i+1)== n:
        break
    mul = matrix[i+1][i]
    for j in range(n):
        matrix[i][j] = matrix[i][j]/num
        if(i+1)== n:
            break
        matrix[i+1][j] = matrix[i+1][j] - mul* matrix[i][j]
    
    
    

print(matrix)


