from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI项目"
    VERSION: str = "1.0.0"
    DEBUG: bool = True

    # Database Configuration
    DATABASE_URL: str = "postgresql://root:fuwenhao@127.0.0.1:5432/aistak_db?sslmode=prefer"

    model_config = {"env_file": ".env"}

settings = Settings()