class matrix: # this code is slightly broken, the rref and inverse files arent but i havent updated this yet 
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
        for i in range(min(rows, columns)):
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
        for i in range(min(rows, columns)):
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

x = matrix([[2,2,3,3],[2,2,3,3],[3,3,4,5],[3,56,2,2],[45,56,5,2]])
print(x.rref())
