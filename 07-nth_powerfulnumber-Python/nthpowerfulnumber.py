# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it. 
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.
def isprime(a):
	if a > 1:
		for j in range(2, int(a/2) + 1):  
			if (a % j) == 0:
				return False
		return True
	else:
		return False
def powerful(n):
	for i in range(2,n):
		if isprime(n) and (n%i==0 and n%(i**2)==0):
			return True
def nthpowerfulnumber(n):
	# Your code goes here
	count=0
	num=0
	while count<=n:
		if powerful(num):
			count+=1
		num+=1
	return num

print(nthpowerfulnumber(53))
