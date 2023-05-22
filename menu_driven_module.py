import Function_module2

while True:
    print("\nMAIN MENU")
    print("1. Arithmetic Operations")
    print("2. Factorial of Nummber")
    print("3. Prime Number")
    print("4. Fibonacci Series")
    print("5. Armstrong Number")
    print("6. Factor of number")
    print("7. Exit")
    choice1 = int(input("Enter the Choice:"))

    if choice1 == 1:
        while True:
            print("\nCALCULATE PARAMETER")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Exit")
            choice2 = int(input("Enter the Choice:"))

            if choice2 == 1:
                a = int(input("Enter First Number:"))
                b = int(input("Enter Second Number:"))
                Function_module2.add(a, b)

            elif choice2 == 2:
                a = int(input("Enter First Number:"))
                b = int(input("Enter Second Number:"))
                Function_module2.sub(a, b)

            elif choice2 == 3:
                a = int(input("Enter First Number:"))
                b = int(input("Enter Second Number:"))
                Function_module2.mul(a, b)

            elif choice2 == 4:
                a = int(input("Enter First Number:"))
                b = int(input("Enter Second Number:"))
                Function_module2.div(a, b)

            elif choice2 == 5:
                print("Arithmetic Operations End Here!!!")
                break

            else:
                print("Oops! Incorrect Choice.")

    elif choice1 == 2:
        Function_module2.fact()

    elif choice1 == 3:
        Function_module2.prime()

    elif choice1 == 4:
        Function_module2.fib()

    elif choice1 == 5:
        Function_module2.arm()

    elif choice1 == 6:
        Function_module2.factor()

    elif choice1 == 7:
        break
