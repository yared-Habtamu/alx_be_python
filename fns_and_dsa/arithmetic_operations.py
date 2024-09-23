from . import main
def perform_operation(*num1,*num2,*operation):
    if operation == 'add':
        return num1+num2
    elif operation == 'substract':
        return num1-num2
    elif operation == 'multiply':
        return num1*num2
    else:
        if num2 != 0:
            return num1/num2
        return "You can't divide a number by 0"
