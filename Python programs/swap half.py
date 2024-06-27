def swap_half(lst,n):
    mid=0
    if n%2==0:
        mid=n//2
    else:
        mid= n//2 +1

    j=mid
    for i in range(n//2):
        lst[i],lst[j]=lst[j],lst[i]
        j+=1

lst=[10,20,30,40,50,60,70]
print(lst)
n=len(lst)
swap_half(lst,n)
print(lst)
