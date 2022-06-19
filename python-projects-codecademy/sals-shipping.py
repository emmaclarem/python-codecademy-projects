#Objective: Sal runs the biggest shipping company in the tri-county area, Sal’s Shippers. Sal wants to make sure that every single one of his customers has the best, and most affordable experience shipping their packages. Write a shipping.py Python program that asks the user for the weight of their package and then tells them which method of shipping is cheapest and how much it will cost to ship their package using Sal’s Shippers.

weight = 41.5

# ground shipping
if weight <= 2:
  ground_cost = (weight * 1.5) + 20
elif weight <= 6:
  ground_cost = (weight * 3) + 20
elif weight <= 10:
  ground_cost = (weight * 4) + 20
else:
  ground_cost = (weight * 4.75) + 20
print("Ground shipping cost: ")
print(ground_cost)

# premium ground shipping
premium_ground_shipping = 125.0
print("Premium ground shipping cost: ")
print(premium_ground_shipping)

# drone shipping
if weight <= 2:
  drone_cost = weight * 4.5
elif weight <= 6:
  drone_cost = weight * 9
elif weight <= 10:
  drone_cost = weight * 12
else:
  drone_cost = weight * 14.25
print("Drone shipping cost: ")
print(drone_cost)
