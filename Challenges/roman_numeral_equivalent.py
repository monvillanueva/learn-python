import random

random_num = random.randint(1, 10)

roman_numeral = ""

if random_num == 10:
    roman_numeral = "X"
elif random_num == 9:
    roman_numeral = "IX"
elif random_num == 8:
    roman_numeral = "VIII"
elif random_num == 7:
    roman_numeral = "VII"
elif random_num == 6:
    roman_numeral = "VI"
elif random_num == 5:
    roman_numeral = "V"
elif random_num == 4:
    roman_numeral = "IV"
elif random_num == 3:
    roman_numeral = "III"
elif random_num == 2:
    roman_numeral = "II"
elif random_num == 1:
    roman_numeral = "I"

print("The roman number equivalent of " + str(random_num) + " is: " + roman_numeral)
