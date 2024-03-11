num1=int(input("enter a number"))
sum=0

for i in num1:
    sum+=int(i)**3
if sum==int(num1):
   print("armstong")
else:
    print("not armstrong")
