#https://replit.com/join/gyebaodxzu-elisaramirez4

distance = float(input("Enter the distance in miles: "))
mpg = float(input("Enter the car's miles per gallon (MPG): "))
gas_price = float(input("Enter the current price of gasoline per gallon: "))
days = int(input("Enter the number of days you plan to travel: "))

total_miles = distance * days

total_gallons = total_miles / mpg

total_cost = total_gallons * gas_price

print("Total cost of the trip: $" + str(round(total_cost, 2)))
