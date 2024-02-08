def max_area(height):
    max_area_val = 0
    left, right = 0, len(height) - 1

    while left < right:
        h = min(height[left], height[right])
        w = right - left
        max_area_val = max(max_area_val, h * w)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area_val

# Test Case
input_array = [1, 5, 4, 3]
result = max_area(input_array)
print(result)  # Output: 6
