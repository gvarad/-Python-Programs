a = int(input("Enter a 1st number:"))
b = int(input("Enter a 2nd number:"))
def add():
    
    return a+b
    # print("Sum:",sum)

a1 =add()

fileptr = open("add1.txt","w")

fileptr.write("a="+str(a)+'\n')
fileptr.write("b="+str(b)+'\n')
fileptr.write("Sum="+str(a1)+'\n')
fileptr.close()