from aiogram.filters.state import State,StatesGroup

class RegisterGroup(StatesGroup):
    fullname = State()
    title = State()
    content = State()
    check = State()