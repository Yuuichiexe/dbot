import asyncio
import datetime
from datetime import datetime

from telegram import __version__ as ptb
from telethon import Button

from DazaiRobot import BOT_NAME, BOT_USERNAME, SUPPORT_CHAT
from DazaiRobot import pbot as Horix
from DazaiRobot.events import register

edit_time = 5
""" =======================Horix====================== """
file1 = "https://graph.org/file/8af7c21f6b5c5dfb55241.jpg"
file2 = "https://graph.org/file/2808aba74d5f1667f71ee.jpg"
file3 = "https://graph.org/file/488755b1ed61dffb45dca.jpg"
file4 = "https://graph.org/file/354a3c1adb16121b89848.jpg"
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
    HoriX = f"**☘️I'm {BOT_NAME}\nI'm Working Perfectly **\n\n"
    HoriX += f"**✨My Uptime :** `{uptime}`\n\n"
    HoriX += f"**👺My Creator:** [TOAA](https://t.me/Itz_Shion_II)"
    BUTTON = [
        [
            Button.url("♻️Help", f"https://t.me/{BOT_USERNAME}?start=help"),
            Button.url("🌱Support", f"https://t.me/{SUPPORT_CHAT}"),
        ]
    ]
    await Horix.send_file(yes.chat_id, file="https://graph.org/file/7d58c0096a704c8a93e21.mp4",caption=HoriX, buttons=BUTTON)
    
__mod_name__ = "Aʟɪᴠᴇ"
