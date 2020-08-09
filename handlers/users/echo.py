from aiogram import types
from loader import dp


@dp.message_handler()
async def bot_echo(message: types.Message):
    await message.answer("Обработчик к данному апдейту не задан.\n"
                         "Ввывести апдейт:\n\n"
                         f"{message.text}")
