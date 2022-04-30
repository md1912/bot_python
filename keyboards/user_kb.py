from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

button_downlowd = KeyboardButton('/Регистрация')
button_chanel = KeyboardButton('/Отмена')


button_user = ReplyKeyboardMarkup(
    resize_keyboard=True).row(button_downlowd, button_chanel)