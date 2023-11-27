
from data.config import ADMINS
from loader import dp,bot
from aiogram import types,F
from aiogram.filters import Command
from states.mystates import RegisterGroup
from aiogram.fsm.context import FSMContext
from keyboards.default.buttons import checkbtn
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton,CallbackQuery
# CallbackData
@dp.message(Command('register'))
async def get_name(message:types.Message,state:FSMContext):
    await message.answer("Ism familiyangizni kiriting! ")
    await state.set_state(RegisterGroup.fullname)
@dp.message(F.text,RegisterGroup.fullname)
async def get_title(message:types.Message,state:FSMContext):
    fullname = message.text
    await state.update_data({
        'fullname':fullname
    })
    await message.answer("Contentingizni sarlavhasini yuboring !")
    await state.set_state(RegisterGroup.title)
@dp.message(F.text,RegisterGroup.title)
async def get_content(message:types.Message,state:FSMContext):
    title = message.text
    await state.update_data({
        'title':title
    })
    await message.answer("Contentingizni yuboring !")
    await state.set_state(RegisterGroup.content)
@dp.message(F.text,RegisterGroup.content)
async def final(message:types.Message,state:FSMContext):
    content = message.text
    await state.update_data({
        'content':content
    })
    data = await state.get_data()
    result = (f"👤 Foydalanuvchi : {data['fullname']}\n"
              f"📄 Sarlavha : {data['title']}\n"
              f"🗂 Content : {data['content']}")
    await message.answer(result)
    await message.answer("Ma'lumotlar to'grimi ?",reply_markup=checkbtn)
    await state.set_state(RegisterGroup.check)

# action_cb = CallbackData("action", "value")
@dp.message(F.text,RegisterGroup.check)
async def check(message:types.Message,state:FSMContext):
    if message.text == "✅ Ha":
        # id = message.from_user.id
        data = await state.get_data()
        # button = InlineKeyboardMarkup()
        result = (f"👤 Foydalanuvchi : {data['fullname']}\n"
                  f"📄 Sarlavha : {data['title']}\n"
                  f"🗂 Content : {data['content']}")
        # button.row(InlineKeyboardButton(text="✅ E'lon qilish",callback_data=action_cb.new(value=f'elon{id}')))
        # button.row(InlineKeyboardButton(text="❌ Rad etish", callback_data=action_cb.new(value=f'rad{id}')))
        await bot.send_message(chat_id=ADMINS[0],text=result)
        await state.clear()
    else:
        await message.answer(text="Bot sizning xizmatingizda!\n"
                                  "Iltimos Content yozish uchun /register buyrug'ini bering!")