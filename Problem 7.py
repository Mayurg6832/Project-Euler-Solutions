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

i=1
count=1
while count!=10001:
    if prime(i):
        print(i)  
        i+=1
        count+=1
    i+=1
  
