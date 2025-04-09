# Example of RuntimeError: maximum recursion depth exceeded
def infinite_recur():
    print("Calling infinite_recur()")
    infinite_recur()  # Recursive call to demonstrate infinite recursion


# Uncomment the following line to test the RuntimeError

# infinite_recur()
