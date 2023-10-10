#https://replit.com/join/xoeangbkcj-elisaramirez4

weight_kg = float(input("Enter your weight in kilograms: "))
duration_minutes = int(input("Enter the duration of the activity in minutes: "))
activity = input("Enter the type of activity (running, swimming, cycling): ").lower()

if activity == "running":
    calories_burned = 0.076 * weight_kg * duration_minutes
elif activity == "swimming":
    calories_burned = 0.068 * weight_kg * duration_minutes
elif activity == "cycling":
    calories_burned = 0.035 * weight_kg * duration_minutes
else:
    print("Invalid activity. Try again.")

print("The calories you burned are:",calories_burned)
