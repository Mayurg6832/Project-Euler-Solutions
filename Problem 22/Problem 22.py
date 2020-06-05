names=open("p022_names.txt",'r')
p=sorted(names.read().replace('"','').split(','),key=str)
mul=0
fi=0
for i in p:
	mul+=1
	sum1=0
	for j in range(len(i)):
		sum1+=ord(i[j])-64
	fi+=sum1*mul
print(fi)