from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import CallbackQuery, Message

from thirstyhome.bot.i18n import (
    Language,
    build_language_keyboard,
    get_message,
    user_languages,
)

router = Router()


@router.message(CommandStart())
async def handle_start(message: Message) -> None:
    user_id = message.from_user.id if message.from_user else 0
    text = get_message(user_id, "choose_language")
    await message.answer(text, reply_markup=build_language_keyboard())


@router.message(Command("language"))
async def handle_language_command(message: Message) -> None:
    user_id = message.from_user.id if message.from_user else 0
    text = get_message(user_id, "choose_language")
    await message.answer(text, reply_markup=build_language_keyboard())


@router.callback_query(F.data.startswith("lang:"))
async def handle_language_choice(callback: CallbackQuery) -> None:
    if not callback.data:
        return

    _, raw_lang = callback.data.split(":", 1)
    try:
        selected_language = Language(raw_lang)
    except ValueError:
        await callback.answer()
        return

    user_id = callback.from_user.id
    user_languages.set(user_id, selected_language)

    await callback.answer()

    confirmation = get_message(user_id, "language_selected")
    welcome = get_message(user_id, "welcome")
    response_text = f"{confirmation}\n\n{welcome}"

    if callback.message and isinstance(callback.message, Message):
        await callback.message.edit_text(response_text)
    else:
        await callback.answer(confirmation, show_alert=True)


@router.message(Command("help"))
async def handle_help(message: Message) -> None:
    user_id = message.from_user.id if message.from_user else 0
    await message.answer(get_message(user_id, "help"))
