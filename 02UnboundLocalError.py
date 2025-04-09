def unbound_example():
    """
    Demonstrates the use of the `nonlocal` keyword to modify a variable 
    in an outer (enclosing) function's scope from within an inner function.

    The function `unbound_example` defines a variable `x` in its local scope 
    and an inner function `inner` that modifies `x` using the `nonlocal` keyword. 
    The `nonlocal` keyword allows the inner function to access and modify the 
    variable `x` from the enclosing scope.

    Returns:
        int: The modified value of `x` after being incremented by 5 in the inner function.
    """
    x=10
    def inner():
        nonlocal x  # Declare x as nonlocal to access the outer scope variable
        x += 5 # Modify the value of x in the inner function
        return x
    return inner()  # Call the inner function and return its result
# Call the function and print the result
result = unbound_example()
print(result)  # Output: 15