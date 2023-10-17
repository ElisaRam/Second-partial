https://replit.com/join/fajlwnscjj-elisaramirez4

print("What is your average grade?")
grade = int(input())

print("Do you participate in class? (yes/no)")
participation = input()

print("What is your project score?")
project = int(input())

if grade >=75 and participation == "yes":
  print("You are in good academic standing")
  if project > 90:
    print("You've received a distinction!")
  
elif grade < 60 or participation == "no":
  print("You need to improve your performance")
  if project > 90:
    print("You've received a distinction!")

else:
  print("Invalid answers, repeat.")
