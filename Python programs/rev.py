def rev(lst,n):
    for i in range(n//2):
        lst[i],lst[n-1-i]=lst[n-1-i],lst[i]
        

lst=[10,20,30,40,50,60]
print(lst)
n=len(lst)
rev(lst,n)
print(lst)
