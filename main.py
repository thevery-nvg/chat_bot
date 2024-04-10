from aiogram import Bot, Dispatcher
import asyncio
from aiogram.types import Message
from chat import chat_bot_answer

bot = Bot(token="5816435930:AAGoEM54yRNXqbclwbaqBfHaeV6SJeD1exs")
dp = Dispatcher(bot=bot)


def on_startup():
    print("Бот успешно запущен")


async def main():
    on_startup()
    await dp.start_polling(bot)


@dp.message()
async def main_menu(msg: Message):
    x = await chat_bot_answer(msg.text)
    await bot.send_message(msg.from_user.id, x)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот успешно остановлен')
