def is_palindrome(x):
    # Convert integer to string for easier comparison
    str_x = str(x)
    
    # Check if the string is the same when read backward
    return str_x == str_x[::-1]

# Test Case
input_number = 123
result = is_palindrome(input_number)
print(result)
