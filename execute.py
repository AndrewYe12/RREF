from all_together import matrix
#import numpy as np 

x = matrix([[-3,3,4,5], [2,2,3,3],[2,2,3,22]])
y = matrix([[-3,3,4,10,9], [2,22,3,3,8],[2,11,3,22,7],[4,2,1,34,5]])
z = matrix([[-3,3,4], [2,2,3],[2,2,4]]) 
a = matrix([[1,2,23],[0,4,4],[0,1,6]])
print(a.inverse().matrix) 
print(a.det())
print(a.rref().matrix)
