class emp:
    name=""
    designation=""
    def setdata(self):
        self.name=input("Enter employee name:")
        self.designation=input("Enter designation:")
    def display(self):
        print(self.name,self.designation)

class child(emp):
    sal=0
    def set(self):
        self.sal=int(input("Enter salary:"))
    def disp(self):
        print(self.sal)
obj=child()
obj.setdata()
obj.set()
obj.display()
obj.disp()
