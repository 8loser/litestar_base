import os

from pathlib import Path
from dataclasses import dataclass, field


@dataclass
class AppSettings:
    MODE: str = field(default_factory=lambda: os.getenv("MODE", "development"))
    # TODO APP_PORT 加上應用
    APP_PORT: int = field(
        default_factory=lambda: int(os.getenv("APP_PORT", "3000")))
    ALLOWED_CORS_ORIGINS: list[str] | str = field(
        default_factory=lambda: os.getenv("ALLOWED_CORS_ORIGINS", '["*"]'))


@dataclass
class Settings:
    app: AppSettings = field(default_factory=AppSettings)

    @classmethod
    def from_env(cls, dotenv_filename: str = ".env") -> 'Settings':
        env_file = Path(f"{os.curdir}/{dotenv_filename}")

        if env_file.is_file():
            from dotenv import load_dotenv
            load_dotenv(env_file, override=True)
        return Settings()


# TODO 使用 lru_cache ?
def get_settings() -> Settings:
    return Settings.from_env()
