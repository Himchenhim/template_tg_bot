from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext

from loader import dp, db
from aiogram import types
from states import Form


@dp.message_handler(Command('form'))
async def form_query(message: types.Message, ):
    await message.answer("Форма запущена!\n"
                         "Введите Ваше имя:")
    await Form.Q1_name.set()


@dp.message_handler(state=Form.Q1_name)
async def question_1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(dict(name=answer))

    await message.answer("Введите Ваш e-mail:")

    await Form.Q2_email.set()


@dp.message_handler(state=Form.Q2_email)
async def question_2(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(dict(email=answer))
    await message.answer("Введите Ваш номер телефона:")
    await Form.Q3_phone.set()


@dp.message_handler(state=Form.Q3_phone)
async def question_3(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(dict(phone=answer))
    await message.answer("Введите дату рождения: ")
    await Form.next()


@dp.message_handler(state=Form.Q4)
async def question_4(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(dict(date_of_birth=answer))

    data = await state.get_data()
    name = data.get('name')
    email = data.get('email')
    phone = data.get('phone')
    date = data.get('date_of_birth')

    await message.answer("Ты ввел следующие данные:\n\n"
                         f"Имя - {name}\n"
                         f"Email - {email}\n"
                         f"Телефон - {phone}\n"
                         f"Дата рождения = {date}")
    await db.add_user(id=message.from_user.id, Name=name, email=email, phone_number=phone, date_of_birth=date)

    await state.reset_state(with_data=True)
