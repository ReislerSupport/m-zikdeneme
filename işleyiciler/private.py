from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""Merhaba**{bn}** !!

Şu Anda Harika Bir Music Botuna Bakıyorsun 😉
                👇👇👇👇👇
@ReislerSupport DC Oyun Botumuzu Denediniz Mi?
                👆👆👆👆👆

Şu anda desteklediğim komutlar:

⚜️ /oynat - __👉Şarkıyı Başlatır👈__
⚜️ /durdur - __👉Şarkıyı Durdurur👈__
⚜️ /devam - __👉Şarkıya Devam Eder👈__
⚜️ /atla - __👉Şarkıyı Değiştirir👈__
⚜️ /bul - __👉YouTubeden şarkıyı arar👈__
⚜️ /son - __👉Şarkıyı Sonlandırır👈__
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Group 💬", url="https://t.me/ReislerSupport"
                    ),
                    InlineKeyboardButton(
                        "Channel 📣", url="https://t.me/ReislerSupport"
                    )
                ]
            ]
        )
    )
