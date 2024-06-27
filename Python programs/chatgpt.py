def append_elements(L):
    n=int(input("Enter an integer= "))
    L.append(n)
    print(n,"appended successfully.")
    print()
    
def remove_even(L):
    L1=[]
    for i in L:
        if i%2!=0:
            L1.append(i)
    return L1
    print()
    
def remove_odd(L):
    L2=[]
    for i in L:
        if i%2==0:
            L2.append(i)
    return L2
    print()
    
def check_unique(L):
    if len(L)!=0:
        unique_list=set(L)
        if len(unique_list)==len(L):
            print("unique elements exist.")
        else:
            print("Duplicate elements exist.")
    else:
        print("list is empty ")
    print()
    
L=[]
while True:
    print("1. Create a list by appendig elements.")
    print("2. Print list after removing even elements.")
    print("3. Print list by removing odd elements.")
    print("4. Check if all elements are unique are not.")
    print("5. Exit.")
    print()
    ch=int(input("Enter choice(1-5)= "))
    print()
    if ch==1:
        append_elements(L)
    elif ch==2:
        print(remove_even(L))
    elif ch==3:
        print(remove_odd(L))
    elif ch==4:
        check_unique(L)
    elif ch==5:
        print("Exiting the program.")
        break
    else:
        print("Wrong Choice")
        print()