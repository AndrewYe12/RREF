def inverse(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    rref_form = matrix
    inverse = []
    counting = 0
    for row in range(rows): # generate identity 
        inverse.append([0]*rows)
        inverse[row][counting] = 1
        counting += 1
    if rows < columns:
        numbersyay = min(rows, columns)
    else:
        numbersyay = max(rows,columns)
        
    for i in range(numbersyay):
        count = 0
        for nonzero in range(columns):
            pivot = matrix[i][nonzero]
            if pivot != 0:
                break
            count +=1
        if count == columns:
            continue
        rref_form[i] = [x/pivot for x in rref_form[i]]
        inverse[i] = [x/pivot for x in inverse[i]] #inverse
        for rest in range(rows):
            if rest ==i:
                continue 
            k = rref_form[rest][count]
            temp =[]
            for list1, list2 in zip(rref_form[i], rref_form[rest]):
                temp.append(-list1*k + list2)
            rref_form[rest] = temp

            anotherTemp = [] #inverse
            for list1, list2 in zip(inverse[i], inverse[rest]):
                anotherTemp.append(-list1*k + list2)
            inverse[rest] = anotherTemp
    return inverse


print(inverse([[2,2,3,3],[2,2,3,3],[3,3,4,5],[3,56,2,2],[45,56,5,2]]))