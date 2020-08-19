import re
import datetime

from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.utils.exceptions import BadRequest

from filters.group_chat import IsGroup
from loader import dp


@dp.message_handler(IsGroup(),Command("ro", prefixes="!/"))
async def read_onlu_mode(message: types.Message):
    member = message.reply_to_message.from_user
    chat_id = message.chat.id
    member_id = member.id
    command_parse = re.compile(r"(!ro|/ro) ?(\d+)? ?[\w+\D]?")
    parsed = command_parse.match(message.text)
    time = parsed.group(2)
    comment = parsed.group(3)

    if not time:
        time = 5

    time = int(time)

    until_data = datetime.datetime.now() + datetime.timedelta(minutes=time)

    try:
        await message.chat.restrict(user_id = member_id, can_send_messages=False, until_date=until_data)
        await message.reply_to_message.delete()
    except BadRequest as err:
        await message.answer("Ошибка! Пользователь является администратором")
        return

    await message.reply(f"Пользователю {member.id.get_mention(as_html = True)}"
                        f"запрещено писать на {time} минут, по причине <b>{comment}</b>")

