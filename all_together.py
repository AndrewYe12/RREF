class matrix: 
    def __init__(self, matrix):
        self.matrix = matrix

    def inverse(self):
        rows = len(self.matrix)
        columns = len(self.matrix[0])
        rref_form = self.matrix
        inverse = []
        counting = 0
        for row in range(rows): # generate identity 
            inverse.append([0]*rows)
            inverse[row][counting] = 1
            counting += 1
        if rows < columns: # i think this might be arbitrary, but i am afraid to break the code, so i wont change ii
            numbersyay = min(rows, columns)
        else:
            numbersyay = max(rows,columns)
            
        for i in range(numbersyay):
            count = 0
            for nonzero in range(columns):
                pivot = self.matrix[i][nonzero]
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
    
    def rref(self):
        rows = len(self.matrix)
        columns = len(self.matrix[0])
        rref_form = self.matrix
        if rows < columns:
            numbersyay = min(rows, columns)
        else:
            numbersyay = max(rows,columns)
        for i in range(numbersyay): 
            count = 0
            for nonzero in range(columns):
                pivot = self.matrix[i][nonzero]
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
        return rref_form

    def __mul__(self, other):
        finalmatrix = []
        for i in range(len(self.matrix)):
            tempy = []
            for x in range(len(self.matrix[0])):
                temp = [self.matrix[i][x]*other.matrix[x][y] for y in range(len(other.matrix[0]))]
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

    def __add__(self, other):
        finalmatrix = []
        for list1, list2 in zip(self.matrix, other.matrix):
            temp = []
            for listy1, listy2 in zip(list1, list2):
                temp.append(listy1 + listy2)
            finalmatrix.append(temp)
        return finalmatrix



x = matrix([[2,3],[8,9],[1,1]])
y = matrix([[4,5,7],[2,1,0]])
print(y*x)

t = matrix([[22,34],[43,22]])
m = matrix([[34,22],[23,55]])
print(t+m)
