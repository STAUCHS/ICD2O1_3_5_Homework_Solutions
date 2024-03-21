#-------------------------------------------------------------------------
# Name:         Average
# Purpose:		Calculate the average a student's 4 marks
# Author:       Chen. C
# Created:      21/03/2024
#-------------------------------------------------------------------------

# Output title
print("** Average Calculator **")

# Get 4 marks from the user
mark_one = float(input("Enter your mark for Course 1: "))
mark_two = float(input("Enter your mark for Course 2: "))
mark_three = float(input("Enter your mark for Course 3: "))
mark_four = float(input("Enter your mark for Course 4: "))

# Calculate the average
average = (mark_one + mark_two + mark_three + mark_four) / 4
average = round(average)
average = int(average)

# Output the average
print("Your average is", average, "%.")