def count_sorted_vowel_strings(n):
    # Initialize counts for each vowel
    a_count, e_count, i_count, o_count, u_count = 1, 1, 1, 1, 1

    for _ in range(1, n):
        # Update counts based on the lexicographical order
        a_count = a_count + e_count + i_count + o_count + u_count
        e_count = e_count + i_count + o_count + u_count
        i_count = i_count + o_count + u_count
        o_count = o_count + u_count

    # Sum all counts to get the total number of lexicographically sorted strings
    return a_count + e_count + i_count + o_count + u_count

# Test Case
input_n = 2
result = count_sorted_vowel_strings(input_n)
print(result)
