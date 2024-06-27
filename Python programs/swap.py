def swap_adj(lst,n):
    for i in range(0,n-1,2):
        lst[i],lst[i+1]=lst[i+1],lst[i]

lst=[10,20,30,40,50,60]
print(lst)
n=len(lst)
swap_adj(lst,n)
print(lst)
