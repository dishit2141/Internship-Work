class cal1:

    def setdata(self,a,b,d):
        return a,b,d
    def display(self,a,b,d):
        sum=(a+b+d)
        print("Sum=",sum)

c=cal1()
a,b,d=c.setdata(1,2,3)
c.display(a,b,d)

