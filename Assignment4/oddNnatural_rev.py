num=int(input("Enter a num:"))
print("The first N oddnatural number in reverse")
for i in range(num,0,-1):
    if i%2!=0:
        print(i,end=" ")
