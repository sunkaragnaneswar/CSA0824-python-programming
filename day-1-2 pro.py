def sumsquare(l):
    odd_sum = 0
    even_sum = 0

    for num in l:
        if num % 2 == 0:
            even_sum += num**2
        else:
            odd_sum += num**2

    return [odd_sum, even_sum]

# Test Case
input_list = [1,2,3,4,5]
result = sumsquare(input_list)
print(result)
