from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """Application settings loaded from .env file."""
    #App
    APP_NAME: str = "Pipelet"
    APP_VERSION: str = "0.1.0"
    DEBUG: bool = True
    
    # Database
    DATABASE_URL: str = "postgresql://pipelet:pipelet@localhost:5432/pipelet"

    #Redis
    REDIS_URL: str = "redis://localhost:6379"

    #MinIO
    MINIO_ENDPOINT: str = "localhost:9000"
    MINIO_ACCESS_KEY: str = "minioadmin"
    MINIO_SECRET_KEY: str = "minioadmin"

    #MLflow
    MLFLOW_TRACKING_URI: str = "http://localhost:5001"

    #RabbitMQ
    RABBITMQ_URL: str = "amqp://guest:guest@localhost:5672/"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

# Single instance used across the app
settings = Settings()