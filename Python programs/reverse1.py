def reverse(lst,n):
    for i in range(n//2):
        lst[i],lst[n-1-i]=lst[n-1-i],lst[i]


lst=[10,20,30,40,50,60,70]
n=len(lst)
reverse(lst,n)
print(lst)
