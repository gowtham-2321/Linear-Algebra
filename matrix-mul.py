def mul(m1,m2,n):
    matrix = []
    for i in range(0,n):
        temprow =[]
        for j in range(0,n):
            sum = 0
            for k in range(0,n):
                sum = sum + m1[i][k]*m2[k][j]
            temprow.append(sum)
        matrix.append(temprow)
    return matrix


