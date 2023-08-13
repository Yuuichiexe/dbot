import asyncio
import datetime
from datetime import datetime

from telegram import __version__ as ptb
from telethon import Button

from DazaiRobot import BOT_NAME, BOT_USERNAME, SUPPORT_CHAT
from DazaiRobot import telethn as Horix
from DazaiRobot.events import register

edit_time = 5
""" =======================Horix====================== """
file1 = "https://te.legra.ph/file/596df99c920537cfc75b6.jpg"
file2 = "https://te.legra.ph/file/7d10529848bbde4b447b7.jpg"
file3 = "https://te.legra.ph/file/1fb1f71aa5dcd30f7f928.jpg"
file4 = "https://te.legra.ph/file/0f896bb54001928a5643b.jpg"
""" =======================Horix====================== """

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append(f'{amount} {unit}{"" if amount == 1 else "s"}')
    return ", ".join(parts)


@register(pattern=("/alive"))
async def hmm(yes):
    await yes.get_chat()
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    HoriX = f"**🍃 𝖨'𝗆 𝗐𝗈𝗋𝗄𝗂𝗇𝗀 𝗉𝖾𝗋𝖿𝖾𝖼𝗍𝗅𝗒**\n\n"
    HoriX += f"**𝖬𝗒 𝗎𝗉𝗍𝗂𝗆𝖾:** `{uptime}`\n\n"
    HoriX += f"**𝖬𝗒 𝖼𝗋𝖾𝖺𝗍𝗈𝗋:** [A𝗇𝗈𝗇𝗒𝗆𝗈𝗎𝗌](tg://user?id=6171176459)"
    BUTTON = [
        [
            Button.url("ʜᴇʟᴘ ❓", f"https://t.me/{BOT_USERNAME}?start=help"),
            Button.url("sᴜᴘᴘᴏʀᴛ ♻️", f"https://t.me/{SUPPORT_CHAT}"),
        ]
    ]
    await Horix.send_file(yes.chat_id, file="https://te.legra.ph/file/27047ede7f2e6689c9032.mp4",caption=HoriX, buttons=BUTTON)
    
__mod_name__ = "𝙰ʟɪᴠᴇ"
