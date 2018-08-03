def prod(num):
	prd = 1
	while num:
		prd *=num%10
		num = num/10
	if prd > 10:
		return prod(prd)
	else:
		return prd
def colorful(num):
	setN = {}
	snum = str(num)
	print prod(num)
	for i in range(len(str(num))):
		for j in range(i, len(str(num))):
			n = int(snum[i:j+1])
			prd = prod(n)
			if prd in setN:
				print setN
				return 0
			else:
				setN[prd] = n
	
	return 1
print colorful(234)
