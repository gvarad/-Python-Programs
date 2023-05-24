fileptr = open('myfile.txt','r')

for i in fileptr:
    print(i)

import os

print(os.getcwd())