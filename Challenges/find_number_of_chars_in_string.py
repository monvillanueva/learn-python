user_string = str(input("Enter a string: "))
char_count = 0

print(user_string)

for letter in user_string:
    char_count += 1

print("The string has " + str(char_count) + " characters")