# 20. SyntaxWarning
x =5
if x ==  5:
     print("Use  == not is for literals")


"""
Here’s an explanation of the SyntaxWarning in your code:

Explanation:
A SyntaxWarning is a type of warning in Python that indicates potential issues in your code that may not cause an immediate error but could lead to unexpected behavior.
In this case, the warning would occur if you used the is operator instead of == to compare the value of x with the literal 5.
Why?
The is operator checks for object identity, meaning it verifies if two variables point to the same object in memory.
The == operator checks for value equality, meaning it compares the actual values of the objects.
For literals like integers, strings, etc., you should use == to compare their values. Using is can lead to incorrect results because it depends on Python's internal object caching and memory management.
For example:

To avoid confusion and ensure correctness, always use == for value comparisons.
"""