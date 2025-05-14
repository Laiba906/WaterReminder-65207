
#  Water Reminder App

**Name**: Laiba Imran  
**Student ID**: 65207

---

##  Features

- Calculates recommended daily water intake based on weight
- Suggests reminder interval based on age
- Recommends ideal water temperature:
  -  Cool for youth
  -  Room Temperature for adults
  -  Lukewarm for elders
- Handles invalid or missing input with proper error messages

---

##  How to Use

1. Run the app.
2. Enter your weight in kg and age in years.
3. The app will:
   - Show recommended water intake (in liters)
   - Suggest how often to drink (reminder interval)
   - Recommend ideal temperature for drinking water

---

##  Testing

- Unit tests are written using `pytest` in `test_water_reminder.py`.
- Run with:
  ```bash
  pytest test_water_reminder.py
