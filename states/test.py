from aiogram.dispatcher.filters.state import State, StatesGroup


class Form(StatesGroup):
    Q1_name = State()
    Q2_email = State()
    Q3_phone = State()
    Q4 = State()
