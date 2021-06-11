class cal2:
    r=0
    def setdata(self):
        r=int(input("Enter radius to find area of circle:"))
        return r
    def area(self,area):
        area=r*r*3.14
        return area
    def display(self,data):
        return data

c=cal2()
r=c.setdata()
area=c.area(r)
data=c.display(area)
print("area of circle=",data)