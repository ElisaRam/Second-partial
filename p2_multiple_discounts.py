#https://replit.com/join/eyrdhbkcst-elisaramirez4

("Enter the quantity:")
quantity = int(input())
print("Enter the unit of origin (miles, liters or fahrenheit):")
origin = input()
print("Enter the unit of destination (kilometers, gallons or celsius):")
destination = input()

if origin == "miles" and destination == "kilometers":
  result = quantity * 1.609344

elif origin == "liters" and destination == "gallons":
  result = quantity * 0.264172

elif origin == "fahrenheit" and destination == "celsius":
  result = (quantity - 32) * 5/9
  
else:
  print("Invalid answer, make sure you write it the same way as the ones in the options")
    
print(quantity, origin, "is", result, destination)
