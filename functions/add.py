def addmatrix(matrix1, matrix2):
    finalmatrix = []
    for list1, list2 in zip(matrix1, matrix2):
        temp = []
        for listy1, listy2 in zip(list1, list2):
            temp.append(listy1 + listy2)
        finalmatrix.append(temp)

    return finalmatrix

print(addmatrix([[1,1],[1,1]], [[1,1],[1,4]])) 