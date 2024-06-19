def write_to_file():
    user_input = input("Enter a string: ")
    with open("output.txt", "w") as file:
        file.write(user_input)
    print("String written to output.txt")

write_to_file()