import math
def prime(n):
    ans=[]
    while n%2==0:
        ans.append(2)
        n=n//2


    num=math.floor(math.sqrt(n))
    for i in range(3,num+1,2):
        while n%i==0:
            ans.append(i)
            n=n//i
    return max(set(ans))

print(prime(600851475143))
