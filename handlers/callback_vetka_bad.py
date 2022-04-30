from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import bot

async def vetka_quiz_bad_1(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_11 = InlineKeyboardButton("Упал с космоса ☠",
                                         callback_data="button_call_11")
    button_call_12 = InlineKeyboardButton("Провалил эгзамены",
                                         callback_data="button_call_12")
    markup.add(button_call_11,button_call_12)
    await bot.send_message(call.message.chat.id,'Почему плохо?',
                           reply_markup=markup)

async def vetka_quiz_bad_1_1(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_13 = InlineKeyboardButton("Оживи",
                                         callback_data="button_call_13")
    markup.add(button_call_13)
    await bot.send_message(call.message.chat.id,'Чем могу помочь?',
                           reply_markup=markup)


async def vetka_quiz_bad_1_2(call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id, 'Ты воскрес 😇',)


async def vetka_quiz_bad_2_1_1(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_14 = InlineKeyboardButton("Улететь",
                                         callback_data="button_call_14")
    button_call_15 = InlineKeyboardButton("Перездать",
                                         callback_data="button_call_15")
    markup.add(button_call_14,button_call_15)
    await bot.send_message(call.message.chat.id,'Ты провалил эгзамены что теперь будеш делат?',
                           reply_markup=markup)

async def vetka_quiz_bad_2_1_2(call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id, 'Поздравляю ты здал эгзамены 🎓🏅',)

async def vetka_quiz_bad_2_1_3(call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id, 'Ты улетел в другую страну 🇭🇲🇰🇬🇲🇩🇲🇫🇦🇫',)

def register_handler_callback(dp: Dispatcher):
    dp.register_callback_query_handler(vetka_quiz_bad_1,
                                       lambda call: call.data == "button_call_6")
    dp.register_callback_query_handler(vetka_quiz_bad_1_1,
                                       lambda call: call.data == "button_call_11")
    dp.register_callback_query_handler(vetka_quiz_bad_1_2,
                                       lambda call: call.data == "button_call_13")
    dp.register_callback_query_handler(vetka_quiz_bad_2_1_1,
                                       lambda call: call.data == "button_call_12")
    dp.register_callback_query_handler(vetka_quiz_bad_2_1_2,
                                       lambda call: call.data == "button_call_15")
    dp.register_callback_query_handler(vetka_quiz_bad_2_1_3,
                                       lambda call: call.data == "button_call_14")