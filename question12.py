def sum_of_digits():
    num = input("Enter a number: ")
    sum_digits = sum(int(digit) for digit in num)
    print(f"The sum of the digits is: {sum_digits}")

sum_of_digits()