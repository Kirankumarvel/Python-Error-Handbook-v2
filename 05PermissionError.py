import os

try:
	# Specify the file path
	file_path = "05test.txt"

	# Check if the file is writable
	if os.access(file_path, os.W_OK) or not os.path.exists(file_path):
		with open(file_path, "w") as file:
			file.write("This is a test.")
	else:
		print(f"Error: You do not have write access to '{file_path}'.")
except PermissionError:
	print("Permission denied: You do not have the necessary permissions to write to this file.")
except FileNotFoundError:
	print("File not found: The specified file path does not exist.")
except Exception as e:
	print(f"An unexpected error occurred: {e}")
	
# fix: use a file you have write access to
#open("test.txt", "w")
# FileNotFoundError: [Errno 13] Permission denied: '/etc/shadow'    
# # The PermissionError occurs when you try to access a file or directory without the necessary permissions.
# # In this case, you are trying to open the file "/etc/shadow" for writing, but you don't have permission to do so.
# # To avoid this error, make sure you have the necessary permissions to access the file or directory you are trying to work with.
# # You can check the file permissions using the ls -l command in the terminal.
# # If you don't have the necessary permissions, you can either:    
# # 1. Change the file permissions using the chmod command (if you have the necessary privileges).
# # 2. Run your script with elevated privileges (e.g., using sudo in Linux).
# # 3. Use a different file or directory that you have permission to access.
# # 4. Use a different file or directory that you have permission to access.
# # 5. Check the file path and ensure it is correct.
# # 6. Use a different file or directory that you have permission to access.    
