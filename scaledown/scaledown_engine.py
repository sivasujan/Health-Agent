import numpy as np

def scaledown_health_history(health_data):
    """
    Compress 12-month data into trends & summaries
    """
    steps = [d.steps for d in health_data]
    sleep = [d.sleep_hours for d in health_data]
    rhr = [d.resting_heart_rate for d in health_data]

    summary = {
        "avg_steps": int(np.mean(steps)),
        "avg_sleep": round(np.mean(sleep), 2),
        "avg_resting_hr": int(np.mean(rhr)),
        "step_trend": np.polyfit(range(len(steps)), steps, 1)[0],
        "sleep_debt": max(0, 8 - np.mean(sleep))
    }

    return summary
