kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles*1.61
kilometers_to_miles = kilometers/1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

# round() function. Its job is to round the outputted result to the number of decimal places specified in the parentheses, 
# and return a float (inside the round() function you can find the variable name, a comma, and the number of decimal places we're aiming for). 