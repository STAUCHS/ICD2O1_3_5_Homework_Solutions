#-------------------------------------------------------------------------
# Name:         Minutes
# Purpose:		Calculates the days, hours, and minutes given the total minutes
# Author:       Chen. C
# Created:      21/03/2024
#-------------------------------------------------------------------------

# Get input from user
minutes = int(input("Enter the number of minutes: "))

# Calculate the number of days, hours, and leftover minutes
days = minutes // 1440
hours = minutes % 1440 // 60
leftover_minutes = minutes % 1440 % 60

# Output the days, hours, and leftover minutes
print(minutes, "minutes =", days, "day(s),", hours, "hour(s),", leftover_minutes, "minute(s).")