class calc():
    def sum(self,x,y):
        return(x+y)
    def subtract(self,x,y):
        return(x-y)
    def multiple(self,x,y):
        return(x*y)
    def divide(self,x,y):
        return(x/y)
    
x=10
y=5

obj=calc()

while True:
    print("1.sum")
    print("2.subtract")
    print("3.multiple")
    print("4.divide")
    print("5.Exit")
    choice=int(input("enter your choice"))
    if choice==1:
         print ("result is:",obj.add(x,y))
    elif choice==2:
         print ("result is:",obj.subtract(x,y))
    elif choice==3:
         print ("result is:",obj.multiple(x,y))
    elif choice==4:
         print ("result is:",obj.divide(x,y))
    elif choice==5:    

         break
    else:
        print("invalid option")
        



         
