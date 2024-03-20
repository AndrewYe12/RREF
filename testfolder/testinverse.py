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
    

    templist = rref_form.copy() 
    for x in range(min(rows,columns)-1, -1, -1): #zeros down
        if rref_form[x] == [0]*columns:
            needtoadd = templist[x]
            rref_form.pop(x)
            rref_form.append(needtoadd)
            yayinverse = inverse.pop(x)
            inverse.append(yayinverse)
    

    templist = rref_form.copy()
    tempinverse = inverse.copy()
    for x in range(min(columns,rows)-1, -1, -1): #switch the rows to get rref
        if rref_form[x] == [0]*columns:
            continue        
        elif rref_form[x][x] != 1:
            count = 0
            for num in range(columns):
                pivot = rref_form[x][num]
                if pivot != 0:
                    break
                count += 1
            yay = templist[x]
            rref_form.insert(num, yay)
            rref_form.pop(x+1)

            inverseyay = tempinverse[x]
            inverse.insert(num, inverseyay)
            inverse.pop(x+1)
    return inverse
    

print(inverse([[3,3,4,5], [2,2,3,3],[2,2,3,3]]))
#,[2,2,4,2],[443,4,4,4]