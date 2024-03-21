#-------------------------------------------------------------------------
# Name:         Fahrenheit to Celsius
# Purpose:		Converts the temperature in Fahrenheit to Celsius
# Author:       Chen. C
# Created:      21/03/2024
#-------------------------------------------------------------------------

# Output title
print("** Fahrenheit to Celsius Converter **")

# Get temp in fahrenheit from use
temp_fahrenheit = float(input("Enter the temperature in Fahrenheit: "))

# Convert fahrenheit to celsius
temp_celsius = (5/9) * (temp_fahrenheit - 32)
temp_celsius = round(temp_celsius)
temp_celsius = int(temp_celsius)

# Output celsius
print(temp_fahrenheit, "degrees Fahrenheit is", temp_celsius, "degrees celsius.")