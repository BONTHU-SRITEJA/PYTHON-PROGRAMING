#To find the Factorial of a given number

n=int(input("ENTER THE NUMBER:"))

fact=1

for i in range(1,n+1):
	fact=fact*i

print("factorial of the given number is :",fact)
