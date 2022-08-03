num=1000
for i in range(1,num+1):
    temp=i
    sum=0
    while(temp>0):
        rem=temp%10
        sum=sum+(rem**3)
        temp=temp//10
    if(sum==i):
        print(sum,end=" ")
