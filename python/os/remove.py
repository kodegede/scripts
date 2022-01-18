#os.remove used to delete a file in directory

from nturl2path import pathname2url
import os

file = "testdelete.py"
directory = "./"

path = os.path.join(directory, file)
os.remove(path)