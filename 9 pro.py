# Get input from the user
fresh_loaves = int(input("Enter the number of fresh loaves purchased: "))
day_old_loaves = int(input("Enter the number of day-old loaves purchased: "))

# Constants
regular_price_per_loaf = 185
discount_percentage = 60

# Calculate prices
regular_price = fresh_loaves * regular_price_per_loaf
discounted_price = day_old_loaves * (regular_price_per_loaf * (1 - discount_percentage / 100))
total_price = regular_price + discounted_price

# Display the results
print(f"Regular price: Rs.{regular_price:.2f}")
print(f"Amount of new loaves: {regular_price:.2f}")
print(f"Amount of day-old loaves: {discounted_price:.2f}")
print(f"Total amount: Rs. {total_price:.2f}")
