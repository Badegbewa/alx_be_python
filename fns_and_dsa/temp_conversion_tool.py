FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return(fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celsius):
    return(celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

#User Interaction Now
try:
    temp_input = float(input("Enter the temperature to convert: "))
except ValueError:
    raise ValueError("Invalid temperature. Please enter a numeric value.")

unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

if unit == "F":
    result = convert_to_celsius(temp_input)
    print(f"{temp_input}°F is {result}°C")
elif unit == "C":
    result = convert_to_fahrenheit(temp_input)
    print(f"{temp_input}°C is {result}°F")
else:
    raise ValueError("Invalid unit. Please enter 'C' for celsius or 'F' for fahrenheit.")


