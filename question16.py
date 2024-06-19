def char_frequency():
    user_input = input("Enter a string: ")
    frequency = {}
    for char in user_input:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    print("Character frequency:")
    for char, freq in frequency.items():
        print(f"{char}: {freq}")

char_frequency()