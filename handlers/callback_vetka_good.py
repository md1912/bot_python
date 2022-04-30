from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import bot

async def vetka_quiz_good_1(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_7 = InlineKeyboardButton("Хорошо сдал дз 💯",
                                         callback_data="button_call_7")
    button_call_8 = InlineKeyboardButton("Хорошое насторение",
                                         callback_data="button_call_8")
    markup.add(button_call_7,button_call_8)
    await bot.send_message(call.message.chat.id,'Почему хорошо?',
                           reply_markup=markup)

async def vetka_quiz_good_2_1(call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id,'Красавчик')

async def vetka_quiz_good_2_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_9 = InlineKeyboardButton("Погода 🌞🌈",
                                         callback_data="button_call_9")
    button_call_10 = InlineKeyboardButton("Кино 🎬",
                                         callback_data="button_call_10")
    markup.add(button_call_9,button_call_10)
    await bot.send_message(call.message.chat.id,'Что тебя обрадовало?',
                           reply_markup=markup)

async def vetka_quiz_good_2_3(call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id,'Удачного дня')

async def vetka_quiz_good_2_4(call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id,'Хорошего просмотра 🍿')






def register_handler_callback(dp: Dispatcher):
    dp.register_callback_query_handler(vetka_quiz_good_1,
                                       lambda call: call.data == "button_call_5")
    dp.register_callback_query_handler(vetka_quiz_good_2_1,
                                       lambda call: call.data == "button_call_7")
    dp.register_callback_query_handler(vetka_quiz_good_2_2,
                                       lambda call: call.data == "button_call_8")
    dp.register_callback_query_handler(vetka_quiz_good_2_3,
                                       lambda call: call.data == "button_call_9")
    dp.register_callback_query_handler(vetka_quiz_good_2_4,
                                       lambda call: call.data == "button_call_10")