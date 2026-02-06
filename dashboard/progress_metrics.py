def calculate_progress(user_data):
    last_7_days = user_data[-7:]

    avg_steps = sum(d.steps for d in last_7_days) // 7
    avg_sleep = round(sum(d.sleep_hours for d in last_7_days) / 7, 2)

    return {
        "weekly_avg_steps": avg_steps,
        "weekly_avg_sleep": avg_sleep
    }
