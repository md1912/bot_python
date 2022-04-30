import asyncio
import aioschedule
from aiogram import types, Dispatcher
from config import bot



async def get_chat_id(message: types.Message):
    global chat_id
    chat_id = message.chat.id
    await bot.send_message(message.chat.id,
                           "got your id")


async def go_to_sleep():
    await bot.send_message(chat_id=chat_id,
                           text="Go to sleep immediately")


async def scheduler():
    aioschedule.every().day.at("02:42").do(go_to_sleep)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(2)


def register_handler_notification(dp: Dispatcher):

    dp.register_message_handler(get_chat_id, lambda word: 'notify' in word.text)