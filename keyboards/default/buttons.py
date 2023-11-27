from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

checkbtn = ReplyKeyboardMarkup(resize_keyboard=True,
                               keyboard=[
                                   [
                                       KeyboardButton(text="✅ Ha"),
                                       KeyboardButton(text="❌ Yo'q")
                                   ]
                               ],one_time_keyboard=True
)