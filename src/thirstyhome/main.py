import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher

from thirstyhome.bot.handlers import router
from thirstyhome.config import load_settings


def create_bot(token: str) -> Bot:
    return Bot(token=token)


def create_dispatcher() -> Dispatcher:
    dispatcher = Dispatcher()
    dispatcher.include_router(router)
    return dispatcher


async def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )

    settings = load_settings()
    bot = create_bot(settings.bot_token)
    dp = create_dispatcher()

    logging.info("Starting ThirstyHome polling...")
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Bot stopped.")
        sys.exit(0)
