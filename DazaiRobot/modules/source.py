from platform import python_version as y

from pyrogram import __version__ as z
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from telegram import __version__ as o
from telethon import __version__ as s

from DazaiRobot import BOT_NAME, BOT_USERNAME, OWNER_ID, START_IMG, pbot


@pbot.on_message(filters.command(["repo", "source"]))
async def repo(_, message: Message):
    await message.reply_photo(
        photo=START_IMG,
        caption=f"""**ʜᴇʏ {message.from_user.mention},

ɪ ᴀᴍ [{BOT_NAME}](https://t.me/{BOT_USERNAME})**

❱ ᴏᴡɴᴇʀ : ᴀɴᴏɴʏᴍᴏᴜs
❱ 𝙿𝚢𝚝𝚑𝚘𝚗 𝚟𝚎𝚛𝚜𝚒𝚘𝚗: `{y()}`
❱ 𝙻𝚒𝚋𝚛𝚊𝚛𝚢 𝚟𝚎𝚛𝚜𝚒𝚘𝚗: `{o}` 
❱ 𝚃𝚎𝚕𝚎𝚝𝚑𝚘𝚗 𝚟𝚎𝚛𝚜𝚒𝚘𝚗: `{s}` 
❱ 𝙿𝚢𝚛𝚘𝚐𝚛𝚊𝚖 𝚟𝚎𝚛𝚜𝚒𝚘𝚗: `{z}`
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴘᴇʀ", user_id=OWNER_ID),
                    InlineKeyboardButton(
                        "sᴏᴜʀᴄᴇ",
                        url="https://www.youtube.com/watch?v=BBJa32lCaaY",
                    ),
                ]
            ]
        ),
    )


__mod_name__ = "Rᴇᴩᴏ"
