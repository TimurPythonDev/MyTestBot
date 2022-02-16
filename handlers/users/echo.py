from aiogram import types

from loader import dp
import wikipedia

wikipedia.set_lang('ru')


# Википедиа Бот
@dp.message_handler()
async def sendWiki(message: types.Message):

    try:
        respond = wikipedia.summary(message.text)
        await  message.answer(respond)
    except:
        await message.answer("У нас нет статьи на эту тему")

