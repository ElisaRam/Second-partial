https://replit.com/join/rrtbuffpwf-elisaramirez4 

print("Hello! This is the mental health questionary")
print("You'll answer with yes or no to each question and I'll be able to make recommendations for you. Let's begin!")
      
print("Do you sleep from 7 to 9 hours a day?")
sleep = input()

print("Do you do any kind of physical activity?")
exercise = input()

print("Are you a social person?")
social = input()

print("Do you have a balanced diet?")
diet = input()

print("Do you practice meditation or yoga?")
meditation = input()

print("Do you like to spend time outside?")
outside = input()

if sleep == "yes" and exercise == "yes" and social == "yes" and diet == "yes" and meditation == "yes" and outside == "yes":
  print("Your mental health is excellent! You are an active, social, healthy, and balanced person. There are no special recommendations for you, keep it up!")
else:
  if sleep == "no":
    print("You should sleep more in order to have a healthy mind and body.")
  if exercise == "no":
    print("Physical activity is really important in your daily life, consider exercising at least 3 times a week.")
  if social == "no":
    print("Social interaction is important in your daily life, consider talking to people a little bit more")
  if diet == "no":
    print("A balanced diet is essential for your mental health, consider eating a healthy meal a day.")
  if meditation == "no":
    print("Meditation can really help to cope with stress or anxiety, try doing it at least for 10 minutes a day.")
  if outside == "no":
    print("You should spend more time on the outside, enjoying nature and breathing fresh air.")
