def show():
    fin=open("story.txt","w")
    count=0
    for line in fin:
        for word in line.split():
            if word.islower()=="the":
                count+=1

    print(count)
    fin.close()
