# Create a variable called the_string and assign it the string "North Dakota".
the_string = "North Dakota"

# Call .rjust() on the_string with 17 as its argument and print() the result.
print("1: " + the_string.rjust(17))
# Call .ljust() on the_string with the arguments 17 and "*" then print() the result.
print("2: " + the_string.ljust(17, "*"))
# Create a variable called center_plus and assign it the result of .center() being called on the_string with 16 and "+" as arguments.
center_plus = the_string.center(16, "+")
# Use print() to display the string assigned to center_plus.
print("3: " + center_plus)
# Call .lstrip() on the_string to remove "North" then print() the result.
print("4: " + the_string.lstrip("North"))
# Call .rstrip() on center_plus with "+" as its argument and print() the result.
print("5: " + center_plus.rstrip("+"))
# Call .strip() on center_plus with "+" as its argument and print() the result.
print("6: " + center_plus.strip("+"))
# Call .replace() on the_string and replace "North" with "South".  print() the result.
print("7: " + "North Dakota".replace("North", "South"))