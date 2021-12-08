from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    # Swagger docs
    app_name: str = Field("API для обработки данных", env="APP_NAME")
    app_version: str = Field("0.1.0", env="APP_VERSION")

    kafka_bootstrap_servers: str = Field("kafka-1:9092", env="KAFKA_BOOTSTRAP_SERVERS")
    movie_events_topic: str = "movie_events"

    log_level: str = Field("INFO", env="LOG_LEVEL")


settings = Settings()
