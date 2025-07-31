# Add input
first_number =float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
operator = input("Enter an operation (+, -, *, /): ")

# Perform the calculation operation
if operator == '+':
    result = first_number + second_number
    print(f"{first_number} + {second_number} = {result}")
elif operator == '-':
    result = first_number - second_number
    print(f"{first_number} - {second_number} = {result}")
elif operator == '*':
    result = first_number * second_number
    print(f"{first_number} * {second_number} = {result}")
elif operator == '/':
    if second_number != 0:
        result = first_number / second_number
        print(f"{first_number} / {second_number} = {result}")
    else:
        print("❌ Error: Division by zero is not allowed.")
else:
    print("❌ Invalid operator! Please use +, -, *, or /.")