def simple_calculator():
    # Prompt user for input
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    print("Select the operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    operation = input("Enter operation (1/2/3/4): ")
    
    # Perform calculation based on user input
    if operation == '1':
        result = num1 + num2
        print(f"The result of {num1} + {num2} is: {result}")
        
    elif operation == '2':
        result = num1 - num2
        print(f"The result of {num1} - {num2} is: {result}")
        
    elif operation == '3':
        result = num1 * num2
        print(f"The result of {num1} * {num2} is: {result}")
        
    elif operation == '4':
        if num2 != 0:
            result = num1 / num2
            print(f"The result of {num1} / {num2} is: {result}")
        else:
            print("Error! Division by zero.")
    else:
        print("Invalid operation selected.")

# Run the calculator
simple_calculator()
