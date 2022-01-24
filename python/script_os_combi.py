#this script use all of function of os module that I have learned before

import os
from random import choice

print("script os testing:")
print("a. getcwd")
print("b. chdir to ../")
print("c. listdir")

cho = input("insert the choice:")
folder = input ("insert directory:")
dir = os.getcwd(folder)
dir_list = os.listdir(folder)


if cho=='a':
    print('current working directory is:', dir)
if cho=='b':  
    os.chdir('../')
    print('current working directory is:', dir)
if cho=='c': 
    print(dir_list) 

