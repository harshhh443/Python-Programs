


import mysql.connector as msc #this package contains all the required functions
                              #to perform any task from Python to SQL
#connect string
con=msc.connect(host="localhost",user="root",passwd="admin",database="mwf910")

#this function is used to check if we have connected to SQL or not
if con.is_connected()==True: 
    print("Successfully connected to DB")
else:
    print("Connection error!!")

#cursor is like a mediator object any data from/to SQL will be send/received using
#this cursor. You can name it anyting. This is common for reading and writing
#as well
cursor=con.cursor() 

#Topic 1. From Python to SQL (Writing to Database)


#Getting data from user which we will insert into SQL
roll=int(input("Enter Roll: "))
name=input("Enter your name: ")
marks=int(input("Enter marks: "))

#Building the command
cmd="insert into student values({},'{}',{})".format(roll,name,marks)

#Executing the command
cursor.execute(cmd)

#Commit function is used to make sure that the changes have been implemented
#to SQL
con.commit()



#Topic 2. From SQL to Python (Reading from Database)


#Building the command
cmd="Select * from student"

#Executing the command
cursor.execute(cmd)

#As the name suggests fetchall function will fetch all the data from cursor
#to your python variable which it brought from SQL
#if you want only one row then you can use fetchone() instead of fetchall()
#or if you want to fetch subsiquent rows one by one you can use fetchnext()

data=cursor.fetchall() #data will be a list of tuples
for row in data: #Printing record row by row
    print(row)

count=cursor.rowcount #rowcount is a variable which contains total number of
                      #rows which we received from SQL
print("Total number of records received: ",count)

#along with fetchall(), there are also some other fetch function
#which can be used as per requirement e.g. fetchmany(no_of_rows_you_want)
#fetchone() to get one row











