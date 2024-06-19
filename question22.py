def min_max_values():
    numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
    min_val = min(numbers)
    max_val = max(numbers)
    print(f"The minimum value is: {min_val}")
    print(f"The maximum value is: {max_val}")

min_max_values()