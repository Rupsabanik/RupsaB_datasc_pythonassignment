sum=0
num=int(input("Enter any number:"))
print("The sum of first odd N natural number")
for i in range(1,num+1):
    if i%2!=0:
        sum+=i
print(sum)
