n=int(input("enter n value="))
sum=0
temp=n
while n>0:
        rem=n%10
        sum=sum+rem**3
        n=n//10
if (sum==temp):
	print("armstrong number")
else:
	print("not a armstrong number")

