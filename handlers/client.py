from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode
from keyboards import client_kb
from config import bot
from database import bot_db
from prosto_parser import animekisa



async def hello(message: types.Message):
    await bot.send_message(message.chat.id,
                           f"Hello {message.from_user.first_name}",
                           reply_markup=client_kb.start_markup)


async def help(message: types.Message):
    await message.reply("1. Команда /quiz Выводить череду вопросоа по pyhton\n"
                        "2.Команда /joke это просто шутка он нечего не делает\n"
                        "3.Команда /info Выводит информацию о боте\n"
                        "4.Команда /start Приветствует пользователя\n"
                        "5.Команда /help выводит список команда\n"
                        "5.Команда /vetka выводит веточные вопросы\n"
                        "6.Команда /register_user регистрирует пользователя\n"
                        "7. Команда /tvshow выводит список фмльмов"  
                        "Note:Бот-Админ будь осторожен он может удалять сообщения")

async def info(message:types.message):
    await bot.send_message(message.chat.id,
                           f'Этого бота создал програмист Арзиев Темирлан\n'
                           f'bot version 1.0')

async def joke(message:types.message):
    await message.reply('Тебя надули это команда нечего не делает 🤣🤣🤣🤣')







async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("Следующая Викторина",
                                         callback_data="button_call_1")
    markup.add(button_call_1)
    question = "Кто создал pyhton?"
    answers = [
        "Гвидо ван Россум",
        "Микилянжело",
        "Стив Жобс",
        "Ворен Бафет",
        "Чин Кан",
        "Нет правильного ответа",
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="Это был Гвидо ван Россум",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup,
    )


async def vetka_quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_5 = InlineKeyboardButton("Хорошо",
                                         callback_data="button_call_5")
    button_call_6 = InlineKeyboardButton("Плохо",
                                         callback_data="button_call_6")
    markup.add(button_call_5,button_call_6)
    await bot.send_message(message.chat.id, 'Как настроение?',
                        reply_markup=markup)


async def get_all_tvshow(message: types.Message):
    await bot_db.sql_select(message)

async def get_all_users(message: types.Message):
    await bot_db.user_select(message)


async def parser_anime(message:types.Message):
    data = animekisa.scrapy_script()
    for i in data:
        await bot.send_message(message.chat.id, i)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(hello,commands=['start'])
    dp.register_message_handler(help, commands=['help'])
    dp.register_message_handler(info, commands=['info'])
    dp.register_message_handler(joke, commands=['joke'])
    dp.register_message_handler(vetka_quiz_1, commands=['vetka'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(get_all_tvshow, commands=['tvshow'])
    dp.register_message_handler(get_all_users, commands=['users'])
    dp.register_message_handler(parser_anime, commands=['skrapy'])
