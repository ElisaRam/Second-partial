#https://replit.com/join/cpcuismbei-elisaramirez4

print("Enter the price of the product:")
ogprice = float(input())
print("Enter the category (A, B, C):")
category = input()
print("Enter the number of units purchased:")
units = float(input())

if category == "A":
  discount = .10

elif category == "B":
  discount = .05

elif category == "C":
  discount = .02

else:
  print("Invalid category")

if units > 10:
  discount = discount + 0.05
  print("The additional discount would be a 5% since you bought more than 10 units")

print("The price per product before the discount is",ogprice)
print("The discount applied would be:",discount)

price = ogprice - (ogprice * discount)
print("The price per product with discount included is:",price)
