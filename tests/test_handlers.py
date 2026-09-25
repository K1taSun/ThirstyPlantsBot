from aiogram import Dispatcher
from thirstyhome.bot.handlers import router
from thirstyhome.main import create_dispatcher


def test_router_handlers_registration() -> None:
    message_handlers = router.message.handlers
    callback_handlers = router.callback_query.handlers

    assert len(message_handlers) == 3
    assert len(callback_handlers) == 1


def test_create_dispatcher() -> None:
    dp = create_dispatcher()
    assert isinstance(dp, Dispatcher)
    assert router in dp.sub_routers
