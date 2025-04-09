# 25. NameError in closure
def outer():
    x = 10
    def inner():
        print(x)  # Works
    inner()

# Uncomment and run each block one-by-one to see real behavior
outer()  # This will not raise an error