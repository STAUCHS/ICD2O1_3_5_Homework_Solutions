#-------------------------------------------------------------------------
# Name:         Circumference
# Purpose:		Calculates the circumference of a circle
# Author:       Chen. C
# Created:      21/03/2024
#-------------------------------------------------------------------------

import math

# Output title
print("** Circumference Calculator **")

# Get radius from user
radius_cm = float(input("Enter the radius (cm): "))

# Calculate the circumference
circumference = 2 * math.pi * radius_cm
circumference = round(circumference, 2)

# Output the circumference
print("The circumference of your circle is", circumference, "cm.")