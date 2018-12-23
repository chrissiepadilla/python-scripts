import sys
import os

sys.version

string = raw_input("Enter the string to search for: ")
path = raw_input("Enter the path of the directory to search within: ")

allFiles = dict ([(f, None) for f in os.listdir (path)])

found = [f for f in allFiles if string in open(f).read()]

if found:
    print("String found in file(s): ")
    print(found)
else:
    print("String no found in any file.")

#chrissiepadilla