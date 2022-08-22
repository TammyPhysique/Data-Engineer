numbers = [3, 7, 10, 40, 2, 4, 8]

max_value = None

for num in numbers:
    if (max_value is None or num > max_value):
        max_value = num

print(max_value)
