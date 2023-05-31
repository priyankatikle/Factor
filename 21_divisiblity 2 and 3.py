#check weather no is divisible by 2 and 3 or both
num=int(input("Enter the number:"))
if(num%2==0):
    print("Number is divisible by 2")
    if(num%3==0):
        print("Number is divisible by 3")
        if(num%2==0 and num%3==0):
            print("Number is divisible by 2 and 3 both")
else:
    print("Number is neither divisible by 2 nor by 3")
