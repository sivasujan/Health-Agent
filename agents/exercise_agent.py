def exercise_plan(scaledown_data):
    plan = []

    if scaledown_data["avg_steps"] < 5000:
        plan.append("30 min brisk walking daily")
    else:
        plan.append("Strength training – 4 days/week")
        plan.append("Cardio – 2 days/week")

    if scaledown_data["avg_resting_hr"] > 80:
        plan.append("Add active recovery and stretching")

    return plan
