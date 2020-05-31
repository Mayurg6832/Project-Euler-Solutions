def is_palin(n):
    s=str(n)
    i=0
    j=len(s)-1
    while i<j:
        if s[i]==s[j]:
            i+=1
            j-=1
        else:
            return False
    if i==j:
        return True
    if s[i]==s[j]:
        return True

    return False

sum=0
for n in range(1,1000001):
    b=bin(n)
    if is_palin(n) and is_palin(b[2:]):
        sum+=n
print(sum)
