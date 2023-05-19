# Write function in python for the Factorial of Number

def fact():
    n=int(input("Enter the number:"))
    a=1
    for i in range(1,n+1):
       a=i*a
    print(a)


fact() 