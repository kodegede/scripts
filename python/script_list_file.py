# this script receive user's directory input and give list of file in directory as output
# tested on 2022/01/19
 
import os

dir = input("insert the directory:")
dir_list = os.listdir(dir)

if len(os.listdir(dir)) == 0:
    print("Directory is empty")
else:    
    print(dir_list)