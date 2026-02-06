from pydantic import BaseModel
from typing import List
from datetime import date

class DailyHealthData(BaseModel):
    date: date
    steps: int
    calories_burned: float
    sleep_hours: float
    resting_heart_rate: int

class UserHealthProfile(BaseModel):
    user_id: str
    age: int
    height_cm: float
    weight_kg: float
    health_history: List[DailyHealthData]
