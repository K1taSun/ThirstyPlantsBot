from enum import StrEnum
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


class Language(StrEnum):
    EN = "en"
    PL = "pl"
    UA = "ua"


DEFAULT_LANGUAGE = Language.PL

MESSAGES: dict[Language, dict[str, str]] = {
    Language.PL: {
        "choose_language": (
            "Witaj w ThirstyHome!\n"
            "Wybierz preferowany język / Choose language / Оберіть мову:"
        ),
        "language_selected": "Wybrano język: Polski.",
        "welcome": (
            "Cześć! Jestem ThirstyHome.\n\n"
            "Za chwilę będziesz mógł dodać swoje rośliny i dostawać "
            "przypomnienia o podlewaniu wprost od nich!\n\n"
            "Na razie umiem tylko się przywitać."
        ),
        "help": (
            "Dostępne komendy:\n"
            "/start – powitanie i wybór języka\n"
            "/language – zmiana języka\n"
            "/help – pomoc"
        ),
    },
    Language.EN: {
        "choose_language": (
            "Welcome to ThirstyHome!\n"
            "Choose your language / Wybierz preferowany język / Оберіть мову:"
        ),
        "language_selected": "Language set to English.",
        "welcome": (
            "Hello! I am ThirstyHome.\n\n"
            "Soon you will be able to add your plants and receive "
            "watering reminders directly from them!\n\n"
            "For now, I can only say hello."
        ),
        "help": (
            "Available commands:\n"
            "/start – welcome and language selection\n"
            "/language – change language\n"
            "/help – help message"
        ),
    },
    Language.UA: {
        "choose_language": (
            "Ласкаво просимо до ThirstyHome!\n"
            "Оберіть мову / Choose language / Wybierz preferowany język:"
        ),
        "language_selected": "Мову встановлено: Українська.",
        "welcome": (
            "Привіт! Я ThirstyHome.\n\n"
            "Незабаром ви зможете додати свої рослини та отримувати "
            "нагадування про полив безпосередньо від них!\n\n"
            "Поки що я можу лише привітатися."
        ),
        "help": (
            "Доступні команди:\n"
            "/start – привітання та вибір мови\n"
            "/language – зміна мови\n"
            "/help – довідка"
        ),
    },
}


class UserLanguageStorage:
    def __init__(self) -> None:
        self._preferences: dict[int, Language] = {}

    def get(self, user_id: int) -> Language:
        return self._preferences.get(user_id, DEFAULT_LANGUAGE)

    def set(self, user_id: int, language: Language) -> None:
        self._preferences[user_id] = language


user_languages = UserLanguageStorage()


def get_message(user_id: int, key: str) -> str:
    lang = user_languages.get(user_id)
    return MESSAGES.get(lang, MESSAGES[DEFAULT_LANGUAGE]).get(key, "")


def build_language_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="English", callback_data=f"lang:{Language.EN}"),
                InlineKeyboardButton(text="Polski", callback_data=f"lang:{Language.PL}"),
                InlineKeyboardButton(text="Українська", callback_data=f"lang:{Language.UA}"),
            ]
        ]
    )
