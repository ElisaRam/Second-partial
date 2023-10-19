def ruby():
  print("Hi, I will give you a care diagnosis for Ruby, depending on the answers I'm given.")
  print("What is the temperature in Celsius? Only type the number")
  temperature = int(input())

  if 25 >= temperature >= 20:
    print("Good conditions.")
  elif temperature < 20:
    print("Bring it inside the house.")
  elif temperature > 25:
    print("Bring it inside the house and turn on the fan.")

  print("What day is it today? Only type the day with the first letter in capital letters")
  day = input()

  if day == "Tuesday" or day == "Thursday" or day == "Saturday":
    print("Water Ruby.")
  else:
    print("You don't have to water Ruby today.")

  print("What is the humidity percentage? Only type the number, without the percentage sign.")
  humidity = int(input())

  if humidity < 20:
    print("You should water Ruby.")
  elif 22 >= humidity >= 20:
    print("Suitable humidity.")
  elif humidity > 22 and day == "Monday" or day == "Wednesday" or day == "Friday" or day == "Sunday":
    print("It is not necessary to water Ruby.")

ruby()
