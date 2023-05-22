def fib(n):
    result=[]
    a,b = 0,1
    while b<n:
        result.append(b)
        a,b = b,a+b
    print(result)


import module2 
fib(20)