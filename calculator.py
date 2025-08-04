def calculator(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operation"

print(calculator(10, 5, 'add'))
print(calculator(10, 5, 'subtract'))
print(calculator(10, 5, 'multiply'))
print(calculator(10, 5, 'divide'))
print(calculator(10, 0, 'divide'))
print(calculator(10, 5, 'invalid'))
