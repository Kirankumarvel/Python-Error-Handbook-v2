# 23. OSError
"""
This script demonstrates the handling of an OSError in Python.

An OSError is raised when a system-related error occurs, such as 
issues with file access, invalid file paths, or other operating 
system-related problems. In this example, an attempt is made to 
open a file using an invalid file path, which triggers an OSError. 
The exception is caught, and a user-friendly message is displayed 
to indicate a general file access error.
"""

try:
    open("///invalid///path")
except OSError:
    print("General file access error")