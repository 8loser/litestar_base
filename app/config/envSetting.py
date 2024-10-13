import os

from pathlib import Path
from dataclasses import dataclass, field


@dataclass
class AppSettings:
    MODE: str = field(default_factory=lambda: os.getenv("MODE", "development"))
    APP_PORT: int = field(
        default_factory=lambda: int(os.getenv("APP_PORT", "5173")))


@dataclass
class Settings:
    app: AppSettings = field(default_factory=AppSettings)

    @classmethod
    def from_env(cls, dotenv_filename: str = ".env") -> 'Settings':
        from litestar.cli._utils import console

        env_file = Path(f"{os.curdir}/{dotenv_filename}")

        if env_file.is_file():
            from dotenv import load_dotenv

            console.print(
                f"[yellow]Loading environment configuration from {dotenv_filename}[/]"
            )

            load_dotenv(env_file, override=True)
        return Settings()


# TODO 使用 lru_cache ?
def get_settings() -> Settings:
    settings_instance = Settings.from_env()

    return settings_instance
