# 11. MemoryError
# a = [1] * (10**10)  # Try allocating huge memory
# # MemoryError: list too large

import threading

def worker():
    print("Worker thread is running")

# Create a thread object
thread = threading.Thread(target=worker)

# Start the thread
thread.start()

# Attempt to start the thread again (this will raise a RuntimeError)
try:
    thread.start()
except RuntimeError as e:
    print(f"RuntimeError occurred: {e}")

# Attempt to create a large list (this may raise a MemoryError)
try:
    a = [1] * (10**10)
except MemoryError as e:
    print(f"MemoryError occurred: {e}")
