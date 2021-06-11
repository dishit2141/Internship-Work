no1=int(input("Enter Number 1:"))
no2=int(input("Enter Number 2:"))
no3=int(input("Enter Number 3:"))
if(no1>no2):
    if(no1>no3):
        print(no1,"is greater")
    else:
        print(no3,"is greater")
elif(no2>no3):
    print(no2,"is greater")
else:
    print(no3,"is greater")

