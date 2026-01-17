
# penne = 1668 / 100
# sauce = 6.98
# garlic = 16.78
# seasoning = 15.26
# baguettes = 3.00
# meatballs = 4.39

# method 1

penne = 16.68
sauce = 6.98
garlic = 16.78
seasoning = 15.26
baguettes = 3.00
meatballs = 4.39

method1 = round(penne + sauce + garlic + seasoning + baguettes + meatballs, 2)
print(method1)

# method 2
penne = 16.68 * 100
sauce = 6.98 * 100
garlic = 16.78 * 100
seasoning = 15.26 * 100
baguettes = 3.00 * 100
meatballs = 4.39 * 100

method2 = ((penne + sauce + garlic + seasoning + baguettes + meatballs) / 100)
print(method2)
