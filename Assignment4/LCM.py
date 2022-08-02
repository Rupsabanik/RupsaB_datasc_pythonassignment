a = float(input("Enter the First Value a: "))
b = float(input("Enter the Second Value b: "))
if(a>b):
    maximum=a
else:
    maximum=b
while(True):
    if(maximum % a == 0 and maximum % b == 0):
        print("LCM:",maximum)
        break;
    maximum = maximum + 1
