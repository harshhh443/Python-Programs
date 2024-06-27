def swag_adj(lst,n):
    end=0
    if n%2==0:
        end=n
    else:
        end=n-1
        for i in range (0,end,2):
            lst[i],lst[i+1]=lst[i+1],lst[i]

lst=[10,20,30,40,50,60]
print(lst)
n=len(lst)
swag_adj(lst,n)
print(lst)
