num=int(input("Enter a num:"))
print("The first N even natural number in reverse")
for i in range(num,1,-1):
    if i%2==0:
        print(i,end=" ")
