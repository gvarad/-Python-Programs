# Arithmetic Operation

def add(a, b):
    sum = a+b
    print("Sum:", sum)


def sub(a, b):
    sub = a-b
    print("Subtraction:", sub)


def mul(a, b):
    mul = a*b
    print("Multiplication:", mul)


def div(a, b):
    div = a/b
    print("Division:", div)


# # Driver Code
# a = int(input("Enter first number:"))
# b = int(input("Enter second number:"))

# add(a, b)
# sub(a, b)
# mul(a, b)
# div(a, b)

# # Factorial Number


def fact():
    n = int(input("Enter the number to check factorial:"))
    a = 1
    for i in range(1, n+1):
        a = i*a
    print("Factorial of", n, "is", a)


# # Prime number


def prime():
    n = int(input('Enter a number to check prime:'))
    m = 0
    for i in range(2, n):
        if (n % i == 0):
            m = 1
            break
    if m:
        print(n, "is not prime")
    else:
        print(n, "is prime")


# # Fibonacci Series


def fib():
    n = int(input("Enter a range:"))
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    print(result)


# # Armstrong Number


def arm():
    num = int(input("Enter a number to check armstrong number:"))
    n = num
    sum = 0
    while n > 0:
        rem = int(n % 10)
        n = int(n/10)
        sum = int(sum+rem*rem*rem)

    if num == sum:
        print(num, "is armstrong number")
    else:
        print(num, "is not armstrong number")


# # Factors


def factor():
    n = int(input("Enter a number to check Factors:"))
    list = []
    for i in range(1, n):
        if (n % i == 0):
            list.append(i)

    print(list)
