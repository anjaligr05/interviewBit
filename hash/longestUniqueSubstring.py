def longestUniqueString(A):
	start = 0
	max_len = 0
	hmap = {}
	for i in range(len(A)):
		if A[i] in hmap:
			start = hmap[A[i]] + 1
		else:
			max_len = max(max_len, i-start+1)
			#print A[start:i+1]
		hmap[A[i]] = i
	return max_len
print longestUniqueString('abcabcad')
print longestUniqueString('bbbb')
