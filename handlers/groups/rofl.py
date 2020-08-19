import random
from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp, bot


@dp.message_handler(Command("gay", prefixes="!/"))
async def gay_meter(message: types.Message):
    text = f"{message.from_user.get_mention()} гей на {random.randint(1, 100)} %🌈"
    await message.reply(text=text)


@dp.message_handler(Command("dead_inside", prefixes="!/"))
async def dead_inside(message: types.Message):
    text = f"{message.from_user.get_mention()} дэд инсайд на 1/{random.randint(2, 10)}☠"
    await message.reply(text=text)


@dp.message_handler(Command("biba", prefixes="!/"))
async def biba(message: types.Message):
    num = random.randint(5, 30)
    if message.from_user.id == 400372071:
        num = 26
    if num < 20:
        text = f"У {message.from_user.get_mention()} биба {num} см🍆"
        await message.reply(text=text)
    elif num >= 20 and num < 25:
        text = f"У {message.from_user.get_mention()} биба {num} см🍆"
        await message.reply(text=text)
        await bot.send_sticker(chat_id=message.chat.id,
                               sticker="CAACAgIAAxkBAAEBOUpfPSr405MBGgrl_ShVW4WJRlk1XwACXgADUomRI_5xpNU-Z9mEGwQ")
    else:
        text = f"У {message.from_user.get_mention()} биба {num} см🍆\nНастоящий гигант! "
        await message.reply(text=text)
        await bot.send_sticker(chat_id=message.chat.id,
                               sticker="CAACAgQAAxkBAAEBOVBfPS1PudJYBUAgUcEKqWlxrtQu0QACAgEAAtGVsgaa7e7Ww73IkRsE")


@dp.message_handler(Command("mmr", prefixes="!/"))
async def mmr(message: types.Message):
    num = random.randint(300, 11000)
    if num <= 610:
        await message.reply(f"ММР у {message.from_user.get_mention()}: <b>{num}</b>\n\n"
                            f"Этот парень был из тех\n"
                            f"Кто просто любит жить")
        await bot.send_sticker(chat_id=message.chat.id,
                               sticker="CAACAgIAAxkBAAEBOZ1fPU3ac7yKPPRFXuvZ3gd9xwvZ7AACRQADuv8xAAEqsC4x1w1HyxsE")
    elif num > 610 and num <= 1400:
        await message.reply(f"ММР у {message.from_user.get_mention()}: <b>{num}</b>\n<i>Guardian</i>")
        await bot.send_sticker(chat_id=message.chat.id,
                               sticker="CAACAgIAAxkBAAEBOZlfPU3HKUiT97codjBeuFt7aTp67AACOgADuv8xAAEj2WpVru5iMhsE")
    elif num > 1400 and num <= 2150:
        await message.reply(f"ММР у {message.from_user.get_mention()}: <b>{num}</b>\n<i>Crusader</i>")
        await bot.send_sticker(chat_id=message.chat.id,
                               sticker="CAACAgIAAxkBAAEBOaNfPU7R09R61APLfwcZMSaBLSdybAACNAADuv8xAAECscKyZ8rVThsE")
    elif num > 2150 and num <= 2930:
        await message.reply(f"ММР у {message.from_user.get_mention()}: <b>{num}</b>\n<i>Archon</i>")
        await bot.send_sticker(chat_id=message.chat.id,
                               sticker="CAACAgIAAxkBAAEBOalfPU-6oXH8ztEvGrRpFlYIZZcGKQACTQADuv8xAAKel7wx9RCaGwQ")
    elif num > 2930 and num <= 3700:
        await message.reply(f"ММР у {message.from_user.get_mention()}: <b>{num}</b>\n<i>Legend</i>")
        await bot.send_sticker(chat_id=message.chat.id,
                               sticker="CAACAgIAAxkBAAEBOa1fPVArbMyB1A6hpL-Dvn0LpWfDxgACQwADuv8xAAHKr-r0i2JdHhsE")
    elif num > 3700 and num < 4460:
        await message.reply(f"ММР у {message.from_user.get_mention()}: <b>{num}</b>\n<i>Ancient</i>")
        await bot.send_sticker(chat_id=message.chat.id,
                               sticker="CAACAgQAAxkBAAEBObVfPVDQufhMa8Y-EmzN2TJvRo0UgwACPQADeh4OAAE6G7O8chT2fhs")
    else:
        await message.reply(
            f"ММР у {message.from_user.get_mention()}: <b>{num}</b>\n<i>Divine</i>\nТы не взломал систему\nТы стал её частью!")
        await bot.send_sticker(chat_id=message.chat.id,
                               sticker="CAACAgQAAxkBAAEBObdfPVELZSoNdlWixx0Xu-Iup7v_3gAC1AAD0ZWyBvHMr1Xk6on1GwQ")
