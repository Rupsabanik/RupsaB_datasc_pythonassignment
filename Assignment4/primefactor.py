n=int(input("Enter any Number: "))
for i in range(2,n+1):
    if(n%i==0):
        prime=1
        for j in range(2,(i//2+1)):
            if(i%j==0):
                prime = 0
                break
        if (prime==1):
            print("%d is a Prime Factor of a Given Number %d" %(i,n))
