import shutil
import os

from_dir = "/home/arshiaj87/Python_Projects/HW_102/Downloads"
to_dir = "/home/arshiaj87/Python_Projects/HW_102"

list_of_files = os.listdir(from_dir)

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)
    if extension == "":
        continue
    if extension in ['.gif', '.png', '.jpeg', '.jpg', '.jfif']:
        path1 = from_dir + "/" + file_name
        path2 = to_dir + "/" + "Document_Files"
        path3 = path2 + "/" + file_name

        if os.path.exists(path2):
            print("Moving" + file_name + "......")
            shutil.move(path1, path3)

        else:
            os.makedirs(path2)
            print("Moving" + file_name + "......")
            shutil.move(path1, path3)