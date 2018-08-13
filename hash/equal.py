def equal(A):
	hmap = {}
	result = []
	for i in range(len(A)):
		for j in range(i+1, len(A)):
			if A[i]+A[j] in hmap:
				a,b,c,d = hmap[A[i]+A[j]]+(i,j)
				if a<b and c<d and a<c and b!=c and b!=d:
					result.append([a,b,c,d])
			else:
				hmap[A[i]+A[j]] = (i,j)
	if len(result)==0:
		return []
	return min(result)
print equal([3,4,7,1,2,9,8])
