def in_sort(lst,n):
    for i in range(1,n):
        j=i
        while j>0 and lst[j]<lst[j-1]:
            lst[j],lst[j-1]=lst[j-1],lst[j]
            j-=1

lst=[50,40,20,30,10]
n=len(lst)
in_sort(lst,n)
print(lst)
