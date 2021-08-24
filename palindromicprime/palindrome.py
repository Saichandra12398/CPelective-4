def isPrime(n):
    if n<2 or n%2==0:
        return False
    if n==2:
        return True
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False
    return True
# print(isPrime(121))
def palindromicprime(n):
    if isPrime(n) and isPrime(int(str(n)[::-1])):
        return True
    return False


print(palindromicprime(121))