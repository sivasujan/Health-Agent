from pydantic_settings import BaseSettings
from pydantic import ConfigDict

class Settings(BaseSettings):
    # App
    APP_NAME: str = "AI Health Monitoring Agent"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True

    # Wearable APIs
    FITBIT_CLIENT_ID: str = ""
    FITBIT_CLIENT_SECRET: str = ""
    APPLE_HEALTH_CLIENT_ID: str = ""
    APPLE_HEALTH_CLIENT_SECRET: str = ""

    # Database
    DATABASE_URL: str = ""

    # Security
    JWT_SECRET_KEY: str = "change_this"

    # Health thresholds
    MIN_SLEEP_HOURS: int = 7
    MIN_DAILY_STEPS: int = 7000

    # ✅ IMPORTANT FIX
    model_config = ConfigDict(
        env_file=".env",
        extra="allow"   # 👈 THIS FIXES THE ERROR
    )

settings = Settings()
