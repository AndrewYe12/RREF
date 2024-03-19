#this function row reduces a matrix, not to exactly echelon form as the first entries of the nonzero rows are in column ki where i is the row, 
#and it does not follow the form k1<k2<k3<k4... --> need to do that

def rref(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    rref_form = matrix
    for i in range(min(rows, columns)):
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
    return rref_form



print(rref([
        [1, 0, 0, 0, 0, 0,0,0,0,0,0,0,0, 2010],
        [1, 1,1,1,1,1,1,1,1,1,1,1,1,2052],
        [1,2,2**2,2**3,2**4,2**5,2**6,2**7,2**8,2**9,2**10,2**11,2**12, 1880],
	[1, 3, 3**2, 3**3, 3**4, 3**5,3**6,3**7, 3**8,3**9,3**10,3**11,3**12,2099],
	[1, 4, 4**2, 4**3, 4**4, 4**5,4**6,4**7,4**8,4**9,4**10,4**11,4**12, 2039],
        [1, 5, 5**2,5**3,5**4,5**5, 5**6,5**7,5**8,5**9,5**10,5**11,5**12,2110],
	[1, 6, 6**2,6**3,6**4,6**5,6**6,6**7,6**8,6**9,6**10,6**11,6**12, 2016],
	[1, 7,7**2,7**3,7**4,7**5,7**6,7**7,7**8,7**9,7**10,7**11,7**12, 2027],
	[1, 8, 8**2,8**3,8**4,8**5,8**6,8**7,8**8,8**9,8**10,8**11,8**12, 2011],
	[1, 9, 9**2,9**3,9**4,9**5,9**6,9**7,9**8,9**9,9**10,9**11,9**12,1943],
	[1, 10, 10**2,10**3,10**4,10**5,10**6,10**7,10**8,10**9,10**10,10**11,10**12,1993],
	[1, 11, 11**2,11**3,11**4,11**5,11**6,11**7,11**8,11**9,11**10,11**11, 11**12,1929],
	[1, 12, 12**2,12**3,12**4,12**5,12**6,12**7,12**8,12**9,12**10,12**11,12**12,2014]
	]))
