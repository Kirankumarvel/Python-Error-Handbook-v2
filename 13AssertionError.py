# 13. AssertionError
assert 2 + 2 == 4  # Works
#assert 2 + 2 == 5  # Uncomment to raise AssertionError
# AssertionError: assert 2 + 2 == 5

"""
An AssertionError occurs when an assertion statement evaluates to False. In Python, the assert keyword is used to test whether a condition is True. If the condition is True, the program continues execution. If the condition is False, Python raises an AssertionError and halts the program (unless the error is caught and handled).

Explanation of the Code
Here, the assertion is commented out, so it won't execute. If you uncomment it, the assertion will check whether 2 + 2 == 5. Since this condition is False, Python will raise an AssertionError.

Why Does This Happen?
2 + 2 evaluates to 4.
The condition 4 == 5 is False.
Therefore, the assertion fails, and Python raises an AssertionError.
Purpose of Assertions
Assertions are typically used for debugging and testing. They help ensure that certain conditions hold true during execution. For example:

If x is not greater than 0, an AssertionError will occur with the message "x must be positive".

Key Points
Assertions are not meant for handling runtime errors in production code.
They are often used during development to catch bugs early.
Assertions can be disabled globally by running Python in optimized mode (python -O).

"""