# Write function in python for the Prime Number

def prime():
    n=int(input('Enter a number:'))
    m=0
    for i in range(2,n):
        if(n%i==0):
            m=1
            break
    if m:
        print(n,"is not prime")
    else:
        print(n,"is prime")

prime()