import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Settings:
    bot_token: str


def load_settings() -> Settings:
    token = os.getenv("BOT_TOKEN")
    if not token or not token.strip():
        raise ValueError("BOT_TOKEN is required. Set it in .env file.")
    return Settings(bot_token=token.strip())
