def calculator():
    print("Welcome to the Calculator!")
    print("Choose an option:")
    print("1. Basic Calculator")
    print("2. Profit and Loss Calculator")
    
    choice = input("Enter 1 or 2: ")

    if choice == '1':
        num1 = float(input("Enter first number: "))
        op = input("Enter operation (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if op == '+':
            result = num1 + num2
            print(f"Result: {result}")
        elif op == '-':
            result = num1 - num2
            print(f"Result: {result}")
        elif op == '*':
            result = num1 * num2
            print(f"Result: {result}")
        elif op == '/':
            if num2 != 0:
                result = num1 / num2
                print(f"Result: {result}")
            else:
                print("Error: Cannot divide by zero!")
        else:
            print("Invalid operation!")

    elif choice == '2':
        cost_price = float(input("Enter Cost Price (CP): "))
        selling_price = float(input("Enter Selling Price (SP): "))

        if selling_price > cost_price:
            profit = selling_price - cost_price
            print(f"Profit: {profit}")
        elif cost_price > selling_price:
            loss = cost_price - selling_price
            print(f"Loss: {loss}")
        else:
            print("No Profit, No Loss.")

    else:
        print("Invalid choice. Please choose 1 or 2.")

# Run the calculator
calculator()
