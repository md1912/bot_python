from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

help_button = KeyboardButton('/help')
quiz_button = KeyboardButton('/quiz')
info_button = KeyboardButton('/info')
joke_button = KeyboardButton('/joke')
vetka_button = KeyboardButton('/vetka')
tvshow_button = KeyboardButton('/tvshow')
users_button = KeyboardButton('/users')
register_user_button = KeyboardButton('/register_user')

start_markup = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
start_markup.row(help_button,quiz_button,
                 info_button,joke_button,
                 vetka_button,register_user_button,
                 tvshow_button,
                 users_button)