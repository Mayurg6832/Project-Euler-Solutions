for i in range(1001):
    for j in range(i):
        for k in range(j):
            if k**2+j**2==i**2 and (i+j+k)==1000:
                print(i*j*k)
                exit()