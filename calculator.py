print("1 - ADD")
print("2 - SUBTRACT")
print("3 - MULTIPLY")
print("4 - DIVIDE")

while True:
    try:
        option = int(input("Select an operation to perform: "))
        if option in [1, 2, 3, 4]:
            num1 = int(input("Enter First Number: "))
            num2 = int(input("Enter Second Number: "))

            if option == 1:
                result = num1 + num2
            elif option == 2:
                result = num1 - num2
            elif option == 3:
                result = num1 * num2
            elif option == 4:
                result = num1 // num2

            print("The Result is {}".format(result))
            break  # Exit the loop after successful calculation
        else:
            print("Invalid option. Please select a valid operation.")
    except ValueError:
        print("Invalid input. Please enter a number.")
