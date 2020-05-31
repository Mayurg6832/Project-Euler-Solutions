import math

def same_multi(num):
    ans=1
    for i in range(1,num+1):
        ans=int((ans*i)/math.gcd(ans,i))
    return ans
    
print(same_multi(20))