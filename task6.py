def nextBigger(num):
    # Convert the number to a list of digits
    digits = list(str(num))
    
    # Starting from the right, find the first digit that is smaller than the digit to its right
    i = len(digits) - 2
    while i >= 0 and digits[i] >= digits[i+1]:
        i -= 1
    
    # If all digits are in non-increasing order, return -1
    if i < 0:
        return -1
    
    # Starting from the right, find the smallest digit to the right of the digit at i that is greater than it
    j = len(digits) - 1
    while j >= 0 and digits[j] <= digits[i]:
        j -= 1
    
    # Swap the digits at i and j
    digits[i], digits[j] = digits[j], digits[i]
    
    # Reverse the digits to the right of i
    digits[i+1:] = reversed(digits[i+1:])
    
    # Convert the list of digits back to an integer and return it
    return int(''.join(digits))

