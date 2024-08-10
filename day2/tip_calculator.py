#!/usr/bin/python

"""Tip calculator"""

#concepts
# Data types
# numbers
# Operations
# Type conversion
# f-string

print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
num_people = int(input('How many people to split the bill? '))
tip = (int(input("What percentage tip would you like to give? 10, 12, or 15? ")) * 0.01) * bill

total_bill = bill + tip
print(total_bill)



print(f'Each person should pay: ${round((total_bill / num_people), 1)}')