sub1=int(input("Enter 1st Subject number: "))
sub2=int(input("Enter 2nd Subject number: "))
sub3=int(input("Enter 3rd Subject number: "))
sub4=int(input("Enter 4th Subject number: "))
sub5=int(input("Enter 5th Subject number: "))
sub=sub1 + sub2 + sub3 + sub4 + sub5
per=sub/5
if (sub1 and sub2 and sub3 and sub4 and sub5)<=100:
    if sub>100:
        print("Result: pass")
        if per>=90:
            print("Grade: A+")
        elif per>=80:
            print(" Grade: A")
        elif per>=60:
            print("Grade: B+")
        elif per>=40:
            print("Grade: B")
        elif per>=20:
            print("Grade: c")
    else:
        print("Result: fail")
else:
    print("subject number cannot greater than 100")
