# this script receive user's directory input and give list of file in directory as output
import os

dir = input("insert the directory:")
dir_list = os.listdir(dir)
print(dir_list)

