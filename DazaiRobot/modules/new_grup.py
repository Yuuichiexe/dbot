import random
from pyrogram import filters, Client
from DazaiRobot import pbot as dazai
from pyrogram.types import (
    Message,
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

photo = [
"https://te.legra.ph/file/c41a9c4f9390da781af12.jpg",
"https://te.legra.ph/file/c41a9c4f9390da781af12.jpg",
"https://te.legra.ph/file/c0a58fdde7782abed9c8d.jpg",
"https://te.legra.ph/file/c0a58fdde7782abed9c8d.jpg",
]


@dazai.on_message(filters.new_chat_members, group=2)
async def _kk(dazai, message):
    chat = message.chat
    for members in message.new_chat_members:
        if members.id == 1711510822:
            count = await dazai.get_chat_members_count(chat.id)

            msg = (
                f"❗ 𝖴𝗐𝗎 𝗌𝗈𝗆𝖾𝗈𝗇𝖾 𝖺𝖽𝖽𝖾𝖽 𝗆𝖾 𝗂𝗇 𝗇𝖾𝗐 𝗀𝗋𝗈𝗎𝗉 ❗\n\n"
                f"◉ 𝖢𝗁𝖺𝗍 𝖨𝖣: {message.chat.id}\n"
                f"◉ 𝖢𝗁𝖺𝗍 𝖴𝗌𝖾𝗋𝗇𝖺𝗆𝖾: @{message.chat.username}\n"
                f"◉ 𝖢𝗁𝖺𝗍 𝖭𝖺𝗆𝖾: {message.chat.title}\n"
                f"◉ 𝖬𝖾𝗆𝖻𝖾𝗋𝗌 𝖼𝗈𝗎𝗇𝗍: {count}"
            )
            await dazai.send_photo(-1001985765132, photo=random.choice(photo), caption=msg, reply_markup=button)
