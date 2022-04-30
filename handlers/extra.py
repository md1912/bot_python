from aiogram import types,Dispatcher
from config import bot


async def secret_word(message:types.Message):
    await message.reply("Да мой Господин 🙇")

async def echo_and_ban(message:types.Message):
    ban_words = ['bitch','damn','fack','дурак']
    # if message.text.lower() in ban_words:
    #     await bot.send_message(message.chat.id,
    #                            f'Ban for the word,User: {message.from_user.full_name}')
    #     await bot.delete_message(message.chat.id,
    #                              message.message_id)

    for i in ban_words:
        if i in message.text.lower().replace(" ",""):
            await bot.send_message(message.chat.id,
                                   f'Ban for the word,User: {message.from_user.full_name}')
            await bot.delete_message(message.chat.id,
                                    message.message_id)
    if message.text.startswith("Pin"):
        await bot.pin_chat_message(message.chat.id,message.message_id)
    elif message.text.lower() == 'dice':
        await bot.send_dice(message.chat.id,emoji='🎲')
    await message.reply('Unregistered command')



def register_handler_other(dp:Dispatcher):
    dp.register_message_handler(secret_word,lambda word: 'ботчик' in word.text)
    dp.register_message_handler(echo_and_ban)