# Create a variable and assign it the list [[0, 2], [4, 6], [8, 10], [12, 14]]
# Access the first list from the list of lists in step 1 by index then print it.
# Access the 14 from the list in step 1 then print it.
# Create a second variable and assign it the list ["chair", "table", "desk", "lamp", "bed"]
# Use a negative integer to access "chair" from the variable in step 4 by index then print it.
# Print "Most people own at least 2 chairs." by concatenating the 2 from the list in step 1 and the "chair" from the list in step 4 with "Most people own at least ", a space, and a period.
# Create a third variable and assign it the list [0.98, 8.76, 6.54, 4.32]
# Print the slice [8.76, 6.54, 4.32] from the variable you created in step 7.
# Print the slice [8.76, 6.54] from the variable you created in step 7.
# Print the slice [0.98, 8.76] from the variable you created in step 7.

pair_list = [[0, 2], [4, 6], [8, 10], [12, 14]]
print(pair_list[0])
print(pair_list[3][1])

pair_list_2 = ["chair", "table", "desk", "lamp", "bed"]
print(pair_list_2[-5])
print("Most people own at least {} {}(s).".format(pair_list[0][1], pair_list_2[0]))

pair_list_3 = [0.98, 8.76, 6.54, 4.32]
print(pair_list_3[1:])
print(pair_list_3[1:3])
print(pair_list_3[:2])


