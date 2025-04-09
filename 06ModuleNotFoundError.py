try: 
    import nonexistentmodule
except ModuleNotFoundError:
    print("Module not found. Provide correct path.")
# The ModuleNotFoundError occurs when you try to import a module that doesn't exist in the specified path.

#import nonexistentmodule
#ModuleNotFoundError: No module named 'nonexistentmodule'
# The ModuleNotFoundError occurs when you try to import a module that doesn't exist in the specified path.  
# In this case, the module "nonexistentmodule" is not found, which raises the error.
# To avoid this error, make sure to check if the module exists before trying to import it.
# You can check the module's name and ensure it is spelled correctly.   
# You can also check if the module is installed in your Python environment using the pip list command.
# If the module is not installed, you can install it using pip install module_name. 
# If the module is installed, you can check if it is in your Python path using the sys.path variable.
# If the module is not in your Python path, you can add it using sys.path.append(module_path).  
# You can also check if the module is in your Python path using the sys.path variable.
# If the module is not in your Python path, you can add it using sys.path.append(module_path).
