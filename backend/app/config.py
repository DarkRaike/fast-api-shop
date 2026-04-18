from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "FastAPI shop"
    debug: bool = True # позволяет видеть ошибки, в продакшене обычно выключается
    database_url: str = "sqlite:/// .shop.db" 
    cors_origins: list = [ # пути от которых будет принимать на backend запросы от фронтенда
        "http://localhost:5173",
        "http://localhost:3000",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:3000",
    ]
    static_dir: str = "static"
    images_dir: str = "static/images"

    class Config:
        env_file = ".env"

settings = Settings()
