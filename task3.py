def digitalRoot(n):
    """
    This function calculates the digital root of a non-negative integer.
    """
    # Loop until the number is reduced to a single digit
    while n > 9:
        # Convert the number to a string to access its digits
        digits = str(n)
        # Sum up the digits of the number
        n = sum(int(digit) for digit in digits)
    # Return the final single-digit result
    return n