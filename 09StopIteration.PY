iterator = iter([])
#print(next(iterator))
# StopIteration error

"""
This script demonstrates the use of the `StopIteration` exception in Python. 
The `StopIteration` exception is raised to signal that there are no further 
items produced by an iterator. This is typically encountered when using the 
`next()` function on an iterator that has been exhausted.
Example:
    # Create an empty iterator
    # Attempt to retrieve the next item
    # Output:
    # No more items in the iterator.
Explanation:
    - An iterator is created using `iter([])`, which is an empty list.
    - The `next()` function is called to retrieve the next item from the iterator.
    - Since the iterator is empty, a `StopIteration` exception is raised.
    - The exception is caught in the `except` block, and a message is printed 
      indicating that there are no more items in the iterator.
"""
try:
    print(next(iterator))
except StopIteration:
    print("No more items in the iterator.")
# # Output: No more items in the iterator.

