def detect_anomalies(latest_data, scaledown_data):
    alerts = []

    if latest_data.resting_heart_rate > scaledown_data["avg_resting_hr"] + 10:
        alerts.append("Abnormal heart rate detected.")

    if latest_data.sleep_hours < 4:
        alerts.append("Severe sleep deprivation detected.")

    return alerts
