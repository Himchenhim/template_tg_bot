from aiogram import types

async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Запуск бота"),
        types.BotCommand("biba", "Узнать свой размер"),
        types.BotCommand("gay", "Проверка на гея"),
        types.BotCommand("ro", "Выдача режима - 'read_only'"),
        types.BotCommand("dead_inside", "Проверка юности"),
        types.BotCommand("mmr","Проверка ММР-а")
    ])