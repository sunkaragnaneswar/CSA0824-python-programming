def isomorphic_strings(s, t):
    if len(s) != len(t):
        return False
    
    mapping_s_t = {}
    mapping_t_s = {}

    for char_s, char_t in zip(s, t):
        if char_s in mapping_s_t:
            if mapping_s_t[char_s] != char_t:
                return False
        else:
            mapping_s_t[char_s] = char_t

        if char_t in mapping_t_s:
            if mapping_t_s[char_t] != char_s:
                return False
        else:
            mapping_t_s[char_t] = char_s

    return True

# Test Cases
print(isomorphic_strings("foo", "bar"))  # Output: True
print(isomorphic_strings("egg", "add"))  # Output: True
print(isomorphic_strings("paper", "title"))  # Output: True
print(isomorphic_strings("fry", "sky"))  # Output: True
print(isomorphic_strings("apples", "apple"))  # Output: True
