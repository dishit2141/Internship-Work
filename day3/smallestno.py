no1=int(input("Enter Number 1:"))
no2=int(input("Enter Number 2:"))
no3=int(input("Enter Number 3:"))
if(no1<no2 and no1<no3):
    print(no1,"is Smallest")
elif(no2<no1 and no2<no3):
    print(no2,"is Smallest")
else:
    print(no3,"is Smallest")