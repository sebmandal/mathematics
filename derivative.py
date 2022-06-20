def derive(*args):
    """
    This function returns the derivative of an equation
    Example args: [1, 4, 2] # A list dynamically made of all the provided params
    Args are dynamic, and work no matter the length of the list
    """
    
    res = []
    for index, arg in enumerate(args):
        """
        Looping through the provided parameters, figuring out the
        exponent of the current loop item, multiplying it with
        the value of the current item, then adding it to the
        result array
        """
        
        if index == len(args) - 1:
            """
            If this is the last item, it's a constant, no need to
            add it, then we break the loop
            """
            break
            
        res.append(float(arg) * (len(args) - (index + 1)))
    
    return res

"""
Example input

input   -> 2, 3, -1, 4 (2x^3 + 3x^2 - x + 4)
output  -> 6, 6, -1    (6x^2 + 6x - 1)
"""
print(derivate(2, 3, -1, 4))
