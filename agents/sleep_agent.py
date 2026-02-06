def sleep_analysis(scaledown_data):
    insights = []

    if scaledown_data["avg_sleep"] < 7:
        insights.append("Increase sleep duration to 7–8 hours.")
        insights.append("Avoid screens 1 hour before bed.")

    if scaledown_data["sleep_debt"] > 1:
        insights.append("Recover sleep debt over the next 3 days.")

    return insights
