def derivate(*args):
    """
    This function returns the derivative of an equation
    Example args: [1, 4, 2] # A list dynamically made of all the provided params
    Args are dynamic, and work no matter the length of the list
    """
    res = []
    for index, arg in enumerate(args):
        if index == len(args) - 1:
            break
        res.append(float(arg) * (len(args) - (index + 1)))
    return res

print(derivate(2, 3, -1, 4))
# input   -> 2, 3, -1, 4 # 2x^3 + 3x^2 - x + 4
# output  -> 6, 6, -1    # 6x^2 + 6x - 1
