# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every 
# digit (from 0 to 9) at least once. 309 is the smallest number with this property. 
# Write the function nthWithProperty309 that takes a non-negative int n and returns 
# the nth number with Property309.
def prop309(n):
	n=n**5
	x=str(n)
	li=[0,0,0,0,0,0,0,0,0,0]
	while n>0:
		li[n%10]+=1
		n//=10
	return li.count(0)==0
def nthwithproperty309(n):
	i=0
	count=-1
	while count<n:
		i+=1
		if prop309(i):
			count+=1
	return i
print(nthwithproperty309(0))
	# Your code goes here
	
	