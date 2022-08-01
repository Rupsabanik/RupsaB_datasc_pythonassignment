a=int(input("Enter 1st no:"))
b=int(input("Enter 2nd no:"))
n=complex(a,b)
print("The complex number:",n)
print("The real part: ",n.real)
print("The imaginary part: ",n.imag)
if n.real>n.imag:
    print(n.real,"is greater")
else:
    print(n.imag,"is greater")
