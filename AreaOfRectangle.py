#-------------------------------------------------------------------------
# Name:         Area of Rectangle
# Purpose:      Calculate the area of a rectangle
# Author:       Chen. C
# Created:      21/03/2024
#-------------------------------------------------------------------------

# Output title
print("** Area of a Rectangle Calculator **")

# Get the length and width from user
length_cm = float(input("Enter the length (cm): "))
width_cm = float(input("Enter the width (cm): "))

# Calculate area = l * w
area = length_cm * width_cm

# Output area
print("The area of your rectangle is", area, "cm^2")
print("The area of your rectangle is " + str(area) + " cm^2")
print(f"The area of your rectangel is {area} cm^2.")