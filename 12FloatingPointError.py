import numpy as np
# import numpy as np
np.seterr(all='raise') # Raise an error for all floating point errors
# np.seterr(all='warn') # Raise a warning for all floating point errors 
# np.seterr(all='ignore') # Ignore all floating point errors
# np.seterr(all='call') # Call a function for all floating point errors
# np.seterr(all='print') # Print a message for all floating point errors
# np.seterr(all='log') # Log a message for all floating point errors

#np.divide(1.0, 0.0) # This will raise a FloatingPointError

try:
    np.divide(1.0, 0.0)
except FloatingPointError:
    print("Handle divide-by-zero in float operation")

