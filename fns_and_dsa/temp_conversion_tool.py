FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

try:
    tempre = float(input("Enter the temperature to convert: "))
except ValueError:
    raise ValueError("Invalid temperature. Please enter a numeric value.")

which = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
if which.lower() == 'c':
    print(f'{tempre}°C is {convert_to_fahrenheit(tempre)}°F')
elif which.lower() == 'f':
    print(f'{tempre}°F is {convert_to_celsius(tempre)}°C')
else:
    print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
