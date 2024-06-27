def tot(a,b,c,n ):
    for i in range(n):
        c.append(a[i])
        c.append(b[i])

a=[10,20,30]
b=[40,50,60]
c=[]
n=len(a)
tot(a,b,c,n)
print(c)
