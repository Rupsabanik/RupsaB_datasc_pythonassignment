a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
c=int(input("Enter 3rd number:"))
greatest=0
if a>b and a>c:
    print(a,"is greatest")
elif b>a and b>c:
    print(b,"is greatest")
else:
    print(c,"is greatest")
