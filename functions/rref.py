#this function row reduces a matrix, not to exactly echelon form as the first entries of the nonzero rows are in column ki where i is the row, 
#and it does not follow the form k1<k2<k3<k4... --> need to do that

def rref(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    rref_form = matrix
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
        for rest in range(rows):
            if rest ==i:
                continue 
            k = rref_form[rest][count]
            temp =[]
            for list1, list2 in zip(rref_form[i], rref_form[rest]):
                temp.append(-list1*k + list2)
            rref_form[rest] = temp

    templist = rref_form.copy()
    for x in range(min(rows,columns)-1, -1, -1): #zeros down
        if rref_form[x] == [0]*columns:
            needtoadd = templist[x]
            rref_form.pop(x)
            rref_form.append(needtoadd)

    templist = rref_form.copy()
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
            
    return rref_form




print(rref([[3,3,4,5], [2,2,3,3],[2,2,3,3],[2,2,4,2],[443,4,4,4]]))
 