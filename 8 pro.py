def is_valid_number(s):
    s = s.strip()

    # Define flags for components
    has_dot = False
    has_digit = False
    has_exponent = False

    # Iterate through each character in the string
    for i, char in enumerate(s):
        if char.isdigit():
            has_digit = True
        elif char in ['+', '-']:
            # Sign character can only appear at the beginning or after 'e'
            if i != 0 and s[i - 1] not in ['e', 'E']:
                return False
        elif char == '.':
            # Dot can only appear once and cannot appear after 'e'
            if has_dot or has_exponent:
                return False
            has_dot = True
        elif char in ['e', 'E']:
            # 'e' can only appear once and there must be at least one digit before it
            if has_exponent or not has_digit:
                return False
            has_exponent = True
            has_digit = False  # Reset digit flag for the part after 'e'
        else:
            return False  # Invalid character

    # The number is valid if it has at least one digit
    return has_digit

# Test Case
input_s = "e"
result = is_valid_number(input_s)
print(result)
