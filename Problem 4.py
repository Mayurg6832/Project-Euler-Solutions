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

mx=0
for i in range(100,1000):
    for j in range(100,1000):
        n=i*j
        if is_palin(n) and n>mx:
            mx=n
print(mx)
