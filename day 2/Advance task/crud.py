import mysql.connector  

mysqldb=mysql.connector.connect(host="localhost",user="dp",password="1234",database="employee")#established connection between your database  
mycursor=mysqldb.cursor()#cursor() method create a cursor object    
print("\t\t\tEmployee Data Store")
print("1. INSERT  RECORD")
print("2. DISPLAY RECORD")
print("3. UPDATE RECORD")
print("4. DELTE RECORD")

ch=input("Enter Your Choice:")
if(ch=='1'):
    empid=input("Enter Employee id:")
    empname=input("Enter Employee Name:")
    salary=input("Enter Employee salary:")

    try:  
        #Execute SQL Query to insert record  
        insert_stmt = ("insert into emp (empid,empname,salary) values(%s,%s,%s)")
        data = (empid,empname,salary)
        mycursor.execute(insert_stmt,data)  
        mysqldb.commit() # Commit is used for your changes in the database  
        print('Record inserted successfully...')   
    except:  
        # rollback used for if any error   
        mysqldb.rollback()  
        mysqldb.close()#Connection Close  
if(ch=='2'):
    try:  
        mycursor.execute("select * from emp")#Execute SQL Query to select all record   
        result=mycursor.fetchall() #fetches all the rows in a result set   
        for i in result:    
            empid=i[0]  
            name=i[1]  
            salary=i[2]  
            print(empid,name,salary)  
    except:   
        print('Error:Unable to fetch data.')  
        mysqldb.close()#Connection Close  
if(ch=='3'):

    str="update emp set salary=salary+1000 where empid='%d'"
    salary=int(input("Enter ID where you want to update salary:"))
    args=(salary)
    mycursor.execute(str % args)
    mysqldb.commit() # Commit is used for your changes in the database  
    print('Record updated successfully...')   
    # rollback used for if any error  
    mysqldb.rollback()  
    mysqldb.close()#Connection Close 
if(ch=='4'):
    no=int(input("Enter empid to delete record:"))
    delete_stmt = "DELETE FROM emp WHERE empid='%d'"
    args = (no)

    mycursor.execute(delete_stmt%args)#Execute SQL Query to detete a record   
    mysqldb.commit() # Commit is used for your changes in the database  
    print('Record deteted successfully...')  
    mysqldb.close()#Connection Close  
