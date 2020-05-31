def rev_bit(n):
    rev=0
    while n>0:
        rev=rev<<1
        if n&1==1:
            rev^=1
        n=n>>1
    return rev

def is_palin_bin(n):
    rev=rev_bit(n)
    return (n==rev)

def is_palin_int(n):
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
    if is_palin_int(n) and is_palin_bin(n):
        sum+=n
print(sum)