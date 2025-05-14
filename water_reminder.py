
def get_user_input():
    try:
        weight = float(input("Enter your weight in kg: "))
        age = int(input("Enter your age in years: "))
        if weight <= 0 or age <= 0:
            raise ValueError("Weight and age must be positive numbers.")
        return weight, age
    except ValueError as ve:
        print(f"Input error: {ve}")
        return None, None

def calculate_water_intake(weight):
    return round(weight * 0.033, 2)

def suggest_reminder_interval(age):
    if age < 18:
        return 3
    elif age <= 55:
        return 2
    else:
        return 1.5

def recommend_water_temperature(age):
    if age < 18:
        return "Cool"
    elif age <= 55:
        return "Room Temperature"
    else:
        return "Lukewarm"

def main():
    weight, age = get_user_input()
    if weight and age:
        intake = calculate_water_intake(weight)
        interval = suggest_reminder_interval(age)
        temp = recommend_water_temperature(age)

        print(f"\n✅ Recommended Water Intake: {intake} liters/day")
        print(f"🔔 Reminder every {interval} hours")
        print(f"💧 Ideal Water Temperature: {temp}")

if __name__ == "__main__":
    main()
