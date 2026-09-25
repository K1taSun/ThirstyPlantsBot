from thirstyhome.bot.i18n import (
    DEFAULT_LANGUAGE,
    MESSAGES,
    Language,
    UserLanguageStorage,
    build_language_keyboard,
    get_message,
)


def test_language_enum_values() -> None:
    assert Language.EN == "en"
    assert Language.PL == "pl"
    assert Language.UA == "ua"


def test_messages_structure_consistency() -> None:
    required_keys = {"choose_language", "language_selected", "welcome", "help"}
    for lang in Language:
        assert lang in MESSAGES, f"Missing language: {lang}"
        missing_keys = required_keys - MESSAGES[lang].keys()
        assert not missing_keys, f"Language {lang} missing keys: {missing_keys}"


def test_user_language_storage() -> None:
    storage = UserLanguageStorage()
    assert storage.get(999) == DEFAULT_LANGUAGE

    storage.set(999, Language.UA)
    assert storage.get(999) == Language.UA

    storage.set(999, Language.EN)
    assert storage.get(999) == Language.EN


def test_get_message() -> None:
    msg_pl = get_message(1001, "language_selected")
    assert "Polski" in msg_pl


def test_build_language_keyboard_buttons() -> None:
    keyboard = build_language_keyboard()
    buttons = keyboard.inline_keyboard[0]

    assert len(buttons) == 3
    button_texts = [b.text for b in buttons]
    callbacks = [b.callback_data for b in buttons]

    assert button_texts == ["English", "Polski", "Українська"]
    assert callbacks == ["lang:en", "lang:pl", "lang:ua"]

    # Verify no flag emojis in button text
    for text in button_texts:
        assert not any(char in text for char in ["🇬🇧", "🇵🇱", "🇺🇦"])
