import math
a=int(input("Enter the number of a: "))
b=int(input("Enter the number of b: "))
c=int(input("Enter the number of c: "))
d = (b**2) - (4*a*c)
q1 = (-b-math.sqrt(d))/(2*a)
q2 = (-b+math.sqrt(d))/(2*a)
print("The quadratic equation are:",q1,q2)    
