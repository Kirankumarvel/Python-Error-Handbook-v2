#open("/home/user/folder/", "r")
# # IsADirectoryError: [Errno 21] Is a directory: '/home/user/folder/'
# # The IsADirectoryError occurs when you try to open a directory as if it were a file. 
# # In this case, you are trying to open the directory "/home/user/folder/" for reading, but it is a directory, not a file.
# # To avoid this error, make sure to check if the path you are trying to open is a file and not a directory.
# # You can check the file type using the os.path.isfile() function in Python.  