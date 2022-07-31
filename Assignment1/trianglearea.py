a=int(input("Enter the 1st length: "))
b=int(input("Enter the 2nd length: "))
c=int(input("Enter the 3rd length: "))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("The area of triangle: ",area)
