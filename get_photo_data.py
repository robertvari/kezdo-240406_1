import os

# store the full path to the photo directory
# r= raw string
dir_path = r"D:\Work\_PythonSuli\kezdo-240406\alapok_1\photos"

# todo chech path validity
assert os.path.exists(dir_path), f"Folder does not exist: {dir_path}"

# todo check if path is a directory
assert os.path.isdir(dir_path), f"Path must be a directory: {dir_path}"



# todo collect all images (.jpg/.jpeg) from the directory
# todo collect data from files: file_name, file_size, pixel_size (width, height)
# todo write out data in json format