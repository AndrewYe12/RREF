def multiply(matrix1, matrix2):
    finalmatrix = []
    for i in range(len(matrix1)):
        tempy = []
        for x in range(len(matrix1[0])):
            temp = [matrix1[i][x]*matrix2[x][y] for y in range(len(matrix2[0]))]
            if not tempy:
                tempy.append(temp)
            else:
                yay = []
                for list1, list2 in zip(tempy[0], temp):
                    hello = list1 + list2
                    yay.append(hello)
                tempy[0] = yay
        finalmatrix.append(tempy)
    return finalmatrix

print(multiply([[4,5,7],[2,1,0]],[[2,3],[8,9],[1,1]]))        