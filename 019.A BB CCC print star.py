num=int(input("enter no. of rows: "))
k=ord("A")
for i in range(0,num):
    for j in range(0,i+1):
        print(chr(k),end=" ")

    print()
    k=k+1
