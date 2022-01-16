# os.makedirs() used to create a directory recursively
# usecase: os.mkdir('parent_directory', 'directory_name')

import os

#for example, I want to create b directory in "a" parent directory, but "a" is not created yet. makedirs will create "a" and "b"
directory = "b"
parent_dir = "./a" 
path = os.path.join(parent_dir, directory)
os.makedirs(path)
print("Directory '% s' created" % directory)