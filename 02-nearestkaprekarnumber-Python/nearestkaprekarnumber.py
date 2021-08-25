# Note: please do not start this problem prior to completing previous problem. 
# Bearing in mind the definition of Kaprekar Number from above problem, write the function 
# nearestKaprekarNumber(n) that takes an int value n and returns the Kaprekar number 
# closest to n, with ties going to smaller value. For example, nearestKaprekarNumber(49) returns 45, 
# and nearestKaprekarNumber(51) returns 55. And since ties go to the smaller number, 
# nearestKaprekarNumber(50) returns 45. 
# Note: as you probably guessed, this also cannot be solved by counting up from 0, 
# as that will not be efficient enough to get past the autograder. 
# Hint: one way to solve this is to start at n and grow in each direction until you find a Kaprekar number.


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
# def fun_nth_kaprekarnumber(n):
#     count=0
#     i=0
#     while True:
#         i+=1
#         if kaprek(i):
#             print(i)
#             count+=1
#         if count==n+1:
#             return i

# print(fun_nth_kaprekarnumber(20))
# print(4950**2)
import math

def fun_nearestkaprekarnumber(n):
    left=0
    right=0
    for i in range(n,0,-1):
        if kaprek(i):
            left=i
            break
    for i in range(n,n+10000,1):
        if kaprek(i):
            right=i
            break
    print(left,right)
    x=left if n-left<=right-n else right
    return x