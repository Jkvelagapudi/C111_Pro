import os
import shutil

from_dir = 'C:/Users/jkvel/Downloads'
to_dir = 'C:/Users/jkvel/OneDrive/Desktop/Doc_Files_Pro_111'

list_of_files = os.listdir(from_dir)

print(list_of_files)

for i in list_of_files:
    root,exd = os.path.splitext(i)
    print(root,exd)