# Background: a Kaprekar number is a non-negative integer, the representation of whose square 
# can be split into two possibly-different-length parts (where the right part is not zero) 
# that add up to the original number again. For instance, 45 is a Kaprekar number, because 
# 45**2 = 2025 and 20+25 = 45. You can read more about Kaprekar numbers here. The first several 
# Kaprekar numbers are: 1, 9, 45, 55, 99, 297, 703, 999 , 2223, 2728,... 
# With this in mind, write the function nthKaprekarNumber(n) that takes a non-negative int n 
# and returns the nth Kaprekar number, where as usual we start counting at n==0.


import math

def kaprek(n):
    if n==1:
        return True
    x=n**2
    # print(x)
    if len(str(x))>1:
        left=int(str(x)[:len(str(x))//2])
        right=int(str(x)[len(str(x))//2:])
        # print(left,right)
        if left+right==n:
            return True
        else:
            return False
    else:
        return False
    

# kaprek(45)
def fun_nth_kaprekarnumber(n):
    count=0
    i=0
    while True:
        i+=1
        if kaprek(i):
            print(i)
            count+=1
        if count==n+1:
            return i

print(fun_nth_kaprekarnumber(20))
# print(4950**2)