import random
from datetime import date

def fetch_fitbit_data(user_id: str):
    """Mock Fitbit API"""
    return {
        "date": date.today(),
        "steps": random.randint(3000, 12000),
        "calories_burned": random.uniform(1800, 2800),
        "sleep_hours": round(random.uniform(5, 8), 1),
        "resting_heart_rate": random.randint(55, 90)
    }
