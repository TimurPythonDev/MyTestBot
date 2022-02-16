from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

check_button = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text='✅ проверить подписку',callback_data="check_subs")
    ]]
)
