import os
parents = input("Enter parents file: ")

for root, dirs, files in os.walk(parents):
    for filename in files:
        print(filename)