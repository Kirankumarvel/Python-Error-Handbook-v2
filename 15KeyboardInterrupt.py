# while True:
#     pass  # Ctrl+C will raise KeyboardInterrupt
while True:
    pass  # Ctrl+C will raise KeyboardInterrupt


"""
# A KeyboardInterrupt occurs when the user interrupts the program's execution, typically by pressing Ctrl+C. This raises a KeyboardInterrupt exception, which can be caught and handled in Python code.
# The KeyboardInterrupt occurs when you manually interrupt a running Python program by pressing Ctrl+C (or Cmd+C on macOS) in the terminal. This sends a signal (SIGINT) to the Python interpreter, which raises the KeyboardInterrupt exception to stop the program.

In your code, the while True loop runs indefinitely, so pressing Ctrl+C is the only way to terminate it. However, if you want to handle the KeyboardInterrupt gracefully (e.g., perform cleanup or display a message before exiting), you can use a try-except block.

Here’s the updated code with comments explaining the solution:

Explanation:
try block: The infinite loop is placed inside the try block.
except KeyboardInterrupt: This catches the KeyboardInterrupt exception when Ctrl+C is pressed.
Graceful exit: Instead of abruptly terminating, the program prints a message and exits cleanly.
This approach ensures the program handles interruptions in a user-friendly way.
"""
try:
    while True:
        pass  # Ctrl+C will raise KeyboardInterrupt
except KeyboardInterrupt:
    print("\nProgram interrupted by user. Exiting...")
    # Perform any cleanup or final tasks here before exiting
    # For example, closing files, releasing resources, etc.
#     print("Cleanup done.")    
#     # Exit the program gracefully
#     exit(0)  # Optional: exit with a specific status code (0 for success)
# # Output: Program interrupted by user. Exiting...
# # Cleanup done.
