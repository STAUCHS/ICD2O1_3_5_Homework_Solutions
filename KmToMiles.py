#-------------------------------------------------------------------------
# Name:         Km to Miles
# Purpose:		Converts kilometers to miles
# Author:       Chen. C
# Created:      21/03/2024
#-------------------------------------------------------------------------

# Output title
print("** Km to Miles Converter **")

# Get the kilometers from user
distance_km = float(input("Enter the distance in km: "))

# Convert km to miles
distance_miles = distance_km * 0.621371
distance_miles = round(distance_miles, 2)

# Output miles
print(distance_km, "km is", distance_miles, "miles.")
print(str(distance_km) + "km is" + str(distance_miles) + "miles.")
print(f"{distance_km}km is {distance_miles}miles.")