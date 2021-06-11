class cal3:
    p=0
    r=0
    n=0
    sum=0
    def __init__(self,p,r,n):
        self.p=p
        self.r=r
        self.n=n
         
    def calc(self):
        self.sum=self.p*self.r*self.n/100
        
    def display(self):
        print(self.sum)
        
obj=cal3(1000,5,2)
obj.calc()
obj.display()
        
