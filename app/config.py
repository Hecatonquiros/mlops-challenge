import secrets
from pydantic_settings import BaseSettings

class Settings(BaseSettings):


    SECRET_KEY: str = secrets.token_hex(32).upper()
    ALGORITHM: str = "HS256"

    LOG_PATH_FILE: str = "app/logs/app.log"

    ACCESS_TOKEN_TIME: int = 5

settings = Settings()