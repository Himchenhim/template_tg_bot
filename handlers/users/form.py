from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext

from loader import dp
from aiogram import types
from states import Form


@dp.message_handler(Command('form'))
async def form_query(message: types.Message, ):
    await message.answer("Форма запуущена!\n"
                         "Вопрос №1\n\n"
                         "Введите Ваше имя:")
    await Form.Q1_name.set()


@dp.message_handler(state=Form.Q1_name)
async def question_1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(dict(name=answer))

    await message.answer("Вопрос №2\n\n"
                         "Введите Ваш e-mail:")

    await Form.Q2_email.set()


@dp.message_handler(state=Form.Q2_email)
async def question_2(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(dict(email=answer))

    await message.answer("Вопрос №3\n\n"
                         "Введите Ваш номер телефона:")
    await Form.Q3_phone.set()


@dp.message_handler(state=Form.Q3_phone)
async def question_3(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(dict(phone=answer))
    data = await state.get_data()
    name = data.get('name')
    email = data.get('email')
    phone = data.get('phone')

    await message.answer("Привет! Ты ввел следующие данные:\n\n"
                         f"Имя - {name}\n"
                         f"Email - {email}\n"
                         f"Телефон - {phone}")
    await state.finish()
