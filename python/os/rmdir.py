#os.rmdir used to remove empty directory and will give error output if directory is not empty

import os
directory = "testdelete"
parent = "./"

path = os.path.join(parent, directory)

os.rmdir(path)