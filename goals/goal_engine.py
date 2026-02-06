def set_goals(scaledown_data):
    goals = {}

    goals["daily_steps"] = 10000 if scaledown_data["avg_steps"] > 7000 else 7000
    goals["sleep_hours"] = 8
    goals["weekly_workouts"] = 5

    return goals
