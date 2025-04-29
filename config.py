import os
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv

# 加载.env文件
env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


class Settings:
    """应用配置类"""

    # 应用配置
    APP_ENV: str = os.getenv("APP_ENV", "development")
    DEBUG: bool = os.getenv("DEBUG", "True").lower() in ("true", "1")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your_secret_key_here")

    # 数据库配置
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///app.db")

    # 服务器配置
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", "8001"))

    # API配置
    API_PREFIX: str = "/api/v1"
    PROJECT_NAME: str = "FastAPI Template"


# 创建全局设置对象
settings = Settings() 