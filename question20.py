def sum_of_list():
    num_list = input("Enter numbers separated by spaces: ").split()
    num_list = [float(num) for num in num_list]
    print(f"The sum of the list is: {sum(num_list)}")

sum_of_list()