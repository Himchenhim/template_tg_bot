from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery
from aiogram.utils.callback_data import CallbackData

from data.items import mandarin
from keyboards.inline.callback_datas import buy_callback
from keyboards.inline.choice_buttons import mandarin_keyboard
from loader import dp, bot


@dp.message_handler(Command("items"))
async def show_items(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id, photo="https://fimgs.net/himg/o.18106.jpg", caption="Мандаринка",
                         reply_markup=mandarin_keyboard)


@dp.callback_query_handler(buy_callback.filter(IsBought="True"))
async def buy_item(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    item_id = callback_data.get('item_id')
    await bot.send_photo(chat_id=call.message.chat.id, photo="https://fimgs.net/himg/o.18106.jpg",
                         caption=f"Покупай товар!\n"
                                 f"id = {item_id}"
                         )


@dp.callback_query_handler(buy_callback.filter(IsPlus="True"))
async def get_plus_item(call: CallbackQuery):
    await call.answer(text="Тебе понравился этот товар")
    mandarin.plus_rating()


@dp.callback_query_handler(buy_callback.filter(IsMinus="True"))
async def get_plus_item(call: CallbackQuery):
    await call.answer(text="Тебе не понравился этот товар")
    mandarin.minus_rating()
