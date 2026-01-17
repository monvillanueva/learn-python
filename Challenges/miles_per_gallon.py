import random
from math import floor

gas_tank_size_in_gallons = random.randint(10, 25)
total_miles_per_tank = random.randint(200, 400)


print("The gas tank holds " + str(gas_tank_size_in_gallons) + " gallons.")
print("Tha car can travel " + str(total_miles_per_tank) + " miles with a full tank.")
print("The miles per gallon is " + str(floor(total_miles_per_tank / gas_tank_size_in_gallons)))