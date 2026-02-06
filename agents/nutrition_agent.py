def nutrition_recommendation(user, scaledown_data):
    recs = []

    if scaledown_data["avg_steps"] > 8000:
        recs.append("Increase protein intake for muscle recovery.")

    if scaledown_data["avg_sleep"] < 6:
        recs.append("Avoid heavy dinners late at night.")

    recs.append("Add fruits and vegetables for micronutrient balance.")

    return recs
