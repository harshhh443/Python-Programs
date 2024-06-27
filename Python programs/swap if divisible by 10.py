#Swap if divisible by 10
#[25,10,35,20,45]
lst=[25,10,35,20,45]

n=len(lst)

i=0
while i<n-1:
    if lst[i]%10==0:
        lst[i],lst[i+1]=lst[i+1],lst[i]
        i+=1
    i+=1

print(lst)
