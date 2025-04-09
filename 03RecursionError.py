# 3. RecursionError
def infinite_recur(n):
    if n == 0:  # Base condition to stop recursion
        return "Recursion ends"
    return infinite_recur(n - 1)
# fix: add base condition
# def safe_recur(n):
#     if n == 0:
#         return 0
#     return safe_recur(n-1)

# # RecursionError: maximum recursion depth exceeded in comparison
# # This error occurs when a recursive function exceeds the maximum recursion depth allowed by Python.      
# # In this case, the infinite_recur function calls itself indefinitely without a base case to stop the recursion.
# # To avoid this error, make sure to include a base case in your recursive function that stops the recursion when a certain condition is met.
# # For example, in the safe_recur function, the recursion stops when n reaches 0.
# # This way, the function will not exceed the maximum recursion depth and will return a value instead of raising an error. 
# # RecursionError occurs when a recursive function exceeds the maximum recursion depth allowed by Python.
# # This can happen if the recursion does not have a proper base case or if the recursion depth is too high.
# # To fix this error, you can either:
# # 1. Add a base case to your recursive function to stop the recursion when a certain condition is met.
# # 2. Increase the maximum recursion depth using the sys module (not recommended for most cases).
# # 3. Refactor your code to use an iterative approach instead of recursion.
# # Here is an example of a recursive function that causes RecursionError:
# def infinite_recur():
#     return infinite_recur()
# # This function calls itself indefinitely without a base case to stop the recursion.
# # To fix this, you can add a base case:
# def safe_recur(n):
#     if n == 0:    
#         return 0
#     return safe_recur(n-1)
# # This function will stop the recursion when n reaches 0.
# # You can also increase the maximum recursion depth using the sys module:
def safe_recur(n):
     if n == 0:    
         return 0
     return safe_recur(n-1)