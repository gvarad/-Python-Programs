fileptr = open("myfile.txt",'r')

print("The filepointer is at byte:",fileptr.tell())

content = fileptr.read()

print("After reading, the filepointer is at byte:",fileptr.tell())