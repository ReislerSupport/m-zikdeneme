from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""I am **{bn}** !!
I let you play music in your group's voice chat 😉
The commands I currently support are:
⚜️ /oynat - __Yanıtlanan ses dosyasını veya YouTube videosunu bağlantı aracılığıyla oynatır.__
⚜️ /durdur - __Sesli Sohbet Müziği Duraklat.__
⚜️ /devam - __Sesli Sohbet Müziğine Devam Et.__
⚜️ /atla - __Sesli Sohbette ki Şarkıyı Atlar.__
⚜️ /son - __Şarkıyı Sonlandırır.__
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Group 💬", url="https://t.me/intikamtimii"
                    ),
                    InlineKeyboardButton(
                        "Channel 📣", url="https://t.me/intikamtimii"
                    )
                ]
            ]
        )
    )
