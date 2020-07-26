#function for charges ground shipping cost
def ground_shipping(weight):
  if weight<=2:
    return weight*1.50+20
  elif weight>2 and weight<=6:
    return weight*3+20
  elif weight>6 and weight<=10:
    return weight*4+20
  elif weight>10:
    return weight*4.75+20
# charges for premium shipping
premium_ground_shipping = 125
# function for charges drone shipping
def drone_shipping(weight):
  if weight<=2:
    return weight*4.50
  elif weight>2 and weight<=6:
    return weight*9
  elif weight>6 and weight<=10:
    return weight*12
  elif weight>10:
    return weight*14.25
# function for cheapest method of shipping
def shipping(weight):
  ground_ship = ground_shipping(weight)
  drone_ship = drone_shipping(weight)
  if ground_ship<drone_ship and ground_ship<premium_ground_shipping:
    return 'Ground shipping is cheapeast which cost: '+str(ground_ship)
  elif drone_ship<ground_ship and drone_ship<premium_ground_shipping:
    return 'Drone shipping is cheapest which cost: '+str(drone_ship)
  elif premium_ground_shipping<ground_ship and premium_ground_shipping<drone_ship:
    return 'Premium shipping is cheapest which cost: '+str(premium_ground_shipping)
# function call as sample
print(shipping(41.5))