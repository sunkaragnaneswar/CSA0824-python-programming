def is_happy(n):
    def get_next(num):
        sum_of_squares = 0
        while num > 0:
            digit = num % 10
            sum_of_squares += digit ** 2
            num //= 10
        return sum_of_squares

    seen = set()

    while n != 1 and n not in seen:
        seen.add(n)
        n = get_next(n)

    return n == 1

# Test Case
input_number = 2
result = is_happy(input_number)
print(result)
