def prime(n):
    if n<2 and n%2==0:
        return False
    elif n==2:
        return True
    else:
        for i in range(3,int(n**0.5),2):
            if n%i==0:
                return False
        return True


def sumofdig(n):
    sum=0
    while n>0:
        sum+=n%10
        n//=10
    return sum

def additive(n):
    while n>9:
        n=sumofdig(n)
    return prime(n)

print(additive(29))
