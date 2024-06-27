def shift_fw(lst,n):
    for i in range(n-1,0,-1):
        lst[i],lst[i-1]=lst[i-1],lst[i]
        
lst=[10,20,30,40,50,60]
n=len(lst)
shift_fw(lst,n)
print(lst)
