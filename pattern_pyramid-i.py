num=int(input("Enter Line Number : "))
for i in range(1,num+1):
    for j in range(i,num):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    for j in range(1,i):
        print("*",end="")
    print()
