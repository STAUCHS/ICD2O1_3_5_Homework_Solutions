#-------------------------------------------------------------------------
# Name:         Volume of a Cone
# Purpose:		Calculates the volume of a cone
# Author:       Chen. C
# Created:      21/03/2024
#-------------------------------------------------------------------------

import math

# Output title
print("** Volume of a Cone Calculator **")

# Get the radius and height
radius_cm = float(input("Enter the radius (cm): "))
height_cm = float(input("Enter the height (cm): "))

# Calculate the volume
volume = (math.pi * (radius_cm ** 2) * height_cm) / 3
volume = round(volume, 1)

# Output volume
print("The volume of your cone is", volume, "cm^3.")