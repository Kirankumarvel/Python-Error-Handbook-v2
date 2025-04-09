# 4. FileNotFoundError
#open("non_existent_file.txt", "r")
#FileNotFoundError: [Errno 2] No such file or directory: 'non_existent_file.txt'        
# The FileNotFoundError occurs when you try to open a file that doesn't exist in the specified path.
# In this case, the file "non_existent_file.txt" is not found, which raises the error.
# To avoid this error, make sure to check if the file exists before trying to open it.  

# try:
#     open("non_existent_file.txt", "r")
# except FileNotFoundError as e:
#     print("File not found. Provide correct path.")
try:
    open("non_existent_file.txt", "r")
except FileNotFoundError as e:
    print("File not found. Provide correct path.")
