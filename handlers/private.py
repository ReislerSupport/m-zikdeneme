from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgQAAx0CTv65QgABBfJlYF6VCrGMm6OJ23AxHmD6qUSWESsAAhoQAAKm8XEeD5nrjz5IJFYeBA")
    await message.reply_text(
        f"""**Hey, Merhaba {bn} 🎵

Ben @intikamtimii Tarafından Yapılan Music Botuyum Yardım için dm 👉 [Şahin](https://t.me/intikamtimisahibii).

Ben Türkçe Müzik Botuyum!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                  ],[
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/intikamtimii"
                    ),
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/intikamtimii"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="http://t.me/intikamtimimusicbot"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Grup müzik botu aktif✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/intikamtimii")
                ]
            ]
        )
   )


