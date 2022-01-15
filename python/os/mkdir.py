# os.mkdir() used to create a directory
# usecase: os.mkdir('parent_directory', 'directory_name')

import os
 
new_directory = "New Directory"
parent_directory = "./"
path = os.path.join(parent_directory, new_directory)
os.mkdir(path)
print("Directory '% s' created" % new_directory)
