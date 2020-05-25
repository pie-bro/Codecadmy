"""
Sal's Shipping
Sal runs the biggest shipping company in the tri-county area, Sal’s Shippers. Sal wants to make sure that every single one of his customers has the best, and most affordable experience shipping their packages. In this project, you’ll build a program that will take the weight of a package and determine the cheapest way to ship that package using Sal’s Shippers.

Sal’s Shippers has several different options for a customer to ship their package. They have ground shipping, which is a small flat charge plus a rate based on the weight of your package. Premium ground shipping, which is a much higher flat charge, but you aren’t charged for weight. They recently also implemented drone shipping, which has no flat charge, but the rate based on weight is triple the rate of ground shipping.

Here are the prices:

Ground Shipping

Weight of Package	Price per Pound	Flat Charge
2 lb or less	$1.50	$20.00
Over 2 lb but less than or equal to 6 lb	$3.00	$20.00
Over 6 lb but less than or equal to 10 lb	$4.00	$20.00
Over 10 lb	$4.75	$20.00

Drone Shipping

Weight of Package	Price per Pound	Flat Charge
2 lb or less	$4.50	$0.00
Over 2 lb but less than or equal to 6 lb	$9.00	$0.00
Over 6 lb but less than or equal to 10 lb	$12.00	$0.00
Over 10 lb	$14.25	$0.00

Premium Ground Shipping

Flat charge: $125.00

Write a program that asks the user for the weight of their package and then tells them which method of shipping is cheapest and how much it will cost to ship their package using Sal’s Shippers.
"""

def cost_ground(weight):
  if weight <= 2:
    cost = weight * 1.5 + 20
  elif weight <= 6:
    cost = weight * 3 + 20
  elif weight <= 10:
    cost = weight * 4 + 20
  else:
    cost = weight * 4.75 + 20
  return(cost)

cost_ground(8.4)

cost_premium = 125

def cost_drone(weight):
  if weight <= 2:
    cost = weight *4.5
  elif weight <= 6:
    cost = weight *9
  elif weight <= 10:
    cost = weight *12
  else:
    cost = weight *14.25
  return(cost)

cost_drone(1.5)

def cost(weight):
  ground = cost_ground(weight)
  drone = cost_drone(weight)
  cost_premium = 125
  if ground < drone and ground < cost_premium:
    method = "Ground Shipping"
    price = ground
  elif ground > drone and drone < cost_premium:
    method = "Drone Shipping"
    price = drone
  else:
    method = "Premium Shipping"
    price = cost_premium
  
  print("Shipping method is " +method+ ", best price is " +str(price))



cost(4.8)
cost(41.5)

