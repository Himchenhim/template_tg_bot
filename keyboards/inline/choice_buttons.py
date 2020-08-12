from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from data.items import mandarin
from keyboards.inline.callback_datas import buy_callback

mandarin_keyboard = InlineKeyboardMarkup(row_width=2,
                                         inline_keyboard=[
                                             [
                                                 InlineKeyboardButton(
                                                     text="Купить товар",
                                                     callback_data=buy_callback.new(
                                                         item_id=mandarin.get_item_id(),
                                                         IsBought="True",
                                                         IsPlus=False,
                                                         IsMinus=False,
                                                         IsShared=False
                                                     )
                                                 )
                                             ],
                                             [
                                                 InlineKeyboardButton(
                                                     text="👍",
                                                     callback_data=buy_callback.new(
                                                         item_id=mandarin.get_item_id(),
                                                         IsPlus="True",
                                                         IsMinus=False,
                                                         IsShared=False,
                                                         IsBought=False
                                                     )
                                                 ),
                                                 InlineKeyboardButton(
                                                     text="👎",
                                                     callback_data=buy_callback.new(
                                                         item_id=mandarin.get_item_id(),
                                                         IsPlus=False,
                                                         IsMinus="True",
                                                         IsShared=False,
                                                         IsBought=False
                                                     )
                                                 )
                                             ],
                                             [
                                                 InlineKeyboardButton(
                                                     text="Поделиться с другом",
                                                     switch_inline_query=f"{mandarin.get_item_id()}"
                                                 )
                                             ]
                                         ])
