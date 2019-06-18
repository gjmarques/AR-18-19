
from os import walk
import os

keyword = input("Search For?: ")  # ask the user for keyword, use raw_input() on Python 2.x
filedir =""
root_dir = "/mnt/c/Users/JoãoMonteiro/Desktop/AR/AR-18-19/ar-1819/project-files/dynamips"  # path to the root directory to search
for root, dirs, files in os.walk(root_dir, onerror=None):  # walk the root dir
    for filename in files:  # iterate over the files in the current dir
        file_path = os.path.join(root, filename)  # build the file path
        try:
            with open(file_path, "rb") as f:  # open the file for reading
                # read the file line by line
                for line in f:  # use: for i, line in enumerate(f) if you need line numbers
                    try:    
                        line = line.decode("utf-8")  # try to decode the contents to utf-8
                    except ValueError:  # decoding failed, skip the line
                        continue
                    if keyword in line:  # if the keyword exists on the current line...
                        print(file_path)  # print the file path
                        filedir=file_path
                        break  # no need to iterate over the rest of the file   
        except (IOError, OSError):  # ignore read and permission errors
            pass
searchprahse = "\\AR\\AR-18-19\\ar-1819\\project-files\dynamips\\"
almostthere=""
with open(filedir, 'r') as searchfile:
    for line in searchfile:
        if searchprahse in line:
            print (line)
            almostthere = line
            break

finalstring = almostthere+"\\configs"

filedir =""
root_dir = finalstring # path to the root directory to search
keyword = "interface"
for root, dirs, files in os.walk(root_dir, onerror=None):  # walk the root dir
    for filename in files:  # iterate over the files in the current dir
        file_path = os.path.join(root, filename)  # build the file path
        try:
            with open(file_path, "rb") as f:  # open the file for reading
                # read the file line by line
                for line in f:  # use: for i, line in enumerate(f) if you need line numbers
                    try:    
                        line = line.decode("utf-8")  # try to decode the contents to utf-8
                    except ValueError:  # decoding failed, skip the line
                        continue
                    if keyword in line:  # if the keyword exists on the current line...
                        print(file_path)  # print the file path
                        finalstring=file_path
                        break  # no need to iterate over the rest of the file   
        except (IOError, OSError):  # ignore read and permission errors
            pass


f = []
for (dirpath, dirnames, filenames) in walk(mypath):
    f.extend(filenames)
    break