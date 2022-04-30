from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode

from config import bot


async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton("Следующая Викторина",
                                         callback_data="button_call_2")
    markup.add(button_call_2)
    question = "Каком году был основан Python?"
    answers = [
        "1900г",
        "2000г",
        "в начале 1980",
        "конце 1980г",
        "1844",
        "1945",
        "Нет правильного ответа",
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Это было в начале 1980",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup,
    )



async def quiz_3(call: types.CallbackQuery):
    question = "Какая функция возврашает 3 пункт задачи"
    answers = [
        "print(list += list)",
        "def sum_slt(lst):\nsum = lst + lst\nprint(sum)",
        "lamda(x+x)",
        "Нет правильного ответа",
    ]
    photo = open("media/mwe.jpg", "rb")
    await bot.send_photo(call.message.chat.id, photo=photo)
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="This is too easy for explanation",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,

    )






def register_handler_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2,
                                       lambda call: call.data == "button_call_1")
    dp.register_callback_query_handler(quiz_3,
                                       lambda call: call.data == "button_call_2")