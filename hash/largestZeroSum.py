def largestZeroSum(arr):
	print 'original arry = ', arr
	hmap = {}
	cur_sum = 0
	max_len = []
	for i in range(len(arr)):
		cur_sum += arr[i]
		if arr[i] == 0:
			max_len = [i]
		if cur_sum == 0:
			max_len = A[0:i+1]
		if cur_sum in hmap:
			if len(max_len)<i-hmap[cur_sum]:
				max_len = arr[hmap[cur_sum]+1:i+1]
		else:
			hmap[cur_sum] = i
	return max_len
print largestZeroSum([1,2,-2,4,-4])
