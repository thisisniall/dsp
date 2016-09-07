# Matrix Algebra

import numpy

# m * n = rows by columns

# 1. matrix dimensions

A = numpy.matrix([[1,2,3],[2,7,4]]) # 2 row by 3 columns
B = numpy.matrix([[1,-1],[0,1]]) # 2 rows by 2 columns
C = numpy.matrix([[5,-1],[9,1],[6,0]]) # 3 rows by 2 columns
D = numpy.matrix([[3,-2,-1],[1,2,3]]) # 2 rows by 3 columns
u = numpy.matrix([6,2,-3,5]) # 1 row by 4 columns
v = numpy.matrix([3,4,-1,4]) # 1 row by 4 columns
w = numpy.matrix([[1],[8],[0],[5]]) # 4 rows by 1 column

#1: Matrix Dimensions

# numpy.shape displays as (outerarraylength, innerarraylength), or rows/columns as I've coded them

#1.1
print "1.1"
print numpy.shape(A)
#1.2
print "1.2"
print numpy.shape(B)
#1.3
print "1.3"
print numpy.shape(C)
#1.4
print "1.4"
print numpy.shape(D)
#1.5
print "1.5"
print "below should probably display as (1,4) in these circumstances for rows, columns format:"
print numpy.shape(u)
#1.6
print "1.5"
print "below should probably display as (1,4) in these circumstances for rows, columns format:"
print numpy.shape(v)
#1.7
print "1.7"
print numpy.shape(w) # i may have coded w wrong, i can clearly see the column/row difference here but the code doesn't seem to

# #2: Vector Operations
alpha = 6

#2.1: u + v # addition
print "2.1"
print numpy.add(u,v)
#2.2: u - v # subtraction
print "2.2"
print numpy.subtract(u,v)
#2.3 alpha * u #scaling
print "2.3"
print numpy.multiply(alpha,u)
#2.4 u * v #dotproduct
print "2.4"
# we use multiply here due to vector multiplication being slightly different than matrix multiplication per the linear algebra handout
print numpy.multiply(u,v)
#2.5 ||u|| # norm(length)
print "2.5"
print numpy.linalg.norm(u)

#3: Matrix Operations
# use numpy's .dot for matrices multiplying matrixes, for vector by vector or scalar by vector we can use .multiply

# 3.1: A+C
print "3.1"
print "not defined, operation fails"
#print numpy.add(A,C)

# 3.2: A- C transpose
print "3.2"
CT = numpy.transpose(C)
print numpy.subtract(A,CT)

# 3.3: C transpose + 3 * D
three_D = numpy.dot(3,D)
print "3.3"
print numpy.add(CT,three_D)

# 3.4: B*A
print "3.4"
print numpy.dot(B,A)

# 3.5: B * Atranspose 
AT = numpy.transpose(A)
print "3.5"
print "not defined"
#print numpy.dot(B,AT) # fails

print "Optional problems:"

# 3.6: B*C
print "3.6"
print "not defined"
#print numpy.dot(B,C) # fails

# 3.7: C*B
print "3.7"
print numpy.dot(C,B)

# # 3.8: B^4
# print "3.8"

# # 3.9 A * A transpose
# print "3.9"

# # 3.10 D transpose * D
# print "3.10"



# def matrix_add(m1,m2):
# 	result[a][b] == m1[a][b]+m2[a][b]
# 	return "no"
# result = []
# result[0][0]=A[0][0]+B[0][0]
# print result

# def check(m1,m2):
# 	result = []
# 	for i in range(0,len(m1)):
# 		if len(m1[i]) > 1:
# 			for j in range(0,len(m1[i]):
# 				result[i][j] = m1[i][j] + m2[i][j]
# 	return result

# print check(A,D)

# # note this only works for MATRICES WITH 2x2 or greater sizes
# def matrix_add(m1, m2):
# 	# check to make sure matrices have same number of rows
# 	if len(m1) != len(m2):
# 		print 'matrices must be of the same dimensions to add them'
# 		return False
# 	# check to make sure matrices have same number of columns
# 	# this checks literally every sub-item, we could probably do a simple 0 vs 0 check	
# 	for i in range(0,len(m1)):
# 	 	if len(list(m1[i])) != len(list(m2[i])):
# 			print 'matrices must be of the same dimensions to add them'
# 			return False
# 	result = []
# 	#iterate through rows
# 	for a in range(len(m1)):
# 		#iterate through columns
# 		for b in range(len(m1[0])):
# 			result[a][b] = m1[a][b] + m2[a][b]
# 	return result


