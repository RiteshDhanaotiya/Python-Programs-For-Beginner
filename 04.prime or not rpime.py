'''
num=int(input("enter a number"))
if num>1:
    for i in range(2,num):
     if (num%i)==0:
        print("else")
        break
     else:
        print("number is prime")

else:
    print("num is not prime") '''


num=22
for i in range(2,num):
      if(num%i)==0:
            print("not prime")
            break
      else:
             print("prime")
        
