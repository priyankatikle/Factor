#palindrome
num=int(input("Enter the number:"))
r=0
t=num
while(num!=0):
    rem=int(num%10)
    r=(r*10)+rem
    num=int(num/10)
print(r)
if(t==r):
    print("palindrome")
else:
    print("Not palindrome")
print("completed program")

