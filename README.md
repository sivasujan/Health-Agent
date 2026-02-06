# 🧠 AI Health Monitoring Agent

A full-stack AI-powered health monitoring system that provides personalized health recommendations using wearable data and multi-agent intelligence.

---

## 🚀 Features
- Wearable data ingestion (Fitbit – mock integration)
- Multi-agent AI system:
  - Nutrition Agent
  - Exercise Planning Agent
  - Sleep Analysis Agent
  - Anomaly Detection Agent
- ScaleDown-based long-term health memory
- Personalized goal setting
- Clean web UI with HTML & CSS
- FastAPI backend with Swagger documentation

---

## 🏗 Architecture
- **Backend:** FastAPI
- **Frontend:** HTML, CSS, JavaScript
- **AI Logic:** Multi-agent reasoning
- **Health Memory:** ScaleDown summarization

---

## ▶️ How to Run Locally

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload

Open in Browser

UI: http://127.0.0.1:8000/ui

API Docs: http://127.0.0.1:8000/docs

ScaleDown-powered Health Memory:
The system compresses long-term wearable health data into compact summaries, allowing the AI coach to generate fast, personalized, and explainable health recommendations using a user’s historical baseline instead of generic thresholds.

