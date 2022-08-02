num=int(input("Enter a number:"))
print("The first N prime numbers:")
for i in range(1,num+1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i,end=" ")
	
