from fractions import Fraction as frac
import copy

class matrix: 
    def __init__(self, matrix):
        self.matrix = matrix
    
    def fraction(self):
        newmatrix = copy.deepcopy(self.matrix)
        for x in range(len(newmatrix)):
            for y in range(len(newmatrix[0])):
                newmatrix[x][y] = str(frac(str(newmatrix[x][y])).numerator) + '/' + str(frac(str(newmatrix[x][y])).denominator)
        newmatrix = matrix(newmatrix)
        return newmatrix

    def inverse(self):
        rows = len(self.matrix)
        columns = len(self.matrix[0])
        rref_form = copy.deepcopy(self.matrix)
        inverse = []
        counting = 0
        for row in range(rows): # generate identity 
            inverse.append([0]*rows)
            inverse[row][counting] = 1
            counting += 1
        numbersyay = rows
        for i in range(numbersyay):
            count = 0
            for nonzero in range(columns):
                pivot = rref_form[i][nonzero]
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
        
        inverse = matrix(inverse)

        return inverse
    
    def rref(self):
        rows = len(self.matrix)
        columns = len(self.matrix[0])
        rref_form = copy.deepcopy(self.matrix)
        numbersyay = rows
        for i in range(numbersyay): 
            count = 0
            for nonzero in range(columns):
                pivot = rref_form[i][nonzero]
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

        rref_form = matrix(rref_form)

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
        
        finalmatrix = matrix(finalmatrix)
        return finalmatrix

    def __add__(self, other):
        finalmatrix = []
        for list1, list2 in zip(self.matrix, other.matrix):
            temp = []
            for listy1, listy2 in zip(list1, list2):
                temp.append(listy1 + listy2)
            finalmatrix.append(temp)
        
        finalmatrix = matrix(finalmatrix)

        return finalmatrix


if __name__ == '__main__':
    x = matrix([[0,0,0,3,78,8,0],[2,41,3,98,9,89,9],[6,78,4,2,6,76,7],[32,4,8,6,7,5,9],[6,4,8,3,67,8,878]])
    print(x.rref().matrix) 
 