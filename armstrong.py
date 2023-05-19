# Write function in python for the Armstrong number

def arm(n):
    
    sum = 0
    while n>0:
        rem=int(n%10)
        n=int(n/10)
        sum=int(sum+rem*rem*rem)
    
    if num==sum:
        print("The number is armstrong number")
    else:
        print("The number not armstrong number")

num=int(input("Enter a number:"))
arm(num)