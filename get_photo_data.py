import os, json
from PIL import Image


# store the full path to the photo directory
# r= raw string
dir_path = r"D:\Work\_PythonSuli\kezdo-240406\alapok_1\photos"

# chech path validity
assert os.path.exists(dir_path), f"Folder does not exist: {dir_path}"

# check if path is a directory
assert os.path.isdir(dir_path), f"Path must be a directory: {dir_path}"

# collect all images (.jpg) from the directory
folder_content = os.listdir(dir_path)
print(f"File count: {len(folder_content)}")

photo_files = []
for i in folder_content:
    if not i.endswith(".jpg") and not i.endswith(".jpeg"):
        continue

    photo_files.append(i)


# collect data from files: file_name, file_size, pixel_size (width, height)
photo_data = {}
for i in photo_files:
    file_name = os.path.join(dir_path, i)
    file_size = os.path.getsize(file_name) / (1024*1024)

    img = Image.open(file_name)
    pixel_size = img.size

    photo_data[file_name] = {"file_size": file_size, "pixel_size": pixel_size}

# todo write out data in json format