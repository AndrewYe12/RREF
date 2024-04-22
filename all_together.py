from fractions import Fraction as frac
import copy

class matrix: 
    def __init__(self, matrix): #constructor
        self.matrix = matrix
    
    def fraction(self): #Instance method to turn the matrix into one where each entry is a fraction. Returns a 2-d list of strings. 
        newmatrix = copy.deepcopy(self.matrix)
        for x in range(len(newmatrix)):
            for y in range(len(newmatrix[0])):
                newmatrix[x][y] = str(frac(str(newmatrix[x][y])).numerator) + '/' + str(frac(str(newmatrix[x][y])).denominator)
        newmatrix = matrix(newmatrix)
        return newmatrix

    def inverse(self): #Instance method to find the inverse of a particular matrix. Returns an inverse matrix of the matrix class. 
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
            for nonzero in range(columns): #find pivot  
                pivot = rref_form[i][nonzero]
                if pivot != 0:
                    break
                count +=1
            if count == columns:
                continue
            rref_form[i] = [x/pivot for x in rref_form[i]] #divide pivot row by the pivot so the 1st entry is 1
            inverse[i] = [x/pivot for x in inverse[i]] #Do same on inverse
            for rest in range(rows): #Subtract from the rest of the rows in such a way that the only value in the pivot column is the 1 in the pivot row. 
                if rest ==i:
                    continue 
                k = rref_form[rest][count]
                temp =[]
                for list1, list2 in zip(rref_form[i], rref_form[rest]):
                    temp.append(-list1*k + list2)
                rref_form[rest] = temp

                anotherTemp = [] #Do same on inverse
                for list1, list2 in zip(inverse[i], inverse[rest]):
                    anotherTemp.append(-list1*k + list2)
                inverse[rest] = anotherTemp


        countThis = 0 #Counts the number of zero rows
        for x in range(rows):
            if rref_form[x] == [0]*columns:
                countThis +=1

        limit  = min(rows, columns)
        x=0
        z=0
        while z<countThis: #Pulls the zeros down to the bottom. Do on both inverse and rref
            if rref_form[x] == [0]*columns:
                newTemp = inverse[x]
                for y in range(x,rows-1):
                    rref_form[y] = rref_form[y+1]
                    inverse[y] = inverse[y+1]
                rref_form[rows-1] = [0]*columns
                inverse[rows-1] = newTemp
                z +=1
                x-=1
            x+=1

        sortThisArray = [0]*limit #creates a list where the ith entry of the list is the column index of the pivot in row i. 
        for x in range(limit-1, -1,-1):
            for y in range(columns):
                pivot = rref_form[x][y]
                if pivot != 0:
                    break
            sortThisArray[x] = y
        
        constantArray = copy.deepcopy(sortThisArray) #create deep copy
        sortThisArray.sort()
        newInverse = [[0]*rows for i in range(rows)] 
        for x in range(len(sortThisArray)): #compare the old and new lists so that you can figure out where the rows need to go. 
            temp = constantArray[x]
            for index in range(len(sortThisArray)):
                if sortThisArray[index] == temp:
                    break
            newInverse[index] = inverse[x]

        for x in range(rows):
            if newInverse[x] == [0]*rows:
                newInverse[x] = inverse[x]

        newInverse = matrix(newInverse)


        return newInverse
    
    def rref(self): #everything done in the rref method is done in the inverse method. Returns an element of the matrix class 
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

        countThis = 0
        for x in range(rows):
            if rref_form[x] == [0]*columns:
                countThis +=1

        limit = min(rows, columns)
        x=0
        z=0
        while z<countThis: #zeros down
            if rref_form[x] == [0]*columns:
                for y in range(x,rows-1):
                    rref_form[y] = rref_form[y+1]
                rref_form[rows-1] = [0]*columns
                z +=1
                x-=1
            x+=1

        sortThisArray = [0]*limit
        for x in range(limit-1, -1,-1):
            for y in range(columns):
                pivot = rref_form[x][y]
                if pivot != 0:
                    break
            sortThisArray[x] = y
        
        newMatrix= [ [0]*columns for i in range(rows)]
        constantArray = copy.deepcopy(sortThisArray)
        sortThisArray.sort()
        for x in range(len(sortThisArray)):
            temp = constantArray[x]
            for index in range(len(sortThisArray)):
                if sortThisArray[index] == temp:
                    break
            newMatrix[index] = rref_form[x]

        newMatrix = matrix(newMatrix)

        return newMatrix


    def __mul__(self, other): #Overrides the * operator such that it multiplies two matrices together. Returns an element of the matrix class
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

    def __add__(self, other): #Overrides the + operator such that it adds two matrices together. Returns an element of the matrix class. 
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
    #print(x.rref().matrix) 
    y = matrix([[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,1],[1,0,0],[0,0,0],[0,1,0],[0,0,0]])
    print(x.rref().matrix)
 