sub1=int(input("Enter 1st Subject number: "))
sub2=int(input("Enter 2nd Subject number: "))
sub3=int(input("Enter 3rd Subject number: "))
sub4=int(input("Enter 4th Subject number: "))
sub5=int(input("Enter 5th Subject number: "))
Total=(sub1 + sub2 + sub3 + sub4 + sub5)
avg=Total/5
per=(Total/500)*100
if Total<500:
    print("1st division\nResult:pass\npercentage=",per)
elif Total<=420:
    print("2nd division\nResult:pass\npercentage=",per)
elif Total<=250:
    print("3rd division\nResult:pass\npercentage=",per)
else:
    print("Result: fail")
