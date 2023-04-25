# Check file is empty or not
import os

size = os.stat("test.txt").st_size
if size == 0:
    print("File is empty")
else:
    print("File is not empty")


