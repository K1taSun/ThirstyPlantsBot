import pytest
from thirstyhome.config import Settings, load_settings


def test_settings_initialization() -> None:
    settings = Settings(bot_token="test_token_123")
    assert settings.bot_token == "test_token_123"


def test_load_settings_success(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("BOT_TOKEN", "valid_token_xyz")
    settings = load_settings()
    assert settings.bot_token == "valid_token_xyz"


def test_load_settings_missing(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("BOT_TOKEN", raising=False)
    with pytest.raises(ValueError, match="BOT_TOKEN is required"):
        load_settings()


def test_load_settings_empty(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("BOT_TOKEN", "   ")
    with pytest.raises(ValueError, match="BOT_TOKEN is required"):
        load_settings()
