#-------------------------------------------------------------------------
# Name:         Pythagorean Theorem
# Purpose:		Calculates the hypotenuse of a right triangle
# Author:       Chen. C
# Created:      21/03/2024
#-------------------------------------------------------------------------

import math

# Output title
print("** Hypotenuse Calculator **")

# Get side a and b from user
side_a = float(input("Enter the length of side a: "))
side_b = float(input("Enter the lenght of side b: "))

# Calculate the hypotenuse using Pythagorean Theorem
hypotenuse = math.sqrt(side_a ** 2 + side_b ** 2)
hypotenuse = round(hypotenuse, 1)

# Output hypotenuse
print("The hypotenuse of a right triangle with legs", side_a, "and", side_b, "is", hypotenuse, "units.")