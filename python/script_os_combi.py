#this script use all of function of os module that I have learned before

import os
from random import choice

print("script os testing:")
print("a. getcwd")
print("a. chdir")

cho = input("insert the choice:")
dir = os.getcwd()


if cho=='a':
    print('current working directory is:', dir)
if cho=='b':  
    print(os.getcwd())
