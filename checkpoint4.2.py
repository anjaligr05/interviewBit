def nextGreaterEle(A):
	out = []
	indexList = []
	for i in range(len(A)):
		if len(indexList) != 0 and A[indexList[len(indexList)-1]] < A[i]:
			out.insert(indexList.pop(), A[i])
		indexList.append(i)
	while len(indexList)>0:
		out.insert(indexList.pop(), -1)
	print "input :{}".format(A)
	print "output:{}".format(out)
nextGreaterEle([3,4,10,5])
