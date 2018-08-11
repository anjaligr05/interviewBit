def two_sum(arr, target):
	print 'original arr', arr
	hmap = {}
	for i  in range(len(arr)):
		if target-arr[i] in hmap:
			return (hmap[target-arr[i]]+1, i+1)
		if arr[i] not in hmap:
			hmap[arr[i]] = i
	return (None, None) 
print two_sum([2,7,11,15], 9)			
print two_sum([3,7,10,0],13)
print two_sum([4,6,-1,5,2,0], -1)
