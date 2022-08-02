num1=int(input("Enter the 1st number:"))
num2=int(input("Enter the 2nd number:"))
if num1>=num2:
    min=num1
else:
    min=num2
for i in range(1,min+1):
    if num1%i==0 and num2%i==0:
        GCD=i
if GCD==1:
    print("The numbers are co-prime")
else:
    print("The numbers are not co-prime")
    
