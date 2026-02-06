from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from config import settings
from ingestion.fitbit_api import fetch_fitbit_data

from agents.nutrition_agent import nutrition_recommendation
from agents.exercise_agent import exercise_plan
from agents.sleep_agent import sleep_analysis
from agents.anomaly_agent import detect_anomalies

from goals.goal_engine import set_goals


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    debug=settings.DEBUG
)

# Serve static files (CSS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# HTML templates
templates = Jinja2Templates(directory="templates")


# -------------------------------------------------
# Root Health Check
# -------------------------------------------------
@app.get("/")
def root():
    return {"status": "AI Health Monitoring Agent is running"}


# -------------------------------------------------
# UI Route
# -------------------------------------------------
@app.get("/ui")
def ui(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# -------------------------------------------------
# Main Health Coach API
# -------------------------------------------------
@app.get("/health/{user_id}")
def health_coach(user_id: str):
    """
    Collect wearable data, analyze using AI agents,
    and return personalized health recommendations.
    """

    # 1️⃣ Fetch latest wearable data (mock Fitbit)
    latest_data = fetch_fitbit_data(user_id)

    # 2️⃣ Simulated ScaleDown output (demo-friendly)
    scaledown_data = {
        "avg_steps": 7500,
        "avg_sleep": 6.5,
        "avg_resting_hr": 78,
        "sleep_debt": 1.5
    }

    # 3️⃣ Run AI agents
    nutrition = nutrition_recommendation(user_id, scaledown_data)
    exercise = exercise_plan(scaledown_data)
    sleep = sleep_analysis(scaledown_data)

    anomalies = detect_anomalies(
        type("HealthData", (), latest_data),
        scaledown_data
    )

    goals = set_goals(scaledown_data)

    # 4️⃣ Final response
    return {
        "user_id": user_id,
        "latest_wearable_data": latest_data,
        "nutrition_recommendations": nutrition,
        "exercise_plan": exercise,
        "sleep_insights": sleep,
        "anomalies": anomalies,
        "goals": goals
    }
