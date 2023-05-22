def factor():
    n = int(input("Enter a number:"))
    list = []
    for i in range(1,n):
        if(n%i==0):
            list.append(i)

    print(list)

factor()