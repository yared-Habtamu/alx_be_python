num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")
if operation == '+':
    result=num1+num2
    print(f"The result is {result}.")
elif operation == '-':
    result=num-num2
    print(f"The result is {result}.")
elif operation == '*':
    result=num1*num2
    print(f"The result is {result}.")
if operation == '/':
    result=num1//num2
    if num2 != 0:
        print(f"The result is {result}.")
    else:
        print("Cannot divide by zero.")
