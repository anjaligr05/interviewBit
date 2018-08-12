def digits(num):
	d = 0
	if num==0:
		return 1
	while num!=0:
		num = num/10
		d+=1
	return d
def digi_prod(num):
	prod = 1
	while num:
		prod*=num%10
		num = num/10
	return prod
		
def colorful(num):
	n = digits(num)
	onum = num
	i = n
	prods = []
	while i>=1:
		num = onum%pow(10,i)
		while num:
			if digi_prod(num) in prods:
				return 0
			else:
				prods.append(digi_prod(num))
			num = num/10
		i-=1
	return 1
print colorful(3245)
print colorful(0)
print colorful(1)
print colorful(23)
