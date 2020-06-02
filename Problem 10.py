import math
def prime(num):
    if num==1:
        return False
    if num==2:
        return True
    if num>2 and num%2==0:
        return False
    
    for i in range(3,math.floor(math.sqrt(num))+1,2):
        if num%i==0:
            return False
    return True

sum=0
for i in range(2000001):
    if prime(i):
        sum+=i
print(sum)
