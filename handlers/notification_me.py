import asyncio
import aioschedule
from aiogram import types, Dispatcher
from config import bot



async def get_user_id(message: types.Message):
    global chat_id
    chat_id = message.chat.id
    await bot.send_message(message.chat.id,
                           "Я уводемлю вас господин")


async def fly():
    await bot.send_message(chat_id=chat_id,
                           text="Вам пора готовится!\n"
                                "Выш самолет в дубай вылетает сегодня в 15:00 ")


async def lesson():
    await bot.send_message(chat_id=chat_id,
                           text="У вас сегодня в 20:00 будет урок в GeekTech по Pyhon\n"
                                "❗НЕ ЗАБУДЬТЕ не опаздвайте Sir❗")


async def scheduler():
    aioschedule.every().friday.at("09:00").do(fly)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(2)

async def scheduler_lesson():
    aioschedule.every().saturday.at("00:01").do(lesson)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(2)


def register_handler_notification_me(dp: Dispatcher):
    dp.register_message_handler(get_user_id, lambda word: 'fly' in word.text)
    dp.register_message_handler(get_user_id, lambda word: 'lesson' in word.text)