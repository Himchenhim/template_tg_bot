from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp
from utils.misc import rate_limit


@rate_limit(5, 'start')
@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = [
        'Список команд: ',
        '/start - Начать диалог',
        '/form - Запрос на получения формыы',
        '/gay - проверка на гея',
        '/dead_inside - проверка на юность',
        '/biba - проверка на размерчик'
    ]
    await message.answer('\n'.join(text))
