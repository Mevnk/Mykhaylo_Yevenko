def firstNonRepeatingLetter(s):
    """
    This function takes a string input, and returns the first character that is not repeated anywhere in the string.
    """
    # Loop through each character in the string
    for char in s:
        # If the character appears only once in the string
        if s.lower().count(char.lower()) == 1:
            # Return the original character in the correct case
            return char
    # If no non-repeating characters are found, return an empty string
    return ""