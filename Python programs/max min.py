def max_min(lst,n):
    a=lst[0]
    b=lst[0]
    for i in range(1,n):
        if a<lst[i]:
            a=lst[i]
        if b>lst[i]:
            b=lst[i]
    print(a,b)

lst=[10,20,40,30,5,15]
n=len(lst)
max_min(lst,n)

